# # the position of a character is determined by the number referenced in the array
# a = "Hello, World!"
# print(a[1])


# # looping through the characters of a string with a for loop
# for x in "banana":
#   print(x)
  

# # for displaying the length of a string  
# a = "Hello, World!"
# print(len(a))


# # to check if a certain word is in a particular string
# txt = "The best things in life are free!"
# print("free" in txt)

# # adding the if statement to the string checker
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# # the use of the checking in vice versa
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# # the use of the checking in vice versa with the if statement
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


# # to get the characters from position 2 to 5(not included)
# b = "Hello, World!"
# print(b[2:5])


# # start slicing from the start till the position 5(not included)
# b = "Hello, World!"
# print(b[:5])


# # start slicing from position 2 till the end
# b = "Hello, World!"
# print(b[2:])

# # start slicing from the end of the string with the negative sign
# # same exclusion applies with the negative sign 
# b = "Hello, World!"
# print(b[-5:-2])


# # returns the string in upper case
# a = "Hello, World!"
# print(a.upper())


# returns the string in lower case
# a = "Hello, World!"
# print(a.lower())


# # remove whitespaces from the string
# a = " Hello, World! "
# print(a.strip())


# # replace the first string with the string that follows
# # looks for what to replace before it can replace 
# a = "Hello, World!"
# print(a.replace("H", "J"))


# # slpit the word where the specified character is positioned at
# # it's also case sensitive
# a = "Hello, World!"
# print(a.split("W"))


# # merging string a and string b into string c
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# # merging to add whitespace
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# combining string and integers with the use of the format method
age = 36
txt = f"My name is John, I am {age}"
print(txt)