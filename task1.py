## Задача 1

#Дан список целых чисел. Найти второе по величине число в списке.

#**Дано:** 
#```python
numbers = [15, 7, 28, 10, 21]
numbers.sort()
print (numbers [-2])


#**Дано:**
#```python
numbers = [4, 6, 2, 11, 1, 11, 5]

max_number = max(numbers)
print (max_number)
count_max = numbers.count(max_number)
print (count_max)
for i in range(count_max):
    numbers.remove(max_number)
    print(numbers)
max_number2 = max(numbers)
print (max_number2)


