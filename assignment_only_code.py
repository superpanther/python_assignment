		# Q1) Write a program which should return the list on a single line containing the cubes of the first
		# 6 Fibonacci numbers. HINT: Use Lambda function.

# cubes=map(lambda num: num**3,[1,1,2,3,5,8])
# print(cubes)

		# Q2) Write a program to take input from the user in following formats and also check their type by
		# using type function.
		# Formats: Integer, Float, String & Complex

# inp=int(raw_input('Enter a number:  '))
# print(type(inp))

# inp1=float(raw_input('Enter a number:  '))
# print(type(inp1))

# inp2=raw_input('Enter a number or a word:  ')
# print(type(inp2))

# inp3=complex(raw_input('Enter any number in the form of 6+7j:  '))
# print(type(inp3))

		# Q3) Write a program for the following conditions:
		# - If a user enters a negative number it should break the loop
		# - If a user enters any positive value it will run the loop for infinite.

# print('Enter a negative number to end the program')
# print
# while True:
	# try:
		# x=int(raw_input('Enter a number  '))
		# if x<0:
			# break
	
	# except:
		# print('Invalid number. Please try again with number')
		# continue

		# Q4) Write a program to multiply the first 10 even integer number starting from 1 & store them in
		# result variable.

# num1=filter(lambda x:x%2==0,range(1,30))

# result=reduce(lambda a,b:a*b,num1[:10])
# print(result)

		# Q5) Write a program to concatenate the string of those characters which exist at the even
		# position in "innovationwithpython".

# word='innovationwithpython'
# word_list=[]
# for item in range(len(word)):
	# if item%2==0:
		# word_list.append(word[item])
# word_str=''.join(word_list)
# print(word_str)

				#OR

# word='innovationwithpython'
# word_str=''
# for item in range(len(word)):
	# if item%2==0:
		# word_str=word_str+word[item]
# print(word_str)

		# Q6) Write a function to return the list of those numbers in a range of 1 to 50 which is a multiple
		# of 2 and 6 both. Also, calculate the sum of last three values.

# def find_num(num):
	# mylist=[]
	# for i in num:
		# if i%2==0 and i%6==0:
			# mylist.append(i)
	# return mylist
	
# result=find_num(range(1,50))
# print(result)

# t=reduce(lambda x,y:x+y,result[-3:])
# print(t)
	
		#OR (without lambda function)

# def sum_1(new_list):
	# add_list=0
	# for i in new_list[-3:]:
		# add_list=add_list + i

	# return(add_list)

# result2=sum_1(result)
# print(result2)

		# Q7) Write the higher order function reduce to calculate the total sum of first 30 odd values in he
		# range of 1 to 100.

# def addition():
	# list_of_num=range(1,100,2)
	# odd_list=[]
	# for item in list_of_num:
		# odd_list.append(item)
		# if len(odd_list)==30:
			# break
	# return odd_list
	
# res=addition()

# total=reduce(lambda x,y:x+y,res)
# print(total)


		# Q8) What will be the output of the following:
		# new_list=[ 1 , 2 , 3 , 4 , 5 , 6 , [ "Riyaz" , "Ul" , "Haque" , 7 ] , 8 , 9 , 10 ]

# --- new_list [ -4 ]=[ 'Riyaz', 'Ul', 'Haque' , 7 ]

# --- new_list [ 4 ]=5

# --- new_list [ 6 ] [ 1 ]='Ul'
# -
# -- new_list . append ( [ "new" ] )=[ 1 , 2 , 3 , 4 , 5 , 6 , [ 'Riyaz' , 'Ul', 'Haque' , 7 ] , 8 , 9 , 10, [ 'new' ]]

# --- new_list . sort( )= [ 1 , 2 , 3 , 4 , 5 , 6 ,8 , 9 , 10, [ 'Riyaz' , 'Ul', 'Haque' , 7 ], [ 'new' ]]
	
		# Q9) Write a function that takes three arguments which after concatenation should print
		# "innovationwithpython" . This is a void type function.

# def conc(a,b,c):
	# print(a+b+c)
	
# res=conc('innovation','with','python')
# print(res)

		# Q11) Write a function that should multiple three entered values. Now use this function in the
		# different module and take three values as 11, 12 & 13. HINT: Use import


	# NOTE: This function is defined in assignment.py		

# def mult1(a,b,c):
	# return a*b*c

	# NOTE: This import is carried out in another file say xyz.py. I will run xyz.py in interpreter to get the result.

# import assignment

# result=assignment.mult1(11,12,13)
# print(result)

		# Q12) write a program to generate a dictionary that contains ( i , i * i ) such that is an integral
		# number between 1 and n (both included). and then the program should print the dictionary.
		# Suppose the following input is supplied to the program:
		# 4
		# Then, the output should be:
		# {1: 1, 2: 4, 3: 9, 4: 16}

# def create_dict(i):
	# new_dict={}
	# for i in range(1,i+1):
		# new_dict[i]=i
		# new_dict[i]=i*i
	# print(new_dict)
	
# res=create_dict(6)
	
	
		# Q14) Write a program which accepts a sequence of comma-separated numbers from the
		# console and generate a list and a tuple which contains every number.
		# Suppose the following input is supplied to the program:
		# 34,67,55,33,12,98
		# Then, the output should be:
		# ['34', '67', '55', '33', '12', '98']
		# ('34', '67', '55', '33', '12', '98')

# def list_tuple():
	# x=raw_input('Enter more than one number and separate them by a comma ')
	# y=x.split(',')
	# z=tuple(y)
	# print(y)
	# print(z)
	

# list_tuple()

		# Q15) Write a program which accepts a string from console and prints it in reverse order.

# my_string=raw_input('Enter a word: ')
# print(my_string[::-1])

		# Q16) Find out the common character from the two different string using set.

# def common(word1,word2):
	# x=set(word1)
	# y=set(word2)
	# return x & y
	
# common_letters=common('ranking','rafting')
# print(common_letters)

		# Q17) Write a program that read the sentence and gives the output as the length of each word in
		# a sentence in the form of a list.

# def length():
	# x=raw_input('Enter a sentence: ')
	# y=x.split()
	# mylist=list()
	# for word in y:
		# mylist.append(len(word))
	# return mylist
	
# len_of_word=length()
# print(len_of_word)


		# Q18) Write a program to concatenate the following dictionaries to create a new one.
		

# def add_dict(dict1,dict2,dict3):
	# x=dict1.items()
	# y=dict2.items()
	# z=dict3.items()
	# mylist=x+y+z
	
	# return dict(mylist)
	
# outcome1=add_dict({1:'a',2:'b'},{3:'c', 4:'d'},{5:'e', 6:'f'})
# print(outcome1)
		


		