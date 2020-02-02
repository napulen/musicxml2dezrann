# musicxml2dezrann
A tool for generating dezrann `json` files from lyric annotations in a `musicxml` file

## Usage

1. Make your dezrann annotations within MuseScore. Make sure that those annotations are done in a `lyric` text over a note.
2. Export the uncompressed `.musicxml` file in MuseScore.
3. Run `musicxml2dezrann`

```
python musicxml2dezrann.py <input_musicxml_file> <annotation_type>
```
4. The dezrann `json` file will be generated with the same name and extension `.dez`
5. Load your `.dez` file in dezrann

## Release notes, v0.2.0
- Extensions `.musicxml` `.xml`, and `.mxl` are now supported

## Release notes, v0.1.0

- Turns any encoded lyrics in the musicxml file into a **durationless** dezrann annotation
- Only supports `.musicxml` file extensions
- Validates the annotation type according to the types supported by dezrann
  - Comment
  - Harmony
  - Tonality
  - ... and so on...
  
  
