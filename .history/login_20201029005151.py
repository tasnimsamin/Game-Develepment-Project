
import mysql.connector
import cgi

form = cgi.FieldStorage()

first_name=form.getvalue("first_name")   
last_name = form.getvalue("last_name")  
email	= form.getvalue("email")
new_pass=form.getvalue("email")
con_pass=



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login"
)

mycursor = mydb.cursor()

sql = "INSERT INTO reg_tb (name, email, pass) VALUES (%s, %s, %s)"
val = (n, e, p)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount, "record inserted.")