import psycopg2

# connect to db
con = psycopg2.connect(
    host = "web0.eecs.uottawa.ca",
    database = "group_a03_g04",
    user="", # uottawa email without @uottawa.ca
    # remove next line
    password ="",# remove this REMMBER!!!!!!!!!  password of uottawa email REMEMBER TO REMOVE WHEN PUSHING
    # remove remove remove 
    port="15432"
)


# close connectio                                       n
con.close()