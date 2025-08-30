import mysql.connector

def get_airport_by_code(user_area_code):

    while user_area_code != "":
        sql = f"SELECT name, type, municipality FROM airport WHERE iso_country = '{user_area_code}' ORDER BY type desc"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            for row in result:
                print(f"{row[0]} is a {row[1]} in {row[2]}.")
        else:
            print("No airport found with that code.")

        user_area_code = input('Enter area code: ')

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True
         )

user_input = input("Enter area code: ")
get_airport_by_code(user_input)