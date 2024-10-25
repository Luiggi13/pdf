#!/usr/bin/env python3
"""
Simple python wrapper script to use ghoscript function to compress PDF files.

Dependency: Ghostscript.
On MacOSX install via command line `brew install ghostscript`.
"""

import os.path
import shutil
import subprocess
import sys
import time

def compressPDFFile(input_file_path):
    """Function to compress PDF via Ghostscript command line interface"""
    destinationFolderFile = "./descargas"
    original_name = input_file_path
    fileNameToReduce =  "./inputs/" + input_file_path + ".pdf"
    exportName = setFinalName(original_name)
    # Basic controls
    if not os.path.exists(destinationFolderFile):
        os.makedirs(destinationFolderFile)
    # Check if valid path
    if not os.path.isfile(fileNameToReduce):
        print("Error: invalid path for input PDF file.", fileNameToReduce)
        sys.exit(1)

    # Check if file is a PDF by extension
    if fileNameToReduce.split('.')[-1].lower() != 'pdf':
        print(f"Error: input file is not a PDF.", fileNameToReduce)
        sys.exit(1)

    gs = get_ghostscript_path()
    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format("/screen"),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(exportName),
            fileNameToReduce,
        ]
    )

    shutil.move(exportName, destinationFolderFile)
    return exportName


def get_ghostscript_path():
    gs_names = ["gs", "gswin32", "gswin64"]
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(
        f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
    )

def setFinalName(original_name):
    timestamp = int(round(time.time() * 1000))
    filename = original_name + "_" + str(timestamp) + ".pdf"
    return filename

def compress(input: str):
    return compressPDFFile(input)
