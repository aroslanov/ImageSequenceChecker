# Image Sequence Checker
 This program checks for the missing/broken/suspicious images in rendered sequence. It supports major graphic file formats (supported by PIL library)

Suspicious files calculated by comparing current file size with the previous one in the sequence. File size anomaly threshold is the difference between next and previous file in sequence.

This program written and tested in Python 3 under Windows 10 environment, but should work on any other desktop platforms supported by Python 3 (like macOS or Linux). Requirements are in requirements.txt file. (run `pip install -r requirements.txt` before running, if you use python source) Also, windows binary is [available in the releases section](https://github.com/aroslanov/ImageSequenceChecker/releases). 

**How to use:** Pick any file in the sequence you want to check. Image Sequence Checker will offer to save a report file after check is finished if any errors found. 
_Note: it's not necessary to pick a very first file, the program will find one automatically._
