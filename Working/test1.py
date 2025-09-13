# Tuples in python
t1 = (1, 2, 3)
# print("The values of the tuple are: ", t1)
# print("The value of the tuple at index 1 is ", t1[1])

list1 = [12, [234], "string"]
# print("The values of the tuple are: ", list1)
# print("The value of the tuple at index 1 is ", list1[2])

# Sets in python
set1 = {1, 2, 354, 675, 276, 5678}
print("The values of the set is: ", set1)
# print("The value of the tuple at index 1 is ", set1[4])

# Functions
# def check_num(num):
#     try:
#         age = int(num)
#         if age < 18:
#             print("You can't drink ma guy")
#         else:
#             print("You can drink!")
#     except ValueError:
#         print("Please enter a valid number, not a word.")
            
            
def check_sum(num):
    
    try:
        age = int(num)
        if age < 18:
            print("You can't drink fam")
        else:
            print("You good marhn")
    except ValueError:
        print("Enter a valid number not a word")    