# Steam_Parser

Парсер - программа для автоматического сбора информации, размещённой на сайтах. Источником данных служит html код, который парсер анализирует на основе дополнительных библиотек.

Торговая площадка Steam обладает широким кругом различных игровых предметов. Многие сайты/таблицы для сравнения цен, постоянно парсят информацию с нее, а также со сторонних ресурсов.

Сформированные ссылки для торговой площадки Steam имеют одинаковую структуру, например https://steamcommunity.com/market/search?appid=730&q=desert-eagle#p1_default_desc и https://steamcommunity.com/market/search?appid=578080&q=m416#p2_default_desc. <br>
Различающиеся параметры: <br>
* appid - кодовая комбинация, соответствующая игре;
* q - запрос пользователя;
* p - страница.
  
Таким образом ссылки можно формировать в переменной типа string и парсить в цикле, а результаты сохранять в БД MS SQL.

Все страницы имеют одинаковое наполнение. Html код, который нужен для анализа выглядит следующим образом: <br> 1. <div class="market_listing_row market_recent_listing_row market_listing_searchresult" id="result_0" data-appid="730" **data-hash-name="Desert Eagle | Printstream (Well-Worn)**">. data-hash-name содержит имя скина. <br> 2. <span class="market_listing_num_listings_qty" **data-qty="80">80**</span>. data-qty содержит количество лотов на торговой площадке. <br> <span class="normal_price" **data-price="3819" data-currency="1">$38.19 USD**</span>. Класс normal_price содержит цену для покупателя и для продавца (разницу между ними - комиссию забирает себе площадка). 

Для увеличения количества информации в базу данных также отправляется парсинг-запрос пользователя, дата и время, а также с сайта banki.ru курс доллара к рублю из класса class="Text__sc-j452t5-0 bCCQWi".

СУБД - Microsoft SQL содержит 4 таблицы, по одной таблице на каждую игру. <br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/dab98eb8-6414-4906-a842-c60500eec131) <br>

Столбцы в таблицах идентичны. <br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/49b4f8f9-a09b-425d-8c10-f9f501aec896) <br>

Код создания таблиц и столбцов в них. Формат VARCHAR пришлось использовать везде, т.к. параметры, которые парсер извлекает с сайтов, не имеют типа данных.

CREATE TABLE CS_2(
Parsing_request VARCHAR(60),
Skin_name VARCHAR (60),
Quality VARCHAR (60),
Price VARCHAR (60),
Parsing_time VARCHAR (60),
Dollar_rate VARCHAR(60),)

Парсер написан на Python с использованием сторонних библиотек для чтения HTML, а также для взаимодействия с Microsoft SQL.
При запуске появляется меню.


В режиме парсинга пользователь вводит парсинг-запрос, а также количество страниц, которые будут парсить.<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/792127da-0276-4ef6-96e1-a20a6d967f0f)<br>

При успешном парсинге в консоли будут следующие сообщения.<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/ca680092-9408-4a90-84df-c29d0f25814a)

При переходе в раздел работы с базой данных появится меню<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/8f2b9d20-4e74-4697-b872-114f918462b8)

При выборе любого пункта для продолжения необходимо выбрать базу данных. Можно выбрать все, можно выбрать только одну<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/dd2b0c75-a804-48c3-a251-df55818930c4)

Содержимое баз данных<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/5bf1b46d-8181-4925-90a1-997af2de090a)

Содержимое базы данных в MS SQL<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/b27cbcde-14bc-4e96-8788-04b7e0358641)

Добавление данных в базу данных<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/b1cc936b-57e7-4312-b2de-d507162c8a98)

Проверка содержимого <br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/6d84c2d1-6327-49a1-86bb-b61f6497f730)<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/7e3700ca-0848-47d2-a5e9-3c606f4ee7d9)

Удаление информации<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/aae9aeca-4b9e-436c-95f7-3ff1825a05b7)

Проверка содержимого <br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/484a568d-e891-4ada-92df-a359803f9b6a)<br>
![image](https://github.com/DerbiLow/Steam-Parser/assets/126500303/969c50a6-764c-4b80-add9-edbf0dc5fa70)

Ссылка на видео демонстрацию - https://disk.yandex.ru/i/r1IclOAkxg-V_Q 


