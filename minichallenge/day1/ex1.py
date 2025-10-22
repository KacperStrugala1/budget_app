#zad1
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#zad2
import math
list_100 = sum([x for x in range(1,101)])
print(list_100)

#zad3
range_n = int(input("Please type n(range of your numbers): "))
list_in_n_range = [x for x in range(1,range_n+1)]
print(list_in_n_range)
new_list = []
for num, i in enumerate(list_in_n_range):
    if num % 3 == 0:
        del num 
    else:
        new_list.append(num)
        continue

sum_of_n = sum([x for x in new_list])
print(sum_of_n)
print(len(new_list))
print(sum_of_n/len(new_list))