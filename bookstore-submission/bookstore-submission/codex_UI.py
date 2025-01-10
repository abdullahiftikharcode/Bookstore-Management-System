import os
from codex_users import Users
def displaymenu(bookstore):
 sym="█"
 os.system('cls' if os.name == 'nt' else 'clear')
 print(".______     ______     ______    __  ___         _______.___________.  ______   .______       _______    ")
 print("|   _  \\   /  __  \\   /  __  \\  |  |/  /        /       |           | /  __  \\  |   _  \\     |   ____|   ")
 print("|  |_)  | |  |  |  | |  |  |  | |  '  /        |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__      ")
 print("|   _  <  |  |  |  | |  |  |  | |    <          \\   \\       |  |     |  |  |  | |      /     |   __|     ")
 print("|  |_)  | |  `--'  | |  `--'  | |  .  \\     .----)   |      |  |     |  `--'  | |  |\\  \\----.|  |____    ")
 print("|______/   \\______/   \\______/  |__|\\__\\    |_______/       |__|      \\______/  | _| `._____||_______|   ")
 print("                                                                                                        ")
 print("  " + sym*29)
 print("  "+ sym + "      BOOKSTORE MENU       " + sym)
 print("  " + sym*29)
 print("  " + sym + " 1. Add New Book           " + sym)
 print("  " + sym + " 2. Add New Customer       " + sym)
 print("  " + sym + " 3. Add New Author         " + sym)
 print("  " + sym + " 4. Add New Sale           " + sym)
 print("  " + sym + " 5. Available authors      " + sym)
 print("  " + sym + " 6. Available books        " + sym)
 print("  " + sym + " 7. Available customers    " + sym)
 print("  " + sym + " 8. Report(SUB MENU)       " + sym)
 print("  " + sym + " 9. Add new user           " + sym)
 print("  " + sym + " 10. Chatbot               " + sym)
 print("  " + sym + " 11. Display attendance    " + sym)
 print("  " + sym + " 0. Exit                   " + sym)
 print("  " + sym*29 + "\n\n")
def exitpro():
 os.system('cls' if os.name == 'nt' else 'clear')
 print(" ____                        __  __                          __  __                          ")
 print("/\  _`\                     /\ \/\ \                        /\ \/\ \                         ")
 print("\ \ \L\_\    ___     ___    \_\ \ \ \____  __  __     __    \ \ \ \ \    ____     __   _ __  ")
 print(" \ \ \L_L   / __`\  / __`\  /'_` \ \ '__`\/\ \/\ \  /'__`\   \ \ \ \ \  /',__\  /'__`\/\`'__\\")
 print("  \ \ \/, \/\ \L\ \/\ \L\ \/\ \L\ \ \ \L\ \ \ \_\ \/\  __/    \ \ \_\ \/\__, `\/\  __/\ \ \/ ")
 print("   \ \____/\ \____/\ \____/\ \___,_\ \_,__/\/`____ \ \____\    \ \_____\/\____/\ \____\\ \_\ ")
 print("    \/___/  \/___/  \/___/  \/__,_ /\/___/  `/___/> \/____/     \/_____/\/___/  \/____/ \/_/ ")
 print("                                               /\___/                                         ")
 print("                                               \/__/                                          ")
def addbook(bookstore):
 print("------------------------")
 print("|  ADDING NEW BOOK      |")
 print("------------------------")
 title = input("Enter book title: ")
 printAuthors(bookstore,False)
 while True:
        authorid = int(input("Enter Author ID: "))
        if authorid > len(bookstore.getallAuthors()):
            raise ValueError("Invalid Author ID")
        else:
         break
 publisher = input("Enter Publisher name: ")
 price = float(input("Enter Price of Book: "))
 edition = int(input("Enter Edition of Book: "))
 year= float(input("Enter Year of Book: "))
 bookstore.addnewbook(title,authorid,price,year,edition,publisher)
 print("PRESS ENTER TO RETURN TO MENU...")
 input() 
def addcustomer(bookstore):
 print("------------------------")
 print("|  ADDING NEW CUSTOMER  |")
 print("------------------------")
 name = input("Enter  customer name: ")
 email = input("Enter email adress: ")
 adress = input("Enter customer adress: ")
 phonenumber = input("Enter customer phone number: ")
 bookstore.addnewcustomer(name,email,adress,phonenumber)
 print("PRESS ENTER TO RETURN TO MENU...")
 input() 
