from codex_database import Database
from codex_Book import Book
from codex_Sale import Sale
from codex_Author import Author
from codex_Customer import Customer
from codex_chatbot import Chatbot
from codex_users import Users
class Bookstore:
   def __init__(self, dbPath): 
     self.db=Database(dbPath)
     self.currentuser=Users("22","33",4,None,0)
   def addnewbook(self,title,authorid,price,year,edition,publisher):
      book=Book(title,authorid,price,year,edition,publisher)
      self.db.addnewbook(book)
   def addnewcustomer(self,name,email,adress,phonenumber):
      customer=Customer(name,email,adress,phonenumber)
      self.db.addnewcustomer(customer)
   def addnewsales(self,orderdate,customerid,bookid,discount,total):
      sales=Sale(orderdate,customerid,bookid,discount,total)
      self.db.addnewsales(sales)
   def addnewauthors(self,name,gender,email,genre,adress,phonenumber):
      author=Author(name,gender,email,genre,adress,phonenumber)
      self.db.addnewauthors(author)
   def addnewuser(self,username,password,role,image,userid):
      user=Users(username,password,role,image,userid)
      self.db.addnewuser(user)
   def getallAuthors(self):
      return self.db.getallauthors()
   def getallBooks(self):
      return self.db.getallbooks()
   def getallCustomers(self):
      return self.db.getallcustomers()
   def setuser(self,user):
      self.currentuser=user
   def get_authority(self):
       return self.currentuser.get_authority()
   def matchface(self):
        return self.db.facematched(self.currentuser)
   def attending(self):
        return self.db.addnewattendance()
   def attendancedisplay(self):
        self.db.attedancelist()
   def startconversation(self):
      mychatbot=Chatbot()
      user_input=str(input("YOU : "))
      response=mychatbot.startchat(user_input)
      print("CHATBOT :",response)
      while True:
       user_input=str(input("YOU : "))
       if user_input.lower()=="quit":
          break
       response=mychatbot.continuechat(user_input)
       print("CHATBOT :",response)
   def getSalesOfBook(self, id):
      return self.db.sales_on_book(id)
   def getSalesOfAuthor(self, id):
      return self.db.sales_on_author(id)
   def getBooksOfAuthor(self, id):
      return self.db.books_on_author(id)
   def getTopBooks(self):
      return self.db.top_3_books()
   def getTopAuthors(self):
      return self.db.top_3_authors()
       
       
      
        
   



