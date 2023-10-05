lst = [30, 75, 9, 97, 50, -4, 70, 59]
print(max(lst))
lst.remove(min(lst))
lst.sort()
#Last 4 numbers:
print(lst[-4:])
#First 4 numbers:
print(lst[:4])
################################################
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
count = 0
for sublist in main_lst:
    if sublist[0] == "python":
        count += 1
print(count)
################################################
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
result = ' '.join(word.capitalize() for word in my_lst)
print(result)
###############################################
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst=[]
for item in my_lst:
    new_lst.extend([item])
print(new_lst)
################################################
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
new_num=my_lst[2]
my_lst[2] = my_lst[4]
my_lst[4]=new_num
print(my_lst)
###########################################
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
#############################################
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
new_tuple = tuple1 + (9,)
print(new_tuple)
#############################################
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1 + tuple2
print(new_tuple)
#############################################
