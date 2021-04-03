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
        cursor.execute("SELECT * FROM \"Project\".room WHERE \"Project\".room.is_booked = FALSE") #join room to 
        print("| Available Rooms by Number:         |")
        z = cursor.fetchall()
        n=10
        l=0
        loop = True
        print("+-----------+")
        while loop:
            if len(z) < n+l:
                n = len(z)
            for i in range(l,n+l):
                x = [z[i][0],z[i][2]]
                print("Room Number: "+str(x[0]))
                print("Price: $"+str(x[1]))
                print("+-----------+")
            print("For more information on a room, enter its room number. to see more rooms, press E. To go back, press Q")
            inp = input("[ ]: ")
            if inp == "E":
                l += 10
            elif inp == "Q":
                l -= 10
            else:
                room = int(inp)
                cursor.execute("SELECT * FROM \"Project\".room WHERE \"Project\".room.room_num = \'"+inp+"\'")
                g = cursor.fetchall()
                print("Room Number: "+str(g[0][0]))
                print("Is Booked: "+str(g[0][1]))
                print("Price: $"+str(g[0][2]))
                print("Has TV: "+str(g[0][3]))
                print("Has AC: "+str(g[0][4]))
                print("Room Capacity: "+str(g[0][5]))
                print("View Rating: "+str(g[0][6]))
                print("Can Extend: "+str(g[0][7]))
                customer()

def cBook():
    n = input("Enter Room Number: \n")
    br = "booking"
    chk = input("When will you check in?: (YYYY-MM-DD)\n")
    dur = input("How long will you stay?: \n")
    occ = input("How many occupants?: \n")
    nam = input("What is your name?: \n")
    cursor.execute("SELECT is_booked,room_cap FROM \"Project\".room WHERE \"Project\".room.room_num = \'"+n+"\'")
    temp = cursor.fetchall()
    a = temp[0][0] #avaliable or not
    b = temp[0][1] #max number of occupants
    if not a:
        if int(occ) > b:
            print("Too many people!")
        else:
            cursor.execute("INSERT INTO \"Project\"."+br+" (room_num,check_in_date,stay_duration_days,num_ppl,occupant) VALUES ("+n+",\'"+chk+"\',"+dur+","+occ+",\'"+nam+"\')")
            cursor.execute("UPDATE \"Project\".room SET is_booked = true WHERE \"Project\".room.room_num = \'"+n+"\'")
            con.commit()
    else:
        print("Room is not available!")

    # *do some stuff*

def customer():
    print("+--------------------------+")
    print("1: Search Available Rooms")
    print("2: Book a Room")
    print("+--------------------------+")
    x = input("[ ]:")
    if x == "1":
        cSearch() 
    elif x == "2":
        cBook()

def toRenting():
    n = input("Enter Room Number:\n[ ]: " )
    j = input("Credit Card Number:\n[ ]: ")
    cursor.execute("SELECT * FROM \"Project\".booking WHERE \"Project\".booking.room_num = \'"+n+"\'")
    data = cursor.fetchall()[0]
    chk = data[1]
    dur = data[2]
    occ = data[3]
    nam = data[4]
    cursor.execute("INSERT INTO \"Project\".renting (room_num,check_in_date,stay_duration_days,num_ppl,occupant) VALUES ("+str(n)+",\'"+str(chk)+"\',"+str(dur)+","+str(occ)+",\'"+nam+"\') ")
    #con.commit()
    employee()

def newRent():
    n = input("Enter Room Number:\n[ ]: " )
    j = input("Credit Card Number:\n[ ]: ")
    cursor.execute("SELECT * FROM \"Project\".room WHERE \"Project\".room.room_num = \'"+n+"\'")
    data = cursor.fetchall()[0]
    chk = data[1]
    dur = data[2]
    occ = data[3]
    nam = data[4]
    cursor.execute("INSERT INTO \"Project\".renting (room_num,check_in_date,stay_duration_days,num_ppl,occupant) VALUES ("+str(n)+",\'"+str(chk)+"\',"+str(dur)+","+str(occ)+",\'"+nam+"\') ")
    #con.commit()
    employee()


def employee():
    print("[1]: View Rooms Available")
    print("[2]: View Bookings")
    print("[3]: Booking to Renting")
    print("[4]: New Renting")
    z = input("[ ]: ")
    if z == "3":
        toRenting()
    elif z == "1":
        print("Avaliable Rooms by room num: ")
        cursor.execute("SELECT room_num FROM \"Project\".room WHERE \"Project\".room.is_booked = FALSE")
        for n in cursor.fetchall():
            print(n[0])
        employee()
    elif z == "2":
        print("Current Rooms booked by room num: ")
        cursor.execute("SELECT room_num FROM \"Project\".booking")
        for n in cursor.fetchall():
            print(n[0])
        employee()
    elif z == "4":
        
        #print(cursor.fetchall())
    
    
    #print(cursor.fetchall())

def admin():
    while True:
        cursor.execute(input()) #try-catch statement here
        print(cursor.fetchall())




title()
# close connection
con.close()
