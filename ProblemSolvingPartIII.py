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

def increment_of_list():
    input_list = []
    add_num = input("Please enter the number you want to add to the list")
    while add_num != "next":
        input_list.append(int(add_num))
        add_num = input("Please enter the number you want to add to the list or 'next'")
    big_num = max(input_list)
    smol_num = min(input_list)
    diff_of_big_smol = big_num - smol_num
    diff_of_nums = diff_of_big_smol / len(input_list)-1
    look_num = smol_num
    while look_num != big_num:
        if look_num in input_list:
            look_num += diff_of_nums
        else:
            print("false")
    print("true")

increment_of_list()