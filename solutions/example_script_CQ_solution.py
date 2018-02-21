#!/usr/bin/env python3
#the shebang line launches an interpreter with which to run the file contents as a script
#executing python3 script.py on command line does the equivalent

#new function that checks if input is a list and prints a warning if it is not
def print_warning(argument1):
	if type(argument1)!=list:
		print("This is not a list")
	return 0

#python has built in functions like print() but you can define your own function
#functions take input as arguments and return output
#the syntax includes a colon and indentation in following lines
#the key word def tells python what follows is a user defined function
def my_function(argument1,argument2):
	argument1+=1
	print_warning(argument2) #call new function
	argument2.append("!")
	return (argument1,argument2)

#order matters! define functions in the script before the main function
#main function
def main():
	variable1 = 2
	variable2 = ["i","love","girls","who","code"]
  	save_output = my_function(variable1,variable2)
  	print(" ".join(save_output[1]))

#call main
if __name__ == "__main__":
  main()


#challengeQuestions
#1. What data type is variable1? 
#integer

#2. What data type is variable2? 
#list

#3. What data type are elements in variable 2?
#strings

#4. What will print to the command line at the end of this script?
#"i love girls who code!"

#5. Write a function called print_warning
#The function should print a warning to the terminal saying "This is not a list"
#It should only print the warning if argument 2 is not a list
#It should be called within my_function
#Hint: This function takes argument2 as input, but has no output
#See above

#6. What does line 21 do?
#save_output[1] indexes into a tuple to select the list 
#" ".join joins the strings in that list with spaces to print what will look like a sentence

#7. What will save_output[0] be equal to?
#3
