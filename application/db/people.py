from datetime import datetime

def get_employees(employee):
    with open('data/employees_full_info.csv', encoding='utf8') as f:
        for line in f:
            last_name, name, second_name, birth_date, job = line.rstrip().split(",")
            if last_name == employee:
                current_date = datetime.now()
                print(f'Сотрудник: {last_name} {name} {second_name}\nДата рождения: {birth_date}\nДолжность: {job}')
                print(current_date)

if __name__ == '__main__':
    get_employees('Дорон')
