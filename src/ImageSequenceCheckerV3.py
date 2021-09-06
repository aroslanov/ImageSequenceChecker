#!/usr/bin/env python
""" This program checks for the missing/broken/suspicious images in
rendered sequence. Here is the list of supported image formats:
<https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html>
Suspicious files calculated by comparing current file size with the
previous one in the sequence and marked as 'Check'. File size anomaly
threshold can be adjusted by editing value in anomaly variable. Default is 2Kb
This program was written snd tested under Python 3 environment. Also, it may
require PIL module, so please install it with 'pip install PIL' command in
your terminal window if you're getting a missing module error.
How to use: Pick any file in the sequence you want to check.
Note: it's not necessary to pick a very first file, the program will find
one automatically. Also, the program will offer to save a report file after
checking is finished if any errors were found. 

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Timur Aroslanov"
__contact__ = "aroslanov@gmail.com"
__copyright__ = "Copyright 2021, Timur Aroslanov"
__date__ = "2021/09/05"
__deprecated__ = False
__email__ = "aroslanov@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.3"

anomaly = 1000000  # This is file size (in bytes) anomaly threshold, change it to whatever you want

import sys
import re
import glob
import tkinter as tk
import os
import PIL

from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.iconify()

picked_file_name = filedialog.askopenfilename(
    title='Select any file in a sequence')
if picked_file_name == '':
    print('No file chosen, exiting')
    sys.exit()

print('Now checking. Please wait...')

path = os.path.dirname(picked_file_name)
extension = os.path.splitext(picked_file_name)[1]

list_of_files = glob.glob(path + '/*' + extension)
first_file = min(list_of_files)
last_file = max(list_of_files)

regex = re.compile(r'\d{3,6}\.')

first_file_number_str = regex.search(first_file).group(0)
first_file_number_str = first_file_number_str.rstrip(first_file_number_str[-1])
first_file_number_int = int(first_file_number_str)

last_file_number_str = regex.search(last_file).group(0)
last_file_number_str = last_file_number_str.rstrip(last_file_number_str[-1])
last_file_number_int = int(last_file_number_str)

padding = len(first_file_number_str)

base_file_name = first_file.replace(first_file_number_str, '')
base_file_name = os.path.splitext(base_file_name)[0]

file_size = os.path.getsize(first_file)

err_list = []

for filenum in range(first_file_number_int, last_file_number_int):
    num = str(filenum).rjust(padding, '0')
    file_name_generated = base_file_name + num + extension
    if not os.path.isfile(file_name_generated):
        msg = 'Missing: ' + os.path.basename(file_name_generated)
        err_list.append(msg)
        print(msg)
    elif abs(file_size - os.path.getsize(file_name_generated)) > anomaly:
        msg = 'Check:   ' + os.path.basename(file_name_generated)
        err_list.append(msg)
        print(msg)
    else:
        try:
            im = Image.open(file_name_generated)
            im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            im.close()
        except (IOError, SyntaxError) as e:
            msg = 'Broken:  ' + os.path.basename(file_name_generated)
            err_list.append(msg)
            print(msg)

if len(err_list) == 0:
    print('No errors found')
else:
    from tkinter.messagebox import askyesno
    if askyesno(title='confirmation', message='Do you want to save a report?'):
        from tkinter.filedialog import asksaveasfilename
        report_file_name = asksaveasfilename(defaultextension='.txt', filetypes=[(
            "Text files", '*.txt')], initialdir=path, initialfile=base_file_name + '_report.txt', title="Choose report output file name")
        if report_file_name != '':
            with open(report_file_name, 'w') as f:
                for item in err_list:
                    f.write("%s\n" % item)
            f.close

root.destroy

print('Press Enter to close ...')
input()