def addsale(bookstore):
 print("------------------------")
 print("|  ADDING NEW SALES     |")
 print("------------------------")
 printbooks(bookstore,False)
 while True:
        bookid = int(input("Enter BOOK ID: "))
        if bookid > len(bookstore.getallBooks()):
            raise ValueError("Invalid BOOK ID")
        else:
         break
 printcustomers(bookstore,False)   
 while True:
        customerid = int(input("Enter Customer ID: "))
        if customerid > len(bookstore.getallCustomers()):
            raise ValueError("Invalid customer ID")
        else: 
         break
 orderdate = input("Enter Order date of sale: ")
 discount = float(input("Enter discount on sale: "))
 total = float(input("Enter total of Sale: "))
 bookstore.addnewsales(orderdate,customerid,bookid,discount,total)
 print("PRESS ENTER TO RETURN TO MENU...")
 input() 
def addauthor(bookstore):
 print("------------------------")
 print("|   ADDING NEW Author   |")
 print("------------------------")
 name = input("Enter  author name: ")
 gender = input("Enter authors gender: ")
 email = (input("Enter authors email: "))
 adress = (input("Enter authors adress: "))
 phonenumber = (input("Enter authors phonenumber: "))
 genre = (input("Enter authors genre: "))
 bookstore.addnewauthors(name,gender,email,genre,adress,phonenumber)
 print("PRESS ENTER TO RETURN TO MENU...")
 input()
def printAuthors(bookstore,g):
 authors = bookstore.getallAuthors()
 print("------------------------")
 print("|  Authors Available   |")
 print("------------------------")
 print("Author ID |    Author name ")

 for author_id, author_name in authors:
    print(f"{author_id}         |   {author_name}")
 if g:
    print("PRESS ENTER TO RETURN TO MENU...")
    input()
def printbooks(bookstore,g):
 authors = bookstore.getallBooks()
 print("------------------------")
 print("|   Books Available    |")
 print("------------------------")
 print(" Book ID |    Book title ")

 for book_id, booktitle in authors:
    print(f"{book_id}        |   {booktitle}")
 if g:
    print("PRESS ENTER TO RETURN TO MENU...")
    input()
def printcustomers(bookstore,g):
 authors = bookstore.getallCustomers()
 print("------------------------")
 print("| Customers Available   |")
 print("------------------------")
 print("Customer ID|    Customer name ")

 for customer_id, customername in authors:
    print(f"{customer_id}          |   {customername}")
 if g:
    print("PRESS ENTER TO RETURN TO MENU...")
    input()
def startconversation (bookstore):
    bookstore.startconversation()
def addnewuser(bookstore):
  
 if bookstore.get_authority() == 0:
    print("------------------------")
    print("|  ADDING NEW USER      |")
    print("------------------------")
    username = input("Enter user name :")
    password = input("Enter user password :")
    print("SELECT ROLE")
    print("1. Admin")
    print("2. Manager")
    print("3. Staff")
    while True:
        role=int(input("Enter user role :"))
        if role == 1:
            role=0
            break
        elif role == 2:
            role=1
            break
        elif role == 3:
            role=2
            break
    print("NOW ADDING IMAGE...WAIT PATIENTLY...")
    bookstore.addnewuser(username,password,role,None,None)
 else:
    print("ONLY ADMIN CAN CREATE A NEW ROLE .....")
 print("PRESS ENTER TO RETURN TO MENU...", end=" ")
 input()
def withpassword(bookstore):
    username, password = "", ""
    while True:
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            role=3
            image=None
            currentuser=Users(username,password,role,None,image)
            bookstore.setuser(currentuser)
            if bookstore.db.authenticate_user_record(currentuser,role):
                print("WRONG USERNAME AND PASSWORD...")
                print("ENTER CORRECT INFO AGAIN...")
            else:
                bookstore.setuser(currentuser)
                return False
               
def withface(bookstore):
    return bookstore.matchface()
def attending(bookstore):
    return bookstore.attending()
def displayattendance(bookstore):
    bookstore.attendancedisplay()
