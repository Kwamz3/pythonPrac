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



# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x