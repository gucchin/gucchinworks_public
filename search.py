# -*- coding: utf-8 -*-
import console
import editor
import ui


key = console.input_alert('find strings')

text = editor.get_text()
i=0
s=0
while True:
	i = text[s:].find(key)
	l = len(key)
	if i >= 0:
		editor.set_selection(s+i, s+i+l)
		i+=l
		s+=i
		try:
			console.alert('find next','find next','next')
		except KeyboardInterrupt:
			break
	else:
		console.hud_alert('not found.')
		break
	
