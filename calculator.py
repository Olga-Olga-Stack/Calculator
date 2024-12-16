def calculator():
    while True:
        try:
            a = float(input("Введите первое число: "))
            operator = input("Введите арифметический знак (+, -, *, /): ")
            b = float(input("Введите второе число: "))

            if operator == '+':
                result = a + b

            elif operator == '-':
                result = a - b

            elif operator == '*':
                result = a * b

            elif operator == '/':
                if b == 0:
                    raise ZeroDivisionError("Ошибка: на ноль делить нельзя")
                    result=a/b
            else:
                raise VaueError ("Ошибка: неверное действие")
            print("Результат",result)

        except VaueError as ve:
            print(f"Ошибка ввода:{ve}. Попробуйте снова")
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(f"Произошла ошибка:{e}. Попробуйте снова")

            #Предложить пользовартелю продолжить или выйти
        retry=input("Выполнить еще операцию? (да/нет)").strip().lower()
        if retry!="да":
            print("Спасибо. До свидания!")
            break

calculator()




