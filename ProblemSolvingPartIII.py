# Problem 1: Integers
# 1. Get the input which includes numbers in an list and a target sum
# 2. For each number in the list, add it to the other numbers in the list
# 3. During for loop, compare sum to target number, if sum is equal to target number, assign number to variable
# 4. Search list for variables, and return index numbers


# def integer_indices():
#     correct_nums = []
#     array = []
#     counter = 0
#     while counter != 4:
#         list_input = int(input("Please enter the number you wish to add to the array"))
#         array.append(list_input)
#         counter += 1
#     target = int(input("what is the target number?"))
#     for number in array:
#         for add_num in array:
#             if number + add_num == target:
#                 correct_nums.append(number)
#     num_one_ind = array.index(correct_nums[0])
#     num_two_ind = array.index(correct_nums[1])
#     print(num_one_ind, num_two_ind)

# integer_indices()

#Problem 3: list of integers
# 1. Identify the largest number in a list
# 2. Identify the smallest number in a list
# 3. Subtract the largest number from the smallest number
# 4. divide that number by the number of items in the list-1
# 5. look for result of step 4 plus smallest number in the list
# 6. repeat until find a mismatch, or matches biggest number

# def increment_of_list():
#     input_list = []
#     add_num = input("Please enter the number you want to add to the list")
#     while add_num != "next":
#         input_list.append(int(add_num))
#         add_num = input("Please enter the number you want to add to the list or 'next'")
#     big_num = max(input_list)
#     smol_num = min(input_list)
#     diff_of_big_smol = big_num - smol_num
#     diff_of_nums = diff_of_big_smol / (len(input_list)-1)
#     look_num = smol_num
#     is_false = 0
#     while look_num != big_num and is_false != 1:
#         if look_num in input_list:
#             look_num += diff_of_nums
#         else:
#             is_false = 1
#     if look_num == big_num:
#         print("true")
#     else:
#         print("false")

# increment_of_list()



# Problem 4: Positive and Negative number sums

# Get the User's Input for the arrays individually 
# Use for loop and if statement to append numbers that are below zero into their own list
# Use for loop and if statement to append numbers that are above zero into their own list
# Add all of the numbers and use the range function to identify the index of every number in a list for each list
# print those two sums

# def pos_neg_lists(input_list):
#     neg_list = []
#     pos_list = []
#     pos_sum = 0
#     neg_sum = 0
#     sum_list = []
#     for number in input_list:
#         if number > 0:
#             pos_list.append(number)
#         if number < 0:
#             neg_list.append(number)
#     for number in pos_list:
#         pos_sum += number
#     for number in neg_list:
#         neg_sum += number
#     sum_list.append(pos_sum)
#     sum_list.append(neg_sum)
#     print(f'Your positive and negative total is {sum_list}')

# pos_neg_lists([7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21])



# Problem 5 Highest and Lowest number in a string
# accept the string of values
# use a for loop to assign those values to a list
# use a for loop to find the highest value in the list (Gonna do it without max or min)
# use a for loop to find the lowest value in the list
# use string interpolation to print those values as a string with a space

# def high_and_low():
#     input_list = []
#     add_num = ""
#     big_num = 0
#     smol_num = 0
#     sum_list = []
#     user_input = input("Please enter your string of space separated numbers")
#     for number in user_input:
#         if number != " ":
#             add_num += number
#         else:
#             input_list.append(int(add_num))
#             add_num = ""
#     for num_check in input_list:
#         if num_check > big_num:
#             big_num = num_check
#         if num_check < smol_num:
#             smol_num = num_check
#     sum_list.append(big_num)
#     sum_list.append(smol_num)
#     print(f'Big and Smol numbers are {sum_list}.')

# high_and_low()



# Problem 6 Email Address Analyzer
# Accept the email address from the user
# Look for the @ symbol
# Look for the .com at the end
# Print true or false

# def email_check():
#     email = input("Please enter your email address")
#     at_check = 0
#     dotcom_check = 0
#     for symbol in email:
#         if symbol == "@" and email.index(symbol) != 0:
#             at_check = 1
#     if email[-1] == "m" and email[-2] == "o" and email[-3] == "c" and email[-4] == ".":
#         dotcom_check = 1
#     if at_check == 1 and dotcom_check == 1:
#         print("true")
#     else:
#         print("false")

# email_check()



# problem 7 alphabet position
# accept the string input
# establish alphabet list
# for each letter in input, find the index in the alphabet list
# if letter is not first in input, no space before letter
# add the space and index to a string variable
# print string variable

# def alphabet_position():
#     alphabet_list = "abcdefghijklmnopqrstuvwxyz"
#     answer = ""
#     user_input = input("Please enter a string")
#     for letter in user_input:
#         if answer != "":
#             answer += " "
#         alpha_pos = alphabet_list.index(letter)
#         answer += str(alpha_pos+1)
#     print(answer)

# alphabet_position()



# Problem 8 Briefcase Lock
# accept input for current lock
# accept input for target lock
# compare first indexes of both inputs to see which is highest
# subtract highest from the lowest
# add the result to answer
# repeat for each index
# print answer

# def lock_calc():
#     turns = 0
#     user_input = input("Please enter current lock")
#     tar_input = input("Please enter desired lock")
#     for number in user_input:
#         num_int = int(number)
#         counter = 0
#         tar_int = int(tar_input[counter])
#         if num_int > tar_int:
#             turns += (num_int - tar_int)
#         elif num_int < tar_int:
#             turns += (tar_int - num_int)
#         counter += 1
#     print(turns)

# lock_calc()

# Problem 10 Reciprocal Reverse
# accept number input
# reverse input using negative indexing
# Divide 1 by reverse of input

# def reciprocal_reverse():
#     user_input = input("Please enter a number for me to flip and reverse")
#     rev_str = ""
#     for num in user_input:
#         neg_num = (-((user_input.index(num))+1))
#         rev_str += user_input[neg_num]
#     answer = 1 / int(rev_str)
#     print(answer)

# reciprocal_reverse()