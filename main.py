from sys import platform
if platform == "linux" or platform == "linux2":
    import getch
elif platform == "win32" or platform == "win64":
    import msvcrt
else:
	print("Sorry, only Windows and Linux system available.")
	exit()

avail_char = ['<','>','+','-',',','.','[',']',' ']
fp = open("code.txt", "r")
code = []
line = fp.readline()

while line:
	#delete command and space
	line = "".join(line.split()) 
	code.append(line.split('//')[0]);
	line = fp.readline()

# check code
for i in range(len(code)):
	for j in range(len(code[i])):
		if code[i][j] not in avail_char:
			print("Error!! unknown char at line %d, col %d : %s" % (i+1, j+1, code[i][j]))
			exit()
	
# Close opend file
fp.close()
memory = {}
index = 0
memory[index] = chr(0)

loop_stack = []
pass_flag = 0

i = 0
j = 0

while i < len(code):
	j = 0
	while j < len(code[i]):
		
		comm = code[i][j]
		
		if pass_flag == 0:
			#(,) = {*ptr = getchar()};
			if comm == ",":
				if platform == "linux" or platform == "linux2":
					memory[index] = getch.getch().decode('ascii')
				else:
					memory[index] = msvcrt.getch().decode('ascii')
				print(memory[index])
				
			#(.) = {putchar(*ptr)};
			elif comm == ".":
				print(memory[index])
				
			#(+) = {++*ptr};
			elif comm == "+":
				memory[index] = chr(ord(memory[index]) + 1)
				
			#(-) = {--*ptr};
			elif comm == "-":
				if(memory[index] == 0):
					print("Error!! memory value is less then 0 at line %d, col %d"% (i+1, j+1))
					exit()
				memory[index] = chr(ord(memory[index]) - 1)
				
			#(<) = {++ptr};
			elif comm == ">":
				index += 1
				if index not in memory:
					memory[index] = chr(0)
				
			#(<) = {--ptr};
			elif comm == "<":
				if index == 0:
					print("Error!! memory location is less then 0 at line %d, col %d"% (i+1, j+1))
					exit()
				index -= 1
			
		#([) = {while (*ptr) '{'};
		if comm == "[":
			if ord(memory[index]) == 0:
				pass_flag = 1
			else:
				loop_stack.append([i,j])
		#(]) = {'}'};
		elif comm == "]":
			if pass_flag == 1:
				pass_flag = 0
			else:
				if ord(memory[index]) != 0:
					i = loop_stack[-1][0]
					j = loop_stack[-1][1]
				else:
					loop_stack.pop()
		j += 1
	i += 1
			
