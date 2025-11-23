#double = [ x * 2 for x in range(1,16)]
#square = [ y ** 2 for y in range(1,11)]

#print(square)

#fruits = ["mango","coconut","custardapple","banana","kiwi"]

#fruit = [ fruit.upper() for fruit in fruits]
#fruit_char = [fruit[0] for fruit in fruits]

#numbers = [1,4,5,6,8,-5,2,-8,9,-2,-4,-12]
#positive_num = [num for num in numbers if num >= 0]
#negative_num = [num for num in numbers if num <= 0]
#pos_even_num = [num for num in numbers if num % 2 == 0 and num >= 0]
#neg_even_num = [num for num in numbers if num % 2 == 0 and num <= 0]

#print(pos_even_num)

grades = [60,70,56,67,89]
result = [grade for grade in grades if grade >=60 ]
print(result)