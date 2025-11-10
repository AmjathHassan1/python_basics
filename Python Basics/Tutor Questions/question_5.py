# String questions
#
# 1. Str ="python programming is simple " . Convert each of the words into capital letters

# Str ="python programming is simple "
# print(Str.upper())
#======================================================================

# 2. Split the words.

# print(Str.split())
#======================================================================

# 3. Check if there exist any space in the string. (Istring())

# print("space count : ", Str.count(" "))

# 4. Find the length of a string without using len function input by the user.

# Str=input("Enter a string: ")
# count=0
# for i in Str:
#     count+=1
# print(count, len(Str))

# ============================================================
# 5. Count every letters except space of a string without len function input by the user.
# count=0
# for i in Str:
#     if i.isalpha():
#         count+=1
# print(count)

# ====================================================
# 6. Write a program to count the vowels in a string input by the user.

# count=0
# for i in Str:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)

# =======================================================

# 7. Write a program to reverse a string

# print(Str[::-1])
# a =[]
# for i in Str[::-1]:
#     a.append(i)
# print("".join(a))

# =======================================================

# 8. Check a string is palindrome or not input by the user.

# if Str==Str[::-1]:
#     print(Str, "is a palindrome")
# else:
#     print(Str, "is not a palindrome")

# =======================================================

# 9. Take 3 string inputs from the user and find the largest of them (largest length)

# word_lst=[]
# for i in range(3):
#     word_lst.append(input("Enter a word: "))
# len_word=0
# large_word=""
# for i in word_lst:
#
#     if len(i)>len_word:
#         len_word = len(i)
#         large_word=i
# print(len_word, large_word)

# =======================================================

# 10. Str="data science ".find the first and last letter of this string.

# Str="data science "
# first_letter=""
# last_letter=""
# for i in Str:
#     if first_letter == "" and i.isalpha():
#         first_letter=i
# for i in Str[::-1]:
#     if last_letter == "" and first_letter and i.isalpha():
#         last_letter=i
# print(first_letter, last_letter)


# 11. Str="artificial intelligence ".count the occurrences of the letter "l".

# Str="artificial intelligence "
# print(Str.count('l'))
# count=0
# for i in Str:
#     if i=='l':
#         count+=1
# print(count)


# 12. Str ="the less you care about what others think the better your life become".
# check whether "you" exist in this string (hint :use membership operator)

# Str ="the less you care about what others think the better your life become"
# if "you" in Str:
#     print("Yes, you in Str")

# 13. Find the number of words in the above string.

# Str ="the less you care about what others think the better your life become"
# str_lst=Str.split(" ")
# print(len(str_lst))

# 14. Str="string IS SiMple".find the uppercase count and lowercase count.

# count=0
# Str="string IS SiMple"
# for i in Str:
#     if i.islower():
#         count+=1
# print(count)


# 15. Convert a string into a list.

# Str="string IS SiMple"
# lst_list=list(Str)
# print(lst_list)
