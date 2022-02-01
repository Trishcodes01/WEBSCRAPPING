import requests
from bs4 import BeautifulSoup as BS
import pymysql.cursors
from pprint import pprint


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='jumiatyres',
                             cursorclass=pymysql.cursors.DictCursor)


url = "https://www.jumia.com.ng/automobile-tyres/"
headers = requests.utils.default_headers()
headers.update({
        "user-agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })


Brand_name_list=[]
new_price1=[]
category1=[]

# for h in range(1,27):
#     my_response = requests.get(f"https://www.jumia.com.ng/automobile-tyres/?page={h}#catalog-listing")
#     # print(my_response.status_code)

#     first_soup = BS(my_response.content, features = "lxml")
#     second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})
#      # print(second_soup)
    
#     list_of_soups = second_soup.find_all("article", attrs = {"class" : "prd _fb col c-prd"})
    

#     for tyres in list_of_soups:
#         tyres_details = tyres.find("a")

#         category= tyres_details.get("data-category")
#         category = category.split("/")[0]
#         # print(category)
#         category1.append(category)
        
#         # print(len(category1))

#         try:
#             tyres_name = tyres_details.get("data-name")
#             # print(tyres_name)
#         except:
#             tyres_name = None

#         Brand_name_list.append(tyres_name)
#     # print(len(Brand_name_list))


#         try:
#             new_div = tyres.find("div", attrs = {"class" : "prc"})
#             # print(new_div)
#             tyres_new_price = int((new_div.text).lstrip("₦").replace(",", ""))
#             #  print(tyres_new_price)    
#         except:
#             tyres_new_price = None

#         new_price1.append(tyres_new_price)
#     # print(len(new_price1))



#     zipped =zip(Brand_name_list,category1,new_price1)
#     zipped_list = list(zipped)
#     print(zipped_list)


def create_product_table():

    with connection:

         with connection.cursor() as cursor:
             
            sql = "CREATE TABLE product (id INT(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, Brand_name_list CHAR(50), category1 CHAR(40), newprice INT(7));"
       
            cursor.execute(sql)
            connection.commit()

# create_product_table()

def insert_into_table():
    with connection.cursor() as cursor:
        for wheels in zipped_list:
            sql = "INSERT INTO product (Brand_name_list, category1, newprice) VALUES ('{}','{}','{}')".format(*wheels)
            cursor.execute(sql)
            connection.commit()
# insert_into_table()

def filters_table():
    user_input = input("")

    with connection.cursor() as cursor:

        sql = "SELECT *FROM product WHERE Brand_name_list LIKE ('{}')".format(user_input)

        cursor.execute(sql)
        result = cursor.fetchall()
        connection.commit()
        print(result)

filters_table()

