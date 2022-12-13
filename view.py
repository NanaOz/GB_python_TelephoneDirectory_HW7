def print_data(data):
    if len(data) > 0:
        print("ФАМИЛИЯ".center(15), "ИМЯ".center(15), "ОТЧЕСТВО".center(15),
              "ТЕЛЕФОН".center(15), "АДРЕС".center(20))
        print("-" * 90)
        for item in data:
            print(item[0].ljust(15), item[1].ljust(15), item[2].ljust(15),
                  item[3].ljust(15), item[4].ljust(20))
    else:
        print("В справочнике нет данных!")


def search_data(search, data): #работает только по поиску фамилии
    if len(data) > 0:
        for item in data:
            if search in item:
                return item
