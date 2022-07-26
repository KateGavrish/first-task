#Программист Миша владеет биткоинами, кошелек с которыми хранит на флешке с аппаратным шифрованием.
#Пароль от нее он записал на бумажке, которую потерял, а самостоятельно вспомнить нужную комбинацию ему не под силу. 
#Единственное, что он знает про свой пароль, это что он является счастливым числом - то есть сумма первой 
#половины числа совпадает со второй половиной числа, и он делится на 3, 13 и 73. Например, число 12344321 - счастливое.
#Известно, что пароль был шестизначным. Определите все возможные пароли, которые соответствуют условию.


def is_digit_happy(n):
  a = list(map(int, list(str(n))))  # Преобразуем число в строку, затем в список символов. Далее функцией map преобразуем каждый элемент списка в число
  if sum(a[:4]) == sum(a[4:]):      # Сравниваем суммы первой половины и второй
    return True
  return False


for i in range(100000, 1000000):
  if is_digit_happy(i) and i % 73 == 0 and i % 3 == 0 and i % 13 == 0:  # проверяем все условия
    print(i)
