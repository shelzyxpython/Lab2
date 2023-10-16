# def temp_cat(): #функция
#     temp = int(input())
#     if temp < -20: #Проверка условия, если холодно
#         return('Холодно')
#     elif temp >= 20 and temp < 0: #Проверка условия, если прохладно
#         return('Прохладно')
#     elif temp >= 0 and temp < 15: #Проверка условия, если зябко
#         return('Зябко')
#     elif temp >= 15 and temp < 25: #Проверка условия, если тепло
#         return('Тепло')
#     elif temp >= 25: #Проверка условия, если жарко
#         return('Жарко')
# print(temp_cat()) #вывод функции на экран


# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
# for i in phones:
#     if len(i) == 15 and i[0] == '+' and i[10] == '-' and i[2] == '(' and i[6] == ')' and i[1] != '+' or i[0] == 8: #проверка условий
#         print(i)
#     else:
#         print(-1)

# def lim_max(): #создал функцию
#     nums = (10, 20, 30, 40, 50, 60, 70, 80, 100) #список
#     limit = int(input())
#     for i in nums: #пересчет значений в списке
#         if limit > i: #условие
#             a = i
#     return a #возврат
# print(lim_max()) #вывод функции
