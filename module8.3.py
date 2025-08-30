import mysql.connector
from geopy.distance import geodesic

def getting_distance (user_input):

    while user_input != "":
        sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{user_input}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True
         )

first_code = input("Enter first airport code: ")
first_airport = getting_distance(first_code)
second_code = input("Enter second airport code: ")
second_airport = getting_distance(second_code)

distance_between_airports = geodesic(first_airport, second_airport).km
print(f"The distance between two airports is {distance_between_airports:.3f} kilometers.")