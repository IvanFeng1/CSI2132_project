import psycopg2
f = open("cred.txt","r")
uname = f.readline()
upass = f.readline()
uname = uname[0:len(uname)-1]
# connect to db
con = psycopg2.connect(
    host = "web0.eecs.uottawa.ca",
    database = "group_a03_g04",
    user=uname, 
    password =upass,
    port="15432"
)

cursor = con.cursor()

def printQuery(z, n=10):
    if len(z) < n:
        n = len(z)
    print("+-----------+")
    for i in range(n):
        x = z[i]
        for y in x: 
            print("+ "+str(y))
        print("+-----------+")
    



def title(): #main menu. admin and employee should prolly get prompted for passwords n stuff
    title= "+------------------------------------+\n|                                    |\n|                                    |\n|                                    |\n|                                    |\n| [A]: Customer                      |\n| [B]: Employee                      |\n| [C]: Admin                         |\n|                                    |\n|                                    |\n+------------------------------------+"
    print(title)
    x = input("[ ]:")
    if x == "A":
        customer()
    elif x == "B":
        employee()
    elif x == "C":
        admin()

def cSearch(): #this will later take as input the date n stuff. db as is now is empty so idk what to do with them
        print("[1]: Daisu")
        print("[2]: Ivay")
        print("[3]: Shulizany")
        print("[4]: Lame Places")
        print("[5]: Lotsa Rooms")
        print("[6]: Old Zealand")
        print("[7]: Any")
        print("Which Hotel Company?:")
        x1 = input("[ ]:")
        if x1 == "7":
            x1 = "*"
        x2 = input("Before/Exactly/After (B/E/A): \n")
        x3 = input("Date: (YY-MM-DD)\n")
        cursor.execute("SELECT * FROM \"Project\".hotel") #join room to 
        print("| Avaliable Rooms by Number:         |")
        printQuery(cursor.fetchall())

def cBook():
    n = input("Enter Room Number: \n")
    br = input("[1]: Booking\n[2]: Renting\nBooking or Renting?:\n")
    chk = input("When will you check in?: (YY-MM-DD)\n")
    occ = input("How many occupants?: \n")

    # *do some stuff*

def customer():
    print("+--------------------------+")
    print("1: Search Avaliable Rooms")
    print("2: Book a Room")
    print("+--------------------------+")
    x = input("[ ]:")
    if x == "1":

        cSearch() #a and b take as args 
    elif x == "2":
        cBook()

def employee():
        print("Avaliable Rooms: ")
        cursor.execute("SELECT room_num FROM \"Project\".Room")
        print(cursor.fetchall())

def admin():
    while True:
        cursor.execute(input()) #try-catch statement here
        print(cursor.fetchall())




title()
# close connection
con.close()
