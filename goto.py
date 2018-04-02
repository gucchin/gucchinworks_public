# -*- coding: utf-8 -*-
import console
import editor
import io
import sys

try:
	line_num = int(console.input_alert('input line number'))
except ValueError:
	sys.exit(1)
if not isinstance(line_num, int):
	sys.exit(1)
  
text = editor.get_text()
idx = 0
with io.StringIO(text) as f:
	for i in range(line_num):
		line=f.readline()
		idx+=len(line)
		
editor.set_selection(idx)
