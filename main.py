from dbhelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("**********WELCOME*************")
        print()
        print("Press 1. To insert Collage Information")
        print("Press 2. To display all Collage Information")
        print("Press 3. To delete the Collage Information")
        print("Press 4. To update the Collage Information")
        print("Press 5. To exit the program")
        print()
        try:
            choice=int(input())
            if(choice==1):
            #insert data
               cid = int(input("Enter College Id:"))
               cname = input("Enter College Name:")
               location = input("Enter location:")
               db.insert_collage(cid, cname, location)
            elif(choice==2):
                #display collage information
                db.fetch_all()
            elif(choice==3):
                #delete collage information
                bid=int(input("Enter collage Id which you want to delete:"))
                db.delete_collage(cid)
            elif(choice==4):
                #update collage data
                cid=int(input("Enter collage Id you want to update:"))
                cname=input("Enter New collage Name:")
                location=input("Enter New location:")
                db.update_collage(cid,cname,location)
            elif(choice==5):
                pass
                break
            else:
                print("Invalid input!!! Try again")
        except Exception as e:
            print(e)
            print("Invalid detail!! Try again")

    
if __name__=="__main__":
    main()


#main coding
# helper = DBHelper()
# # helper.insert_CollegeInfo(101,"sinhgad", "katraj")
# # helper.insert_CollegeInfo(102,"jspm","wagholi")
# # helper.insert_CollegeInfo(103,"symbosis", "vimannager")
# #helper.delete_CollageData(103)
# helper.update_CollageData(102,"jspm2","nigdi")
# helper.fetch_all()





