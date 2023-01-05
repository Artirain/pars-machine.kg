from bs4 import BeautifulSoup
import requests
import fake_useragent
import json
import os
import random
import time

user = fake_useragent.UserAgent().random



def get_data(url):

    # url = 'https://www.mashina.kg/search/all/'
    headers = {'user-agent': user}

    passengers_cars = {}

    iteration_count = 941
    print(f'Всего итераций: #{iteration_count}')

    for item in range(1, 100):

        req = requests.get(url + f'&page={item}', headers=headers)
        

        with open('machine-kg/index.html', 'w', encoding="utf-8-sig") as file: #запись в index.html
            file.write(req.text)

        with open('machine-kg/index.html', 'r', encoding="utf-8-sig") as file: #запись в index.html
            src = file.read()


    
        soup = BeautifulSoup(src, 'lxml')


        cars_hrefs = soup.find('div', class_='table-view-list').find_all('a')
        cars_titles = soup.find('div', class_='table-view-list').find_all('h2')
        cars_price = soup.find('div', class_='table-view-list').find_all('div', class_='block price')
        cars_year = soup.find('div', class_='table-view-list').find_all('p', class_='year-miles')

        for i in range(len(cars_hrefs)):

            item_href = 'https://www.mashina.kg' + cars_hrefs[i].get('href')
            item_title = cars_titles[i].text.strip()
            price = cars_price[i].find('p').text.strip().replace(' ', '').replace('\n\n', ' ')
            year = cars_year[i].find('span').text.strip().replace(' ', '')


            match item_title.split(' ')[0]: #title делим по пробелу и забираем первое слово, выполняем операции над этим словом          
                case car_name: #с помощью case записывваем переменную title по индексу 0 в переменную car_name
                    if not car_name in passengers_cars: #если не содержится такого ключа, то добавляем ключ, если содержится - добавляем новую машину
                        passengers_cars[car_name] = [{"cars_name": item_title, "year": year, "price": price, "href": item_href}] #создаем список с 1 элементом
                    else:
                        passengers_cars[car_name].append({"cars_name": item_title, "year": year, "price": price, "href": item_href}) #добавляем в существующий список

            
                 
            # if item_title.split(' ')[0] == 'Mercedes-Benz':
            #     passengers_cars['Mercedes-Benz'].append({"cars_name": item_title, "price": price, "href": item_href})

            print(f'{item_title}: {price}: {item_href}')
            
        iteration_count -= 1
        print(f'Итерация #{item} завершена, осталось итераций #{iteration_count}')
        if iteration_count == 0:
            print('Сбор данных завершен')
        # time.sleep(random.randrange(2, 4))

    with open('machine-kg/pars.json', 'w', encoding="utf-8-sig") as file:
        json.dump(passengers_cars, file, indent=4, ensure_ascii=False)

get_data('https://www.mashina.kg/search/all/all/?currency=2&sort_by=upped_at+desc&time_created=all')