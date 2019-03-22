# MediaProbe
This will process a file and create either a data structure (if called as a library) or 
a JSON blob (when called from the command line) of information about a given file.

This effectively combines ffprobe, imagemagic identify, file, and pdfinfo.  Other formats
can easily be added.   If the external tools are not available, only basic information will
be created.

It isn't finished, but it's a good start.

````
usage: media_probe.py [-h] [--ffprobe-bin FFPROBE_BIN]
                      [--identify-bin IDENTIFY_BIN] [--file-bin FILE_BIN]
                      [--pdfinfo-bin PDFINFO_BIN]
                      <mediafile>

Probe a media file for metadata

positional arguments:
  <mediafile>           File to probe

optional arguments:
  -h, --help            show this help message and exit
  --ffprobe-bin FFPROBE_BIN
                        Location of ffprobe binary (/usr/bin/ffprobe)
  --identify-bin IDENTIFY_BIN
                        Location of identify binary (/usr/bin/identify)
  --file-bin FILE_BIN   Location of file binary (/usr/bin/file)
  --pdfinfo-bin PDFINFO_BIN
                        Location of pdfinfo binary (/usr/bin/pdfinfo)

````


