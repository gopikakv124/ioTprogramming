>>> import pymysql
>>> conn =pymysql.connect(database="USERS",user="gopikakv",password="assignment2",host="localhost")
>>> cur=conn.cursor()
>>> name = "anu"
>>> age=20
>>> city="thrissur"
>>> state="kerala"
>>> data={'username':name,'userage':age,'usercity':city,'userstate':state}
>>> print(data)
>>> cur.execute("INSERT INTO userdata (username,userage,usercity,userstate) VALUES (%(username)s,%(userage)s,%(usercity)s,%(userstate)s);",data)
>>> conn.commit()
>>> print("saved to db")
>>> cur.execute("SELECT * FROM userdata;")
>>> data1=cur.fetchone()
>>> data2=cur.fetchall()
>>> print(data1)
>>> print(data2)