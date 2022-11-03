import random
import re
import textwrap
import string

def findFunctionNames(file):
	function_names = []
	for _, line in enumerate(open(file)):
		for name in re.findall(r"(?<=def )\w+(?=\()", line):
			function_names.append(name)
	return function_names

def findVariableNames(file):
	variable_names = []
	for _, line in enumerate(open(file)):
		regex = r"(?!\S*_+ )((\w+)(?=( ||\t)=( |)))|((?<=\()\w+(?=\)))|((?<=\()\w+(?=,))|((?<=, )\w+(?=,))|((?<=, )\w+(?=\)))|(\w+(?=, ))"
		for name in re.findall(regex, line):
			variable_names.append(list(filter((lambda x: x!='' and x!=' '), name))[0])
	return list(set(variable_names))

def RandomString():
	letter = string.ascii_letters
	result_str = ''
	for i in range(random.randint(7,12)):
		result_str += random.choice(letter)
	return result_str


def findStrings(file):
	triple_quoted = []
	for line in enumerate(open(file)):
		for name in re.findall(r"(?<=\").*(?=\")", line,flags=re.MULTILINE):
			triple_quoted.append(name)
	return triple_quoted


def createMap(vars):
	name_map = { i : RandomString() for i in vars }
	return name_map

def FindComments(file):
	comments = []
	for line in enumerate(open(file)):
		for name in re.findall(r"(?<=# ).*", line):
			comments.append(name)
	return comments

def Replace(name_map, filedata):

	for key, value in name_map.items():
		filedata = re.sub(r"(?<=[^.])(\b{}\b)".format(key), value, filedata)
	return filedata

def main():
	with open("main.py", "r",encoding='utf-8') as f:
		filedata = f.read()
	function_names = findFunctionNames("main.py")
	variable_names = findVariableNames("main.py")
	variable_names = list(set(variable_names) - set(function_names)) #prints comment  vars + other vars
	replaced_vars= createMap(variable_names)
	print("replaced vars : ",replaced_vars)
	comments = FindComments("main.py")
	print("comments are :" ,comments)
	replaced_comments = createMap(comments)
	print("replaced comments",replaced_comments)
	filedata = Replace(replaced_vars, filedata)
	filedata = Replace(replaced_comments, filedata)
	print(function_names)
	strings_names = findStrings("main.py")
	print(strings_names)
	with open("obfuscated-result.py", "w") as f:
		f.write(filedata)




if __name__ == "__main__":
	main()
