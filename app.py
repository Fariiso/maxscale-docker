# Name: Abdo Mohamed
# Email: abdomuridi@gmail.com
# Date: 2025-06-19
# Class: CNE 370 
# Description: This script connects to the MaxScale instance and performs several queries on sharded zipcode data.

"""
Description: This script connects to the MaxScale instance and runs queries on the
'all_zipcodes' database to:
1. Find the largest zipcode in zipcodes_one
2. Retrieve all zipcodes where state=KY
3. Retrieve all zipcodes with zipcodes between 40000 and 41000
4. Retrieve the TotalWages column for zipcodes where state=PA
"""

import mysql.connector

def main():
    # Connect to MaxScale
    conn = mysql.connector.connect(
        host="192.168.1.200",   # Updated to VM IP address
        port=4000,              # MaxScale port
        user="maxuser",
        password="maxpwd",
        database="all_zipcodes"
    )
    
    cursor = conn.cursor()

    # 1. Largest zipcode in zipcodes_one
    cursor.execute("SELECT MAX(Zipcode) FROM zipcodes_one;")
    largest_zip = cursor.fetchone()[0]
    print(f"Largest zipcode in zipcodes_one: {largest_zip}")

    # 2. All zipcodes where state=KY (Kentucky)
    cursor.execute("SELECT Zipcode FROM zipcodes_one WHERE State = 'KY';")
    ky_zipcodes = cursor.fetchall()
    print("\nZipcodes in Kentucky (zipcodes_one):")
    for row in ky_zipcodes:
        print(row[0])

    # 3. All zipcodes between 40000 and 41000 (assuming zipcodes_one)
    cursor.execute("SELECT Zipcode FROM zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
    zip_range = cursor.fetchall()
    print("\nZipcodes between 40000 and 41000 (zipcodes_one):")
    for row in zip_range:
        print(row[0])

    # 4. TotalWages column where state=PA (Pennsylvania)
    cursor.execute("SELECT TotalWages FROM zipcodes_one WHERE State = 'PA';")
    wages_pa = cursor.fetchall()
    print("\nTotalWages in Pennsylvania (zipcodes_one):")
    for row in wages_pa:
        print(row[0])

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

