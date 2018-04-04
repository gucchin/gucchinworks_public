# coding: utf-8
template={}

template["cls"]="""
class {{class_name}}({{superclass}}):
def __init__(self):
super({{class_name}}, self).__init__()
"""
		
template["ifm"]="""
def main():
pass
		
if __name__ == '__main__':
main()
"""

template["html5"]="""
<!DOCTYPE html5>
<html>
	<head>
	</head>
	<body>
	</body>
</html>
"""

template["snp"]="""
template[\"{{snippet_name}}\"]=\"\"\"
\"\"\"
"""
