#Crie um programa que receba através de input dois números e retorne sua divisão.

def division(number_one,number_two):
    try:
        result = number_one / number_two

        return result

    except ZeroDivisionError:
        print ("A number it's not divisible by zero. ;)")

    except BaseException:
        print ("An unexpected error as occurred!! ")

def main():
    number_one = int(input("write a number: "))
    number_two = int(input("write other number: "))

    error_or_not = division(number_one, number_two)

    print(error_or_not)

main()