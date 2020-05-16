#!/usr/bin/env python3

import argparse
import json
import os
from collections import defaultdict
from statistics import mean
from xml.dom import Node
from xml.dom.minidom import parse
import mutagen

parser = argparse.ArgumentParser(description='Associate Amarok ratings to MBIDs')

parser.add_argument('input', help='Input XML file, the export from Amarok')
parser.add_argument('output', help='Output JSON file, the ratings associated to MBIDs')
args = parser.parse_args()

def load(input):
    print('Loading {}'.format(input))
    dom = parse(args.input)
    root = dom.documentElement
    root.tagName == 'resultset' or exit('Invalid input XML file')
    rows = [row for row in root.childNodes if row.nodeType == Node.ELEMENT_NODE]
    by_path = {}

    def value_of(row, name):
        f = next(f for f in row.childNodes if f.nodeType == Node.ELEMENT_NODE and f.getAttribute('name') == name)
        return f.firstChild.data

    for row in rows:
        row.tagName == 'row' or exit('Invalid input XML file')
        root = value_of(row, 'root')
        rel_path = value_of(row, 'rel_path')
        rating = int(value_of(row, 'rating'))
        path = os.path.join(root, rel_path)
        if rating > 0:
            if not os.path.exists(path):
                print('Cannot find {}, skipping'.format(path))
                continue
            by_path[path] = rating

    print('{} files with ratings'.format(len(by_path)))
    return by_path

def assign(by_path):

    def parse_recording_ids(tags):
        ids = []
        for t in tags.values():
            if isinstance(t, mutagen.id3.UFID) and t.owner == 'http://musicbrainz.org':
                ids.append(t.data.decode('ascii'))
        if 'MUSICBRAINZ_TRACKID' in tags:
            ids = ids + tags['MUSICBRAINZ_TRACKID']
        if '----:com.apple.iTunes:MusicBrainz Track Id' in tags:
            ids = ids + [x.decode('ascii') for x in tags['----:com.apple.iTunes:MusicBrainz Track Id']]
        return ids

    print('Matching files and assigning ratings')
    by_recording_id = defaultdict(list)
    matched = 0
    unmatched = 0
    for path in by_path:
        tags = mutagen.File(path).tags
        recording_ids = parse_recording_ids(tags)
        if len(recording_ids) > 1:
            print('Ambiguous recording MBIDs found for {}: {}'.format(path, recording_ids))
        elif not recording_ids:
            print('Cannot find recoding MBID for {}'.format(path))
            unmatched = unmatched + 1
        else:
            matched = matched + 1
            for recording_id in recording_ids:
                by_recording_id[recording_id].append(by_path[path])

    print('{} ratings to assign'.format(len(by_path)))
    print('{} matched files'.format(matched))
    print('{} unmatched files'.format(unmatched))

    assigned = { 'recording': by_recording_id }

    return assigned

def rate(assigned):
    def rate_list(l):
        return mean(map(float, l))
    def rate_all(kl):
        return { k: rate_list(l) for k, l in kl.items() }
    return { k: rate_all(kl) for k, kl in assigned.items() }

def save(output, ratings):
    print('Writing ratings to {}'.format(output))
    data = { 'ratings': ratings }
    with open(output, 'w') as out:
        json.dump(data, out, indent=4)

by_path = load(args.input)

assigned = assign(by_path)

ratings = rate(assigned)

save(args.output, ratings)
