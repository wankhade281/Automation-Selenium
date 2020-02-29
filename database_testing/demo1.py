import time

import mysql.connector
from selenium import webdriver

db_con = mysql.connector.connect(host="localhost",  # database host, usually localhost
                                 user="admin1",  # database username
                                 passwd="admin",  # database password
                                 database="dbUser")  # database name
print("!!! Connect to MySql Database !!!")

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db_con.cursor()


def query_execute(query, value=None):
    cur.execute(query, value)
    db_con.commit()


def query_fetchall(query, value=None):
    cur.execute(query, value)
    return cur.fetchall()


def insert_query(data, table_name=None):
    column = []
    rows_values = []
    val = []
    for key, value in data.items():
        column.append(key)
        rows_values.append("%s")
        val.append(value)
    column = ', '.join(column)
    val_ = ', '.join(['%s'] * len(val))
    query = '''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
    print(query)
    query_execute(query=query, value=val)


data = {'Title': "Test Database", 'Description': "Database Testing",
        'Colour': "Green",
        'isPinned': 1, 'isArchive': 1,
        'isTrash': 1, 'user_id': 1}

insert_query(data, table_name="notes")
print("!!! Data inserted Successfully !!!")
query = "select * from users"
result = query_fetchall(query)
# print all the first cell of all the rows
for row in result:
    print(row[0],"  ",row[1],"  ",row[2])
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("//a[@class='nav__button-secondary']").click()
    time.sleep(1)
    driver.find_element_by_id("username").send_keys(row[1])
    driver.find_element_by_id("password").send_keys(row[2])
    driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
    time.sleep(2)
    if "LinkedIn" == driver.title:
        print("Login Successful")
        driver.find_element_by_xpath("//img[@id='ember26']").click()
        driver.find_element_by_xpath("//li[@class='nav-dropdown__item nav-settings__dropdown-item "
                                     "nav-dropdown__action t-14 t-black t-bold']").click()
        driver.close()
    else:
        time.sleep(3)
        print("Login Unsuccessful")
        driver.close()
        break
print("!!! Data print Successfully !!!")
db_con.close()
