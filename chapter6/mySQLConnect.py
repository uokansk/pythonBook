import mysql.connector

# Устанавливаем соединение с сервером MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)

# Создаем базу данных
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE your_database_name")