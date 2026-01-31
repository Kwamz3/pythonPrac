# # these are truthy and falsy values of a simple conditional
# x = 0
# y = 5

# if x < y:                            # Truthy
#     print('yes')

# if y < x:                            # Falsy
#     print('yes')

# if x:                                # Falsy
#     print('yes')

# if y:                                # Truthy
#     print('yes')

# if x or y:                           # Truthy
#     print('yes')

# if x and y:                          # Falsy
#     print('yes')

# if 'aul' in 'grault':                # Truthy
#     print('yes')

# if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
#     print('yes')


# # the block of code to be excuted is often called suite
# if 'bar' in ['bar', 'baz', 'qux']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
# print('After conditional')


# # a much more complicated script to prove the importance of indentation in conditionals
# # Does line execute?                        Yes    No
# #                                           ---    --
# if 'foo' in ['foo', 'bar', 'baz']:        #  x
#     print('Outer condition is true')      #  x

#     if 10 > 20:                           #  x
#         print('Inner condition 1')        #        x

#     print('Between inner conditions')     #  x

#     if 10 < 20:                           #  x
#         print('Inner condition 2')        #  x

#     print('End of outer condition')       #  x
# print('After outer condition')            #  x


# # adding the else keyword to determine an alternative path
# x = 20

# if x < 50:
#     print('(first suite)')
#     print('x is small')
# else:
#     print('(second suite)')
#     print('x is large')
    

# # the use of elif keyword to add more alternatives to the conditional
# name = 'Joe'
# if name == 'Fred':
#     print('Hello Fred')
# elif name == 'Xander':
#     print('Hello Xander')
# elif name == 'Joe':
#     print('Hello Joe')
# elif name == 'Arnold':
#     print('Hello Arnold')
# else:
#     print("I don't know who you are!")


# # We can use the dict.get() method to search for a word and pass a default value if it isn't found
# names = {
#     'Fred': 'Hello Fred',
#     'Xander': 'Hello Xander',
#     'Joe': 'Hello Joe',
#     'Arnold': 'Hello Arnold'
# }

# print(names.get('Joe', "I don't know who you are!"))
# print(names.get('Rick', "I don't know who you are!"))


# # you can write all the expressions of a condtional on the same line seperated by semi-colons
# if 'f' in 'foo': print('1'); print('2'); print('3')


# 