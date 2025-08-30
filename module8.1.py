import mysql.connector

def get_airport_by_code(user_ident):

    while user_ident != "":
        sql = f"SELECT name, municipality FROM airport WHERE ident = '{user_ident}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            for row in result:
                print(f"Airport name is: {row[0]} and the location is: {row[1]}.")
        else:
            print("No airport found with that code.")

        user_ident = input('Enter airport code: ')

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True
         )

user_input = input("Enter airport code: ")
get_airport_by_code(user_input)