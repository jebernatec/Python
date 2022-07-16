# postal code in range(10000 - 1000000) no more than two consecutive numbers
import re

P = input()

regex_integer_in_range = r"^([1-9][0-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9][0-9]|1000000)$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# decorators, write the name of the persons in age range
def person_lister(output):
    def inner(people):
        people = sorted(people, key = lambda p: int(p[2]))
        result = []
        for p in people: 
            result.append(output(p))
        return result
    return inner

@person_lister
def output_format(people):
    return ("Mr. " if people[3] == "M" else "Ms. ") + people[0] + " " + people[1]

if __name__ == '__main__':
    N = int(input())
    if N <= 10 and N >=1:
        people = [input().split() for i in range(N)]
        print(*output_format(people), sep="\n")

# how many emails recibed the mail
from logging import raiseExceptions

class Email():
    def number_emails(self, emails: list[str]):
        set_emails = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            set_emails.add(f'{local}@{domain}')
        return len(set_emails)

def str_email(list):
    n = len(list)
    for i in range(0,n):
        email = list[i]

        if len(email) <= 100 and len(email) >= 1 and email[0] != '+' and email[-4:] == '.com' and (email.count('@')>0) == True:
            continue
        else:
            print(f'email:{email} is invalid, please check:\n 1<=email<=100\ndo not start with character "+"\neach email has the character "@"\nemail ends in ".com" ')
            return False

if __name__ == '__main__':
    # put your email list here
    list = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    str_email(list)
    if str_email(list) == False: 
        raise Exception("invalid emial")
    else: 
        emails = Email()
        print(emails.number_emails(list))
    
# prime numbers
import math

def is_prime(number):

    cont = 0
    if number == 1:
        return False

    else:
        for i in range (1, number+1):
            if number % i == 0: 
                cont +=1

        if cont == 2:
            return True
        else:
            return False

def is_prime_fast(number): 
    if number <= 1 or (number > 2 and number % 2 == 0): 
        #print(f"{number} no es primo")
        return False

    else: 
        for factor in range (2, int(math.sqrt(number))+1): 
            if number % factor == 0: 
                return False
    return True

for n in range(10):
    assert is_prime(n) == is_prime_fast(n)

# function that return all prime numbers up to and including n

def prime_numbers(n):
    numbers = []
    for i in range(1,n):
        if i == 1:
            continue
        else:
            lista = [j for j in range(1,n) if i%j == 0]
            if len(lista) == 2:
                numbers.append(i)
    print(numbers) 

n = int(input('n:'))
prime_numbers(n)