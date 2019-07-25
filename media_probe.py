#!/bin/env python3
"""
Copyright 2018-2019 Trustees of Indiana University

This code is licensed under the APACHE 2.0 License

Original code by Brian Wheeler (bdwheele@indiana.edu)

-------

This will process a file and create either a data structure (if called as a library) or 
a JSON/YAML blob (when called from the command line) of information about a given file.

This effectively combines ffprobe, imagemagic identify, file, and pdfinfo.  Other formats
can easily be added.   If the external tools are not available, only basic information will
be created.

"""

import argparse
import json
import yaml
from media_probe import MediaProbe
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probe a media file for metadata")
    parser.add_argument("--config", type=str, nargs=1, default=[None],
                        help="Specify a YAML config file with tool paths")
    parser.add_argument('--json', action='store_true', default=False,
                        help="Dump JSON instead of YAML")    
    parser.add_argument('mediafile', type=str, metavar="<mediafile>",
                        help="File to probe")
    args = parser.parse_args()
    paths = None
    if args.config[0]:
        # load configuration file
        pass
    
    mp = MediaProbe(paths)
    data = mp.probe(args.mediafile)

    if args.json:
        print(json.dumps(data, sort_keys=True, indent=4))
    else:
        yaml.safe_dump(data, stream=sys.stdout)
    

                