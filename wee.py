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


# close connectio                                       n
con.close()
