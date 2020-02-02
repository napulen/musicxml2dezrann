# musicxml2dezrann - turns lyrics within musicxml files into Dezrann's json file
# Copyright (C) 2020  Nestor Napoles Lopez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from datetime import datetime
import music21
import argparse

version = "0.1.0"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "musicxml",
        type=str,
        help="The input MusicXML file with lyric annotations")
    parser.add_argument(
        "annotation_type", 
        help="The type of annotation your lyrics are",
        type=str,
        metavar="annotation_type",
        choices=[
            "Pattern",
            "Theme",
            "Tonality",
            "Modulation",
            "Harmony",
            "Pedal",
            "Cadence",
            "Harmonic sequence",
            "Texture",
            "Structure",
            "Comment"
        ],
        default="Comment")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    extension = ['.musicxml', '.xml', '.mxl']
    for each_extension in extension:
        filename = args.musicxml.replace(each_extension, '')
    # Get the annotations
    score = music21.converter.parse(args.musicxml)
    dezrann = {
        "meta": {
            "title": score.metadata.title,
            "name": args.annotation_type,
            "date": str(datetime.now()),
            "producer": "musicxml2dezrann v" + version
        },
        "labels": []
    }
    notes_with_lyrics = [n for n in score.flat.notes if n.lyric]
    for n in notes_with_lyrics:
        dezrann_entry = {
            'type': args.annotation_type,
            'start': n.offset,
            'line': 'all',
            'tag': n.lyric
        }
        dezrann['labels'].append(dezrann_entry)
    with open(filename + ".dez", "w") as f:
        f.write(json.dumps(dezrann))