import psycopg2
f = open("cred.txt","r")
uname = f.readline()
upass = f.readline()
uname = uname[0:len(uname)-1]
upass = upass[0:len(upass)-1]
# connect to db
con = psycopg2.connect(
    host = "web0.eecs.uottawa.ca",
    database = "group_a03_g04",
    user=uname, 
    password =upass,
    port="15432"
)

cursor = con.cursor()



def title(): #main menu. admin and employee should prolly get prompted for passwords n stuff
    title= "+------------------------------------+\n|                                    |\n|                                    |\n|                                    |\n|                                    |\n| [A]: Customer                      |\n| [B]: Employee                      |\n| [C]: Admin                         |\n|                                    |\n|                                    |\n+------------------------------------+"
    print(title)
    x = input()
    if x == "A":
        customer()
    elif x == "B":
        employee()
    elif x == "C":
        admin()

def cSearch(): #this will later take as input the date n stuff. db as is now is empty so idk what to do with them
        print("| Avaliable Rooms by Number:         |")
        cursor.execute("SELECT room_num FROM \"Project\".Room")
        print(cursor.fetchall())

def cBook():
    n = input("Enter Room Number: ")
    # *do some stuff*

def customer():
    print("1: Search Avaliable Rooms")
    print("2: Book a Room")
    x = input()
    if x == "1":
        a = input("Before/Exactly/After (B/E/A): ")
        b = input("Date: (YY-MM-DD)")
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
