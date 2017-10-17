import re

def is_isogram(string):
	string = re.compile('[^a-zA-Z]').sub('', string.lower())
	
	for char in string:
		if string.count(char.lower()) > 1:
			return False
	return True