def authenticate_user(bookstore):
   while True: 
    sym="█"
    os.system("cls" if os.name == "nt" else "clear")
    print(".______     ______     ______    __  ___         _______.___________.  ______   .______       _______    ")
    print("|   _  \\   /  __  \\   /  __  \\  |  |/  /        /       |           | /  __  \\  |   _  \\     |   ____|   ")
    print("|  |_)  | |  |  |  | |  |  |  | |  '  /        |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__      ")
    print("|   _  <  |  |  |  | |  |  |  | |    <          \\   \\       |  |     |  |  |  | |      /     |   __|     ")
    print("|  |_)  | |  `--'  | |  `--'  | |  .  \\     .----)   |      |  |     |  `--'  | |  |\\  \\----.|  |____    ")
    print("|______/   \\______/   \\______/  |__|\\__\\    |_______/       |__|      \\______/  | _| `._____||_______|   ")
    print()
    if bookstore.db.no_users_table(bookstore.currentuser) != 0:
        choice =0
        print("  " + sym * 33)
        print("  " + sym + "      USER AUTHENTICATION      " + sym)
        print("  " + sym * 33)
        print(f"  {sym} 1.Enter using password        {sym}")
        print(f"  {sym} 2.Enter using faceid          {sym}")
        print(f"  {sym} 3.Mark Attendance             {sym}")
        print(f"  {sym * 33}\n")
        choice=int(input("Enter your choice : "))
        match choice:
          case 1:
             if withpassword(bookstore)==False:
                break
          case 2:
             if withface(bookstore)==False:
                break
          case 3:
              attending(bookstore)
    else:
        print("NO USER EXISTS IN USER TABLE, CREATE NEW USER")
        addnewuser(bookstore)
        authenticate_user(bookstore)
        break;
def salesreportsubmenu():
    sym = "█"
    os.system("cls")
    print(".______     ______     ______    __  ___         _______.___________.  ______   .______       _______    ")
    print("|   _  \\   /  __  \\   /  __  \\  |  |/  /        /       |           | /  __  \\  |   _  \\     |   ____|   ")
    print("|  |_)  | |  |  |  | |  |  |  | |  '  /        |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__      ")
    print("|   _  <  |  |  |  | |  |  |  | |    <          \\   \\       |  |     |  |  |  | |      /     |   __|     ")
    print("|  |_)  | |  `--'  | |  `--'  | |  .  \\     .----)   |      |  |     |  `--'  | |  |\\  \\----.|  |____    ")
    print("|______/   \\______/   \\______/  |__|\\__\\    |_______/       |__|      \\______/  | _| `._____||_______|   ")
    print("                                                                                                        ")
    print(f"  {sym * 29}")
    print(f"  {sym}       REPORTS SUB-MENU    {sym}")
    print(f"  {sym * 29}")
    print(f"  {sym} 1.SALES REPORT ON BOOKID  {sym}")
    print(f"  {sym} 2.SALES REPORT ON AuthorID{sym}")
    print(f"  {sym} 3.Get Books ON AuthorID   {sym}")
    print(f"  {sym} 4.TOP 3 SALES ON BOOK     {sym}")
    print(f"  {sym} 5.TOP 3 SALES ON AUTHOR   {sym}")
    print(f"  {sym} 0. RETURN TO MAIN-MENU    {sym}")
    print(f"  {sym * 29}\n")
def getsalesreportbookid(bookstore):
   printbooks(bookstore, False)
   id = input("Book ID : ")
   sales = bookstore.getSalesOfBook(id)
   print( "   -------------------------------")
   print(f"   |  SALES REPORT By Book ID:{id}  |")
   print( "   -------------------------------")
   headers = ["SalesId", "OrderDate", "CustomerId", "BooksId", "Discount", "Total"]
   header_line = "{:<10} | {:<10} | {:<10} | {:<7} | {:<8} | {:<6}".format(*headers)
   print(header_line)
   print("-" * len(header_line))
   for SalesId, Orderdate, CustomerId, BooksId, Discount, Total in sales:
    print("{:<10} | {:<10} | {:<10} | {:<7} | {:<8} | {:<6}".format(
            SalesId, Orderdate, CustomerId, BooksId, Discount, Total
        ))
   print("PRESS ENTER TO RETURN TO MENU...")
   input()
