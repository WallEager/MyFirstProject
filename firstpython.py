Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> movies=["krrish","dil se","dhoom"]
>>> movies[0]
'krrish'
>>> print(movies)
['krrish', 'dil se', 'dhoom']
>>> print(len(movies))
3
>>> movies.append("josh")
>>> print(movies)
['krrish', 'dil se', 'dhoom', 'josh']
>>> movies.pop()
'josh'
>>> movies.extend(['300','insidious','victory'])
>>> print(movies)
['krrish', 'dil se', 'dhoom', '300', 'insidious', 'victory']
>>> movies.append('josh')
>>> print(movies)
['krrish', 'dil se', 'dhoom', '300', 'insidious', 'victory', 'josh']
>>> movies.remove('insidious')
>>> movies.insert(0,'ghajini')
>>> print(movies)
['ghajini', 'krrish', 'dil se', 'dhoom', '300', 'victory', 'josh']
>>> movies.insert(0,1)
>>> movies.insert(0,2)
>>> print(movies)
[2, 1, 'ghajini', 'krrish', 'dil se', 'dhoom', '300', 'victory', 'josh']
>>> movies.remove(2)
>>> movies.remove()1
SyntaxError: invalid syntax
>>> movies.remove(1)
>>> print(movies)
['ghajini', 'krrish', 'dil se', 'dhoom', '300', 'victory', 'josh']
>>> for val in movies:
	print(val)

	
ghajini
krrish
dil se
dhoom
300
victory
josh
>>> count=0
>>> while count<len(movies):
	print(movies[count])
	count=count+1

	
ghajini
krrish
dil se
dhoom
300
victory
josh
>>> for i in movies:
	print(i)

	
ghajini
krrish
dil se
dhoom
300
victory
josh
>>> movies=['the holy grail',1975,'terry jones and terry gilliam',91,['graham chapman',['michael pailn','john cleese','terry gilliam','eric idle','terry jones']]]
>>> print(movies)
['the holy grail', 1975, 'terry jones and terry gilliam', 91, ['graham chapman', ['michael pailn', 'john cleese', 'terry gilliam', 'eric idle', 'terry jones']]]
>>> print(movies[4][1][3])
eric idle
>>> for i in movies:
	print(i)

	
the holy grail
1975
terry jones and terry gilliam
91
['graham chapman', ['michael pailn', 'john cleese', 'terry gilliam', 'eric idle', 'terry jones']]
>>> names=['michael','curry']
>>> print(names)
['michael', 'curry']
>>> isinstance(names,list)
True
>>> isinstance(movies,list)
True
>>> isinstance(name,list)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    isinstance(name,list)
NameError: name 'name' is not defined
>>> for i in movies:
	if isinstance(i,list):
		for j in i:
			print(j)
			else
			
SyntaxError: invalid syntax
>>> for i in movies:
	if isinstance(i,list):
		for j in i:
			print(j)
	else:
		print(i)

		
the holy grail
1975
terry jones and terry gilliam
91
graham chapman
['michael pailn', 'john cleese', 'terry gilliam', 'eric idle', 'terry jones']
>>> for i in movies:
	if isinstance(i,list):
		for j in i:
			if isinstance(j,list):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)

		
the holy grail
1975
terry jones and terry gilliam
91
graham chapman
michael pailn
john cleese
terry gilliam
eric idle
terry jones
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(input)
Help on built-in function input in module builtins:

input(...)
    input([prompt]) -> string
    
    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.

>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> clear
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clr
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> cls
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> isinstance(movies[0],string)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    isinstance(movies[0],string)
NameError: name 'string' is not defined
>>> isinstance(movies[0],str)
True
>>> def print_lol(the_list):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i)
		else:
			print i
			
SyntaxError: invalid syntax
>>> def print_lol(the_list):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i)
		else:
			print(i)

			
>>> print_lol(movies)
the holy grail
1975
terry jones and terry gilliam
91
graham chapman
michael pailn
john cleese
terry gilliam
eric idle
terry jones
'
>>> print_lol(movies)
the holy grail
1975
terry jones and terry gilliam
91
graham chapman
michael pailn
john cleese
terry gilliam
eric idle
terry jones
>>> 
