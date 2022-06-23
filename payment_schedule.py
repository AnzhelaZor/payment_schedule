import connection

db = connection.make()

def read_many():
    # Открытие соединения с БД
    db = connection.make()
    # Объект взаимодействия с БД
    cursor = db.cursor()
    # Сам SQL-запрос
    df = "SELECT `итого` , `ставка` , `срок` FROM `заявка на кредит` where `код заявки кредита`=5"
    # Выполняем запрос
    cursor.execute(df)
    rows = cursor.fetchmany()

    for row in rows:
        summ = row["итого"]
        stavka = row["ставка"]
        srok = row["срок"]
    stavka = stavka /12 /100 #ставка в месяц в десятичном виде
    k = (stavka * (1 + stavka) ** srok) / ((1 + stavka) ** srok - 1) #коэффициент аннуитета
    a_payment = round(k * summ,2) #ежемесячный платеж

    # цикл для информации по периоду
    for i in range(1,srok+1):
        insert_debt = round(stavka * summ,2) #долг по процентам
        principal_debt = round(a_payment - insert_debt,2) #основной долг
        remains_principal_debt = round(summ - principal_debt,2) #Остаток основного долга
        summ = remains_principal_debt
        str = [i,a_payment,principal_debt,insert_debt,remains_principal_debt] #информация по периоду
        print(str)
    else:
        print('\nДолг погашен')
columns = ['Месяц', 'Ежемесячный платеж', 'Основной долг', 'Долг по процентам', 'Остаток основного долга'] #колонки для таблицы
print(columns)
print(read_many())