def getsalesreportauthorid(bookstore):
   printAuthors(bookstore, False)
   id = input("Author ID : ")
   sales = bookstore.getSalesOfAuthor(id)
   print("   -------------------------------")
   print(f"   |  SALES REPORT By Author id:{id}|")
   print("   -------------------------------")
   headers = ["SalesId", "OrderDate", "CustomerId", "BooksId", "Discount", "Total"]
   header_line = "{:<10} | {:<10} | {:<10} | {:<7} | {:<8} | {:<6}".format(*headers)
   print(header_line)
   print("-" * len(header_line))
   for SalesId, Orderdate, CustomerId, BooksId, Discount, Total in sales:
    print("{:<10} | {:<10} | {:<10} | {:<7} | {:<8} | {:<6}".format(
            SalesId, Orderdate, CustomerId, BooksId, Discount, Total
        ))
   print("PRESS ENTER TO RETURN TO MENU...")
   input()
def getbooksreportauthorid(bookstore):
   printAuthors(bookstore, False)
   id = input("Author ID : ")
   books = bookstore.getBooksOfAuthor(id)
   print("    -----------------------")
   print(f"   |  BOOKS BY Author ID {id} |")
   print("    -----------------------")
   headers = ["BookId", "Title", "AuthorId", "Price", "Year", "Edition", "Publisher"]
   header_line = "{:<8} | {:<20} | {:<9} | {:<6} | {:<4} | {:<7} | {:<15}".format(*headers)
   print(header_line)
   print("-" * len(header_line))
   for BookId, Title, AuthorId,Price,Year,Edition, Publisher in books:
    print("{:<8} | {:<20} | {:<9} | {:<6} | {:<4} | {:<7} | {:<15}".format(
            BookId, Title, AuthorId, Price, Year, Edition, Publisher
        ))
   print("PRESS ENTER TO RETURN TO MENU...")
   input()
def top3Books(bookstore):
   books = bookstore.getTopBooks()
   print("   -------------")
   print("   | Top BOOKS  |")
   print("   -------------")
   headers = ["BookId", "Title", "Total Sales"]
   header_line = "{:<7} | {:<20} | {:<11}".format(*headers)
   print(header_line)
   print("-" * len(header_line))
   for BookId, Title, Total_Sales in books:
    print("{:<7} | {:<20} | {:<11}".format(BookId, Title, Total_Sales))
   print("PRESS ENTER TO RETURN TO MENU...")
   input()
def top3Authors(bookstore):
   authors = bookstore.getTopAuthors()
   print("   ----------------")
   print("   |  Top authors |")
   print("   ----------------")
   headers = ["AuthorId", "Name", "Total Sales"]
   header_line = "{:<8} | {:<20} | {:<11}".format(*headers)
   print(header_line)
   print("-" * len(header_line))
   for AuthorId, Name, Total_Sales in authors:
     print("{:<8} | {:<20} | {:<11}".format(AuthorId, Name, Total_Sales))
   print("PRESS ENTER TO RETURN TO MENU...")
   input()
def menu(bookstore):
    authenticate_user(bookstore)
    while True: 
       displaymenu(bookstore)
       choice=0
       subchoice=0
       choice=int (input("Enter your choice : "))
       match choice:
        case 1:
          addbook(bookstore)
        case 2:
           addcustomer(bookstore)
        case 3: 
           addauthor(bookstore)
        case 4:
            addsale(bookstore)
        case 5:
            printAuthors(bookstore,True)
        case 6:
            printbooks(bookstore,True)
        case 7:
            printcustomers(bookstore,True)
        case 8:
            while True:
             salesreportsubmenu()
             subchoice = int(input("Enter your choice: "))
             match subchoice:
              case 1:
               getsalesreportbookid(bookstore)
              case 2:
               getsalesreportauthorid(bookstore)
              case 3:
               getbooksreportauthorid(bookstore) 
              case 4:
               top3Books(bookstore)
              case 5:
               top3Authors(bookstore)
              case 0:
                  break 
        case 9:
             addnewuser(bookstore)
        case 10:
            startconversation(bookstore) 
        case 11:
            displayattendance(bookstore) 
        case 0:
            exitpro()
            break 
        
       
