# Image Sequence Checker
 This program checks for the missing/broken/suspicious images in rendered sequence. Here is the list of supported image formats:
<https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html>

Suspicious files calculated by comparing current file size with the previous one in the sequence and marked as *Check*. File size anomaly threshold can be adjusted by editing value in anomaly variable. Default is 1Mb

This program written and tested under Python 3 Windows 10 environment> but should work on any desktop platform supported by Python 3. It requires PIL module, so please install it with `pip install Pillow` command in your terminal window if you're getting a missing module error.

How to use: Pick any file in the sequence you want to check. Inage Sequence Checker will offer to save a report file after checking is finished if any errors were found. 
_Note: it's not necessary to pick a very first file, program will find one automatically.
