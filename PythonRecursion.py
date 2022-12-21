import sys
import string

def Count_Letter(data):
	if not data:
		return 0
	else:
		return 1 + Count_Letter(data[1:])
		
def Reverse_Letter(data):
	if(len(data) == 0):
		return data
	else:
		return Reverse_Letter(data[1:]) + data[0]
	
def isPalindrome(data):
	return len(data) < 2 or data[0] == data[-1] and isPalindrome(data[1:-1])

def isPal(data):
	if len(data) < 1:
		return True;
	else:
		if data[0].isalpha() == True and data[-1].isalpha() == True:
			if data[0].lower() == data[-1].lower():
				return isPal(data[1:-1])
			else:
				return False;
		elif data[0].isalpha() == False:
			return isPal(data[1:])
		else:
			return isPal(data[:-1])	
	
data = input('Enter a string: ')
n = Count_Letter(data)
l = isPal(data)
m = Reverse_Letter(data)

print(str(n))
print(str(m))
print(str(l))
	
