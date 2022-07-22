#В 73-й серии сериала «Теория большого взрыва» Шелдон Купер заметил, что число 73 обладает тремя нетривиальными свойствами, 
#которые делают его «самым замечательным числом». 73 — это 21-ое простое число. Его зеркальное отражение 37 является 12-ым, 
#чье отражение 21 является результатом умножения, не упадите, 7 и 3. Так как Шелдон любит точность и аккуратность, давай 
#найдём все числа в диапазоне [45387634, 375630355], которые делятся на 3, 7 и 73, заканчиваются на 1234 и начинаются на 1


def check(n):
  if (n % 3 == 0 and n % 7 == 0 and n % 73 == 0         # str(i)[-4:] разберем это выражение. Функция str(i) преобразует число i в строку.
      and str(n)[-4:] == '1234' and str(n)[0] == '1'):  # Срез [-4:] берет последние 4 символа
    return True
  return False

for i in range(45387634, 375630356, 2): # рассмотрим генератор range(start, end, step) начало, конец (не включая) и шаг. 
  if check(i):                          # Тут мы знаем, что число четное, так как последняя цифра 4
    print(i)
