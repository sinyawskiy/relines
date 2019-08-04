# -*- coding: utf8 -*-

# Нужно вывести числа от 1 до 100, с некоторыми правилами. 
# Числа, кратные 3 заменить на Fizz, числа, кратные 5 заменить на Buzz, числа кратные и 3 и 5 заменить на FizzBuzz. 
# Остальные числа выводить как есть.
# Компания http://relines.ru

def replacer():
    for item in xrange(1, 101):
        result = []
        if not item%3:
            result.append('Fizz')
        if not item%5:
            result.append('Buzz')
        if len(result):
            print(''.join(result))
        else:
            print('{}'.format(item))

if __name__ == '__main__':
    replacer()
