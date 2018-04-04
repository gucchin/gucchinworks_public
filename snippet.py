from collections import OrderedDict
import console
import editor
import jinja2

from snippet_template import template

class SnippetNotFoundError(Exception): pass

def pickup_labels(data):
	b=0
	s=0
	labels=OrderedDict()
	while True:
		s = data[b:].find('{{')
		if s >= 0:
			e = data[b+s:].find('}}')
			label=data[b+s+2:b+s+e]
			labels[label]=label
			b+=s+e
			continue
		break
		
	return labels

text = editor.get_text()
select = editor.get_line_selection()
key = text[select[0]:select[1]]

try:
	temp = template[key]
	labels = pickup_labels(temp)
except:
	raise SnippetNotFoundError
	

for k in labels:
	labels[k] = console.input_alert(labels[k])

t = jinja2.Template(temp)

editor.replace_text(select[0], select[1], t.render(labels))

	
