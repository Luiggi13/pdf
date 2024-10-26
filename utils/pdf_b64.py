from base64 import b64decode
import base64

from utils.utils import compressPDFFile
# import os
# pdf_file_path = './inputs/20m.pdf'

def toFile(b64: str):

    # Decode the Base64 string, making sure that it contains only valid characters
    bytes = b64decode(b64, validate=True)

    # Perform a basic validation to make sure that the result is a valid PDF file
    # Be aware! The magic number (file signature) is not 100% reliable solution to validate PDF files
    # Moreover, if you get Base64 from an untrusted source, you must sanitize the PDF contents
    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')

    # Write the PDF contents to a local file
    f = open('inputs/file.pdf', 'wb')
    f.write(bytes)
    f.close()
    comp = compressPDFFile("file")
    return comp