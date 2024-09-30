from application.salary import calculate_salary
from application.db.people import get_employees
from application.say import cow_saying


if __name__ == '__main__':

    target = input('🔵Чтобы получить информацию о сотруднике, введите "info".\n🔵Чтобы сделать рассчет заработной платы, введите "salary".\n🟩')
    if target == 'info':
        get_employees(input('Введите фамилию сотрудника:  '))
    elif target == 'salary':
        calculate_salary(input('Введите фамилию сотрудника: '))
    else:
         cow_saying('Неверно введено слово!')       


        
     