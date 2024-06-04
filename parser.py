import requests
from bs4 import BeautifulSoup
import time
import datetime
import pyodbc

choice = 10
admin_choice = 10
print (f"Hi! This is a parser for the Steam trading platform")

while choice !=0:
    conn = pyodbc.connect (r"Driver={SQL Server};Server=LAPTOP-1APQ4KHQ\SQLEXPRESS;Database=steam_parser;Trusted_Connection=yes;")
    cursor = conn.cursor()
    print (f"Select a menu item", '\n', "1. CS2 Skin Parsing", '\n', "2. Dota 2 Skin Parsing", '\n',"3. Rust Skin Parsing", '\n', "4. PUBG Skin Parsing", '\n', "5. Working with the databases", '\n', "0. Exit", '\n')
    choice = input("Your choice --> ")
    choice = int(choice)
    if choice == 0:
       print (f"Have a nice day!")
    elif choice > 0 and choice < 5:
       skin_name = input (f"Enter the name of the skin that we will parse --> ")
       max_page = input(f"Enter the number of pages that we will parse --> ")
       max_page = int(max_page)
       current_page_name = "https://www.banki.ru/products/currency/usd/"
       req = requests.get(current_page_name)
       src = req.text
       soup = BeautifulSoup(src, "lxml")
       print("parsing rate USD complete")
       cource_usd = soup.find(class_="Text__sc-j452t5-0 bCCQWi").text
       for i in range (1, max_page+1):
           if choice == 1:
               current_page_name = "https://steamcommunity.com/market/search?appid=730"
           elif choice == 2:
               current_page_name = "https://steamcommunity.com/market/search?appid=570"
           elif choice == 3:
               current_page_name = "https://steamcommunity.com/market/search?appid=252490"
           elif choice == 4:
               current_page_name = "https://steamcommunity.com/market/search?appid=578080"
           current_page_name = current_page_name + "&q=" + skin_name + "#p" + str(i) + "_default_desc"
           req = requests.get(current_page_name)
           src = req.text
           soup = BeautifulSoup(src, "lxml")
           print("parsing skins complete")
           for ab in range (0,10):
               result = "result_" + str(ab)
               item_code = soup.find(class_="market_listing_row market_recent_listing_row market_listing_searchresult",id=result).get("data-hash-name")
               item_quality = soup.find(class_="market_listing_row market_recent_listing_row market_listing_searchresult",id=result).find(class_="market_listing_num_listings_qty").get("data-qty")
               item_price = soup.find(class_="market_listing_row market_recent_listing_row market_listing_searchresult",id=result).find(class_="normal_price").text
               curr_time = datetime.datetime.now()
               if choice == 1:
                   insert = "INSERT INTO CS_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                   data_type = (skin_name, item_code, item_quality, item_price, curr_time, cource_usd)
                   cursor.execute(insert, data_type)
                   conn.commit()
                   print("Input DataBase CS_2 complete")
               if choice == 2:
                   insert = "INSERT INTO DOTA_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                   data_type = (skin_name, item_code, item_quality, item_price, curr_time, cource_usd)
                   cursor.execute(insert, data_type)
                   conn.commit()
                   print("Input DataBase DOTA_2 complete")
               if choice == 3:
                   insert = "INSERT INTO RUST (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                   data_type = (skin_name, item_code, item_quality, item_price, curr_time, cource_usd)
                   cursor.execute(insert, data_type)
                   conn.commit()
                   print("Input DataBase RUST complete")
               if choice == 4:
                   insert = "INSERT INTO PUBG (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                   data_type = (skin_name, item_code, item_quality, item_price, curr_time, cource_usd)
                   cursor.execute(insert, data_type)
                   conn.commit()
                   print("Input DataBase PUBG complete")
           time.sleep(5)
       conn.close()
    elif choice == 5:
        while admin_choice != 0:
            conn = pyodbc.connect(r"Driver={SQL Server};Server=LAPTOP-1APQ4KHQ\SQLEXPRESS;Database=steam_parser;Trusted_Connection=yes;")
            cursor = conn.cursor()
            print("Select a menu item", '\n', "1. View information", "\n", "2. Add information", "\n", "3. Delete information", "\n", "0. Exit to main menu", "\n")
            admin_choice = input("Your choice --> ")
            admin_choice = int(admin_choice)
            if admin_choice > 0 and admin_choice < 5:
                print ("Select database", "\n", "1. All tables", "\n", "2. CS_2", "\n", "3. Dota_2", "\n", "4. Rust", "\n", "5. PUBG")
                base_choice = input("Your choice --> ")
                base_choice = int(base_choice)
            if admin_choice == 1:
                if base_choice == 1:
                    print(cursor.execute("SELECT * FROM CS_2").fetchall())
                    print(cursor.execute("SELECT * FROM DOTA_2").fetchall())
                    print(cursor.execute("SELECT * FROM RUST").fetchall())
                    print(cursor.execute("SELECT * FROM PUBG").fetchall())
                elif base_choice == 2:
                    print(cursor.execute("SELECT * FROM CS_2").fetchall())
                elif base_choice == 3:
                    print(cursor.execute("SELECT * FROM DOTA_2").fetchall())
                elif base_choice == 4:
                    print(cursor.execute("SELECT * FROM RUST").fetchall())
                elif base_choice == 5:
                    print(cursor.execute("SELECT * FROM PUBG").fetchall())
            elif admin_choice == 0:
                print ("go to main menu")
            elif admin_choice == 2:
                new_parsing_request = input("Input new parsing request --> ")
                new_skin_name = input("Input new skin name --> ")
                new_quality = input("Input new quality --> ")
                new_price = input("Input new price --> ")
                new_parsing_time = input("Input new parsing time --> ")
                new_dollar_rate = input("Input new dollar rate --> ")
                if base_choice == 1:
                    insert = "INSERT INTO CS_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                    insert = "INSERT INTO DOTA_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                    new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                    insert = "INSERT INTO RUST (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                    new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                    insert = "INSERT INTO PUBG (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                    new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                elif base_choice == 2:
                    insert = "INSERT INTO CS_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                    new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                elif base_choice == 3:
                    insert = "INSERT INTO DOTA_2 (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                        new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                elif base_choice == 4:
                    insert = "INSERT INTO RUST (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                        new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                elif base_choice == 5:
                    insert = "INSERT INTO PUBG (Parsing_request, Skin_name, Quality, Price, Parsing_time, Dollar_rate) VALUES (?, ?, ?, ?, ?, ?);"
                    data_type = (
                        new_parsing_request, new_skin_name, new_quality, new_price, new_parsing_time, new_dollar_rate)
                    cursor.execute(insert, data_type)
                    conn.commit()
                print("Add complete")
            elif admin_choice == 3:
                find_skin_name = input("Input the skin name you want to delete --> ")
                if base_choice == 1:
                    insert = "DELETE FROM CS_2 WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                    insert = "DELETE FROM DOTA_2 WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                    insert = "DELETE FROM RUST WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                    insert = "DELETE FROM PUBG WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                if base_choice == 2:
                    insert = "DELETE FROM CS_2 WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                if base_choice == 3:
                    insert = "DELETE FROM DOTA_2 WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                if base_choice == 4:
                    insert = "DELETE FROM RUST WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                if base_choice == 5:
                    insert = "DELETE FROM PUBG WHERE Skin_name = ?;"
                    cursor.execute(insert, find_skin_name)
                    conn.commit()
                print("Delete complete")
            else:
                print(f"You may have made a mistake, please try again")
            conn.close()
    else:
        print (f"You may have made a mistake, please try again")


