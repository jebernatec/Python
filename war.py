#Given an array of integers your solution should find the smallest integer.
def find_smallest_int(arr):
    # Code here
    if len(arr) == 1:
        num = arr[0]
    else:
    
        if arr[0] < arr[1]:
            num = arr[0]
        else: 
            num = arr[1]

        for i in range(0,len(arr)-1):
            if arr[i] < arr[i+1]:
                if arr[i] < num:
                    num = arr[i]

        if arr[len(arr)-1] < num:
            num = arr[len(arr)-1]

    return num

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
    suma = 0
    if num > 0:
        for i in range(0,num+1):
            suma +=i
        return suma

# Build a function that returns an array of integers from n to 1 where n>0.
def reverse_seq(n):
    list = []
    while n >= 1:
        list.append(n)
        n -=1
    return list

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i**2
    return sum

# create a function that removes the first and last characters of a string
def remove_char(s):
    return s[1:len(s)-1]

# Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    h_to_ms = 3600000
    m_to_ms = 60000
    s_to_ms = 1000
    
    h = h * h_to_ms
    m = m * m_to_ms
    s = s * s_to_ms
    
    return h+m+s
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
def count_positives_sum_negatives(arr):
    
    if len(arr) == 0:
        return []
    else:
        sum_pos = 0
        sum_neg = 0
        for i in arr:
            if i > 0:
                sum_pos += 1
            else:
                sum_neg += i
    return [sum_pos, sum_neg]

# Write a function that takes such collection and counts the points of our team in the championship
def points(games):
    sum = 0
    for i in games:
        if i[0] > i[2]:
            sum += 3
        elif i[0] == i[2]:
            sum += 1
    return sum

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
# or
def sum_two_lowest(numbers):
    num = numbers[0]
    for i in numbers:
        if num > i:
            num = i

    menor1 = num

    if menor1 == numbers[0]:
        num2 = numbers[1]
    else:
        num2 = numbers[0]
        for i in numbers:
            if i > menor1:
                if num2 > i:
                    num2 = i

    menor2 = num2

    return menor1 + menor2 

# Simple, given a string of words, return the length of the shortest word(s).
def find_short(s):
    
    list = s.split()
    list2 = []
    
    for i in list:
        list2.append(len(i))
        
    return sorted(list2)[0]