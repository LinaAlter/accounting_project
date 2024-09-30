from datetime import datetime




def calculate_salary(employee):
    with open('data/employees_salary_info.csv', encoding='utf8') as f:
        for line in f:
            name, hours, tariff = line.rstrip().split(",")
            if name == employee:
                salary = int(hours) * int(tariff)
                print(f'К оплате работнику: {salary}')
                current_date = datetime.now()
                print(current_date)
                return salary



if __name__ == '__main__':          
    calculate_salary('Истомина') 