import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='parking'
)
mycursor = mydb.cursor()

def Menu():
    print("\n--- Parking Management System ---")
    print("1: Add Parking Details")
    print("2: View Parking Details")
    print("3: Add Vehicle Details")
    print("4: Remove Vehicle Record")
    print("5: View Vehicle Details")
    print("6: Exit")
    choice = int(input("Please Select an Option: "))
    if choice == 1:
        Add_Record()
    elif choice == 2:
        Rec_View()
    elif choice == 3:
        Vehicle_Detail()
    elif choice == 4:
        remove()
    elif choice == 5:
        Vehicle_View()
    elif choice == 6:
        exit()
    else:
        print("Invalid option. Try again.")
        Menu()


def Add_Record():
    print("\n--- Add Parking Details ---")
    pid = int(input("Enter Parking ID: "))  # Integer input for parking ID
    level = input("Enter Parking Level (e.g., GROUND, FIRST): ")  # Parking level
    freespace = int(input("Enter the number of free spaces: "))  # Integer for free space
    vehiclecount = int(input("Enter Number of Vehicles: "))  # Number of vehicles
    payments = float(input("Enter Payments: "))  # Monetary value for payments
    query = """
        INSERT INTO parkmaster (pid, level, freespace, vehiclecount, payments) 
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (pid, level, freespace, vehiclecount, payments)
    mycursor.execute(query, values)
    mydb.commit()
    print("Parking details added successfully!")
    Menu()


def Rec_View():
    print("\n--- View Parking Details ---")
    print("1: Search by Parking ID")
    print("2: Search by Level")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pid = int(input("Enter Parking ID: "))
        query = "SELECT * FROM parkmaster WHERE pid = %s"
        mycursor.execute(query, (pid,))
    elif choice == 2:
        level = input("Enter Parking Level: ")
        query = "SELECT * FROM parkmaster WHERE level = %s"
        mycursor.execute(query, (level,))
    else:
        print("Invalid choice.")
        Rec_View()
        return

    records = mycursor.fetchall()
    for record in records:
        print(f"Parking ID: {record[0]}, Level: {record[1]}, Free Space: {record[2]}, Vehicle Count: {record[3]}, Payments: {record[4]}")
    Menu()


def Vehicle_Detail():
    print("\n--- Add Vehicle Details ---")
    vehiclename = input("Enter Vehicle Name: ")
    dateofpur = input("Enter Date of Purchase (YYYY-MM-DD): ")
    query = "INSERT INTO vehiclerec (vehiclename, dateofpur) VALUES (%s, %s)"
    values = (vehiclename, dateofpur)
    mycursor.execute(query, values)
    mydb.commit()
    print("Vehicle details added successfully!")
    Menu()


def remove():
    print("\n--- Remove Vehicle Record ---")
    vehiclename = input("Enter the Vehicle Name to Delete: ")
    query = "DELETE FROM vehiclerec WHERE vehiclename = %s"
    mycursor.execute(query, (vehiclename,))
    mydb.commit()
    print("Vehicle record deleted successfully!")
    Menu()


def Vehicle_View():
    print("\n--- View Vehicle Details ---")
    vehiclename = input("Enter Vehicle Name to View Details: ")
    query = "SELECT * FROM vehiclerec WHERE vehiclename = %s"
    mycursor.execute(query, (vehiclename,))
    records = mycursor.fetchall()
    for record in records:
        print(f"Vehicle Name: {record[0]}, Date of Purchase: {record[1]}")
    Menu()


# Start the program
Menu()
