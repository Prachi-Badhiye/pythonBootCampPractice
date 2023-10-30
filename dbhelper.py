import mysql.connector 
class DBHelper:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',
                                         port='3306',
                                         user='root', 
                                         password='root',
                                         database='test4')        
        query = 'create table if not exists collage(collageId int primary key,collageName varchar(100),location varchar(50))'
        mycur=self.con.cursor()
        mycur.execute(query)
       # mycur.execute("create table")
        print("table is Created")

    #insert data
    def insert_collage(self, collageId, collageName, location):
        query = "insert into collage(collageId, collageName, location) values ({},'{}','{}')".format(collageId,collageName,location)
        # print(query)
        mycur=self.con.cursor()
        mycur.execute(query)
        self.con.commit()
        print("data saved to table")

    #Fetch all data
    def fetch_all(self):
        query='select * from collage'
        mycur=self.con.cursor()
        mycur.execute(query)
        for row in mycur:
            print("collage Id:",row[0])
            print("collage Name:",row[1])
            print("collage Location:",row[2])
            print()
            print()

    #Delete collage info
    def delete_collage(self,collageId):
        query='delete from collage where collageId={}'.format(collageId)
        # print(query)
        mycur=self.con.cursor()
        mycur.execute(query)
        self.con.commit()
        print("Data deleted")

    #update the collage
    def update_collage(self, collageId, newname, newlocation):
        query = "update collage set collageName='{}', location='{}' where collageId={}".format(newname, newlocation, collageId)
        mycur = self.con.cursor()
        mycur.execute(query)
        self.con.commit()
        print("Data updated")