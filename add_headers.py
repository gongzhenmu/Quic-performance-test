#!/usr/bin/env python3

# MODIFIED FROM: https://gist.github.com/twdkeule/44e8ff271d34b6e580141013cde05868

import os
from sys import argv

'''
	Adds a minimal HTTP header to files and directories and places them in 'with_headers/'.
	Accepts files and directories as CL arguments. The directories will be traversed and all files will be processed.
	Specifically designed for https://github.com/google/proto-quic/.
'''

#
BASE_URL = 'www.example.org'
DATE = 'Mon, 22 May 2017 09:23:05 GMT'
LAST_MODIFIED = 'Tue, 25 Apr 2017 15:02:35 GMT'

def add_http_header(filename, new_filename, relative_filename):
	# print('file', filename, '; new_file', new_filename, '; relative', relative_filename)
	extension = os.path.splitext(filename)[1].strip('.')
	with open(filename, mode='rb') as fr:
		file_size = os.stat(fr.fileno())[6]
		contents = fr.read()
	header = construct_http_header(file_size, extension, relative_filename)
	print(header)
	os.makedirs(os.path.dirname(new_filename), exist_ok=True)
	with open(new_filename, mode='wb') as fw:
		fw.write(header.encode('utf-8') + contents)

def construct_http_header(file_size, content_type, relative_filename):
	header = 'HTTP/1.1 200 OK\r\nDate: ' + DATE + '\r\nContent-Type: '
	if content_type == 'html':
		header += 'text/html'
	elif content_type == 'mp4':
		header += 'video/mp4'
		header += "Age: 263314"
		header += "Cache-Control: max-age=604800"
		header += "Etag: \"3147526947+ident\""
		header += "Expires: Mon, 12 Dec 2022 04:38:38 GMT"
		header += "Server: ECS (chb/0286)"
		header += "Vary: Accept-Encoding"
		header += "X-Cache: HIT"

	header += '\r\nContent-Length: ' + str(file_size) + '\r\n'
	header += 'Last-Modified: ' + LAST_MODIFIED + '\r\n'
	header += 'X-Original-Url: https://' + BASE_URL + relative_filename + '\r\n\r\n'
	header +=
	return header

def add_header_for_files_in_dir(directory, result_dir):
	print('Processing directory:', directory)
	join = os.path.join
	orig_dir = os.path.abspath('.')
	base = os.path.basename(directory)
	os.chdir(directory)
	for dirpath, _, filenames in os.walk('.'):
		for name in filenames:
			relative_filename = base + (join(dirpath, name)).strip('.')
			add_http_header(join(dirpath, name), join(result_dir, relative_filename), '/' + relative_filename)
	os.chdir(orig_dir)

if __name__ == '__main__':
	result_dir = 'with_headers'
	os.makedirs(result_dir, exist_ok=True)
	result_dir = os.path.abspath(result_dir)

	for arg in argv[1:]:
		if os.path.isdir(arg):
			add_header_for_files_in_dir(arg, result_dir)
		elif os.path.isfile(arg):
			item_base = '/' + os.path.basename(arg)
			add_http_header(arg, result_dir + item_base, item_base)
		else:
			print('Not a file or directory:', arg)
