#zad 1
def square(n:int) -> int:
    return int(n**2)

print(square(5))
print(square(10))

#zad 2
def fitler_even(lst:list) -> list:
    even_num = [x for x in lst if x % 2 == 0]
    return even_num

print(fitler_even([1,2,3,4,5]))

#zad 3 

def word_count(text:str) -> dict[str, int]:
   
    word_dict = {}
    for letter in text.lower():
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            counter+=1
            word_dict[f"{letter}"] = f"{counter}"
            continue
    return word_dict

print(word_count('aaalllliii'))