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

version = "0.1.0"

if __name__ == '__main__':
    dezrann = {
        "meta": {
            "title": None,
            "name": None,
            "date": str(datetime.now()),
            "producer": "musicxml2dezrann v" + version
        },
        "labels": []
    }
    output = json.dumps(dezrann)
    print(output)