# Multi line continuation is allowed with the use of backward slash
item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three
        
print(total)
        

# the use of single, double and triple quotes denote string literals
word = 'word' #single
print (word)

sentence = "This is a sentence." #double
print (sentence)

paragraph = """This is a paragraph. It is   
 made up of multiple lines and sentences.""" #triple
print (paragraph)


# the use of comments
name = "Madisetti" # This is again comment


# you can write multiple statements on one line as long as you use the seme-colon and it doesn't
# start another code block of code
import sys; x = 'foo'; sys.stdout.write(x + '\n')
name = 'Vane'; print(name) 


# suites are a group of individual statements that make up a codeblock. Starting with a keyword
# and ending with a colon followed by the rest of the code
expression = 1
suite_1 = 'good'
suite_2 = 'good'

if expression == 1:
   print(suite_1)
elif expression :
   print(suite_1)
else :
   print(suite_2)
