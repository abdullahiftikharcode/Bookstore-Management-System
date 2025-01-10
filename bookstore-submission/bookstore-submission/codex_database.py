import sqlite3
import cv2
import dlib
import time
import numpy as np
from codex_Book import Book
from codex_Sale import Sale
from codex_Author import Author
from codex_Customer import Customer
from codex_users import Users
from codex_mark import attendance
from datetime import datetime
class Database:
   
   def __init__(self, dbPath): 
    self.shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    self.face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
    self.conn = sqlite3.connect(dbPath)   
    self.cur = self.conn.cursor()  
    self.create_tables()
   def create_tables(self):
    self.cereate_books_table()
    self.cereate_customer_table()
    self.cereate_auhtors_table()
    self.cereate_sales_table()
    self.cereate_users_table()
    self.cereate_attendance_table()
    self.conn.commit()
   def cereate_attendance_table(self):
     self.cur.execute('''CREATE TABLE IF NOT EXISTS Attendance (
                     AttendanceId INTEGER PRIMARY KEY AUTOINCREMENT,
                     Userid TEXT,
                     Date TEXT
                     )''')
   def cereate_books_table(self):
     self.cur.execute('''CREATE TABLE IF NOT EXISTS Books (
                     BookId INTEGER PRIMARY KEY AUTOINCREMENT,
                     Title TEXT,
                     AuthorId INTEGER, 
                     Price INTEGER, 
                     Edition INTEGER, 
                     Year INTEGER,
                     Publisher TEXT 
                     )''')
   def cereate_customer_table(self):
     self.cur.execute('''CREATE TABLE IF NOT EXISTS Customers (
     CustomerId INTEGER PRIMARY KEY AUTOINCREMENT,
     Name TEXT,
     Email TEXT,
     Address TEXT,
     PhoneNumber TEXT)''')
   def cereate_auhtors_table(self):
      self.cur.execute('''CREATE TABLE IF NOT EXISTS Authors (
     AuthorId INTEGER PRIMARY KEY AUTOINCREMENT,
     Name TEXT,
     Gender TEXT,
     Email TEXT,
     GENRE TEXT,
     PhoneNumber TEXT,
     Address TEXT)''')
   def cereate_sales_table(self):
      self.cur.execute('''CREATE TABLE IF NOT EXISTS Sales (
     SalesId INTEGER PRIMARY KEY AUTOINCREMENT,
     Orderdate TEXT,
     CustomerId INT,
     BooksId INT,
     Discount FLOAT,
     Total FLOAT)''')
   def cereate_users_table(self):
      self.cur.execute('''CREATE TABLE IF NOT EXISTS Users (
     UsersId INTEGER PRIMARY KEY AUTOINCREMENT,
     Username TEXT,
     Password INT,                  
     Role INT,
     Image BLOB)''')
   def addnewbook(self,book):
    try:
         self.cur.execute("INSERT INTO Books (Title, AuthorId,Price,Year,Edition, Publisher) VALUES (?, ?, ?, ?,?,?)", (book.get_title(), book.get_authorid(),book.get_price(), book.get_year(),book.get_edition(),book.get_publisher()))
         self.conn.commit()
         print("BOOK HAS BEEN SAVED .....")
         return 0 
    except sqlite3.Error as e:
     print("Error adding book:", e)
     return 1
   def addnewcustomer(self, customer):
    try:
        self.cur.execute("INSERT INTO Customers (Name, Email, Address, Phonenumber) VALUES (?, ?, ?, ?)", (customer.get_name(), customer.get_email(), customer.get_address(), customer.get_phonenumber()))
        self.conn.commit()
        print("CUSTOMER HAS BEEN SAVED .....")
        return 0 
    except sqlite3.Error as e:
        print("Error adding customer:", e)
        return 1
   def addnewsales(self,sales):
    try:
         self.cur.execute("INSERT INTO Sales ( Orderdate,CustomerId,BooksId,Discount,Total ) VALUES (?, ?, ?, ?,?)", (sales.get_orderdate(), sales.get_customerid(),sales.get_bookid(), sales.get_discount(),sales.get_total()))
         self.conn.commit()
         print("Sales HAS BEEN SAVED .....")
         return 0 
    except sqlite3.Error as e:
     print("Error adding sales:", e)
     return 1
   def addnewattendance(self):
    try:
         currentuser=Users("22","33",4,None,0) 
         currentdate=datetime.now()
         self.facematched(currentuser)
         attend =attendance(currentuser.get_userid(),currentdate.strftime("%Y-%m-%d"))
         self.cur.execute("SELECT * FROM Attendance WHERE Userid = ? AND Date = ?", (currentuser.get_userid(), currentdate.strftime("%Y-%m-%d")))
         existing_attendance = self.cur.fetchone()
         if not(existing_attendance):
          self.cur.execute("INSERT INTO Attendance ( Userid,Date ) VALUES (?, ?)", (attend.getuserid(),attend.getdate()))
          print(f"Marked attendance for {currentuser.get_username()}")
         else: 
           print(f"ATTENDANCE HAS ALREADY BEEN MARKED FOR {currentuser.get_username()}.....") 
         self.conn.commit()
         input("PRESS ENTER TO RETURN....")
         return 0 
    except sqlite3.Error as e:
     print("Error adding sales:", e)
     return 1
   def detect_faces(self,image):
    self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)
    return self.faces, self.gray
   def addnewauthors(self,author):
    try:
         self.cur.execute("INSERT INTO Authors (Name,Gender,Email,GENRE,PhoneNumber,Address) VALUES (?, ?, ?, ?,?,?)", (author.get_name(), author.get_gender(),author.get_email(), author.get_genre(),author.get_phonenumber(),author.get_address()))
         self.conn.commit()
         print("Author HAS BEEN SAVED .....")
         return 0 
    except sqlite3.Error as e:
     print("Error adding autors:", e)
     return 1
   def addnewuser(self, user):
        try:
            cap = cv2.VideoCapture(0)
            cv2.namedWindow("User Video", cv2.WINDOW_NORMAL)
            while True:
                ret, frame = cap.read()
                frame=cv2.flip(frame,1)
                if ret:
                    faces, _ = self.detect_faces(frame)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        face_roi = frame[y:y+h, x:x+w]
                        _, img_encoded = cv2.imencode('.jpg', face_roi)
                        cv2.imshow("User Video", frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                           break
                        if len(faces) == 1: 
                            image_data = img_encoded.tobytes()
                            cv2.putText(frame, "Adding face for: " + user.get_username(), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            self.cur.execute("INSERT INTO Users (Username, Password, Role, Image) VALUES (?, ?, ?, ?)",
                                            (user.get_username(), user.get_password(), user.get_authority(), image_data))
                            self.conn.commit()
                            print("CONGRATULATIONS... FACE ADDED SUCCESFULLY")
                            start_time = time.time()
                            while time.time() - start_time < 7:
                             ret, frame = cap.read()
                             frame=cv2.flip(frame,1)
                             if ret:
                              faces, _ = self.detect_faces(frame)
                              for (x, y, w, h) in faces:
                               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                               cv2.imshow("User Video", frame)
                               if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                             cap.release()
                             cv2.destroyAllWindows()
                             return 0
        except sqlite3.Error as e:
            print("Error adding users:", e)
            return 1

   def getallauthors(self):
        authors = []
        try:
          self.cur.execute("SELECT AuthorId, Name FROM Authors")
          rows = self.cur.fetchall()
          for row in rows:
                author_id, name = row
                authors.append((author_id, name))
          return authors
        except sqlite3.Error as e:
            print("Error getting authors:", e)
            return 1
   def getallcustomers(self):
        customers = []
        try:
          self.cur.execute("SELECT CustomerId, Name FROM Customers")
          rows = self.cur.fetchall()
          for row in rows:
                customer_id, name = row
                customers.append((customer_id, name))
          return customers
        except sqlite3.Error as e:
            print("Error getting customers:", e)
            return 1  
   def getallbooks(self):
      books = []
      try:
          self.cur.execute("SELECT BookId, Title FROM Books")
          rows = self.cur.fetchall()
          for row in rows:
                book_id, name = row
                books.append((book_id, name))
          return books
      except sqlite3.Error as e:
            print("Error getting customers:", e)
            return 1  
   def no_users_table(self,currentuser):
        sql = "SELECT COUNT(*) FROM Users"
        self.cur.execute(sql)
        result = self.cur.fetchone()[0]
        if result==0:
           currentuser.set_authority(0)
        return result
   def authenticate_user_record(self, user,role1):
        sql = "SELECT * FROM Users WHERE Username = ? ;"
        self.cur.execute(sql, (user.get_username(),))
        rows = self.cur.fetchall()
        for row in rows:
            userId = row[0]
            db_username = row[1]
            db_password = row[2]
            role1 = row[3]
            if db_username == user.get_username() and db_password == user.get_password():
                user.set_authority(role1)
                return False
        return True
   def load_face_data(self):
        self.cur.execute("SELECT UsersId,Username, Password, Role, Image FROM Users")
        rows = self.cur.fetchall()
        face_data = []

        for row in rows:
            userid,username, password, role, image_data = row
            nparr = np.frombuffer(image_data, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            rgb_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            detector = dlib.get_frontal_face_detector()
            dlib_faces = detector(rgb_img)

            if len(dlib_faces) > 0:
                face_encoding = self.encode_face(rgb_img, dlib_faces[0])
                if face_encoding is not None:
                    face_data.append((username, password, role,userid, face_encoding))

        return face_data

   def encode_face(self, rgb_img, face):
        landmarks = self.shape_predictor(rgb_img, face)
        face_encoding = self.face_recognizer.compute_face_descriptor(rgb_img, landmarks)
        return face_encoding

   def facematched(self, user):
        cap = cv2.VideoCapture(0)
        
        face_data = self.load_face_data()
        cv2.namedWindow("User Video", cv2.WINDOW_NORMAL)
        detector = dlib.get_frontal_face_detector()
        while True:
            ret, frame = cap.read()
            frame=cv2.flip(frame,1)
            if not ret:
                break
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            dlib_faces = detector(rgb_frame)
            if len(dlib_faces)>0:
             for face in dlib_faces:
                face_encoding = self.encode_face(rgb_frame, face)
                for username, password, role,userid,known_face_encoding in face_data:
                    distance = np.linalg.norm(np.array(known_face_encoding) - np.array(face_encoding))
                    if distance < 0.4:
                        left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                        cv2.putText(frame, username, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                        user.set_username(username)
                        user.set_password(password)
                        user.set_authority(role)
                        user.set_userid(userid)
                        start_time = time.time()
                        while time.time() - start_time < 4:
                            ret, frame = cap.read()
                            frame=cv2.flip(frame,1)
                            if not ret:
                                break

                            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            dlib_faces = detector(rgb_frame)
                            if len(dlib_faces) > 0:
                                face = dlib_faces[0]
                                left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
                                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                                cv2.putText(frame, username, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                            cv2.imshow("User Video", frame)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                        cap.release()
                        cv2.destroyAllWindows()
                        return False
                else:
                    left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "User Not Recognized", (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    cv2.imshow("User Video", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                     break

            cv2.imshow("User Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return True
   def attedancelist(self):
       try:
        self.cur.execute("SELECT UsersId, Username FROM Users")
        rows = self.cur.fetchall()
        user_count = len(rows)
        for row in rows:
            user_id, username = row
            print(f"User ID: {user_id}, Username: {username}")
        k=0
        while k==0:
          userk=int(input("Enter the userid to fetch attendance for: "))
          if userk<=user_count:
             k=1
        self.cur.execute("SELECT Date FROM Attendance WHERE Userid = ?", (str(userk)))
        rows = self.cur.fetchall()
        print(f"Attendance for User ID {userk}:")
        for row in rows:
            print(f"Date: {row[0]}")
        input("PRESS ENTER TO EXIT")
       except sqlite3.Error as e:
        print("Error getting users:", e)
   def sales_on_book(self, id):
      sales = []
      try:
          sql = "SELECT Sales.* FROM Sales WHERE BooksId = ? ;"
          self.cur.execute(sql, id)
          rows = self.cur.fetchall()
          for row in rows:
                SalesId, Orderdate, CustomerId, BooksId, Discount, Total = row
                sales.append((SalesId, Orderdate, CustomerId, BooksId, Discount, Total))
          return sales
      except sqlite3.Error as e:
            print("Error getting sales report on book:", e)
   def sales_on_author(self, id):
      sales = []
      try:
          sql = "SELECT S.SalesId, S.Orderdate, S.CustomerId, S.BooksId, S.Discount, S.Total FROM Sales S JOIN Books B ON S.BooksId = B.BookId WHERE B.AuthorId = ? ;"
          self.cur.execute(sql, id)
          rows = self.cur.fetchall()
          for row in rows:
                SalesId, Orderdate, CustomerId, BooksId, Discount, Total = row
                sales.append((SalesId, Orderdate, CustomerId, BooksId, Discount, Total))
          return sales
      except sqlite3.Error as e:
            print("Error getting sales report on author:", e)
   def books_on_author(self, id):
      books = []
      try:
          sql = "SELECT Books.* FROM Books  WHERE AuthorId = ? ;"
          self.cur.execute(sql, id)
          rows = self.cur.fetchall()
          for row in rows:
                BookId, Title, AuthorId,Price,Year,Edition, Publisher = row
                books.append((BookId, Title, AuthorId,Price,Year,Edition, Publisher))
          return books
      except sqlite3.Error as e:
            print("Error getting books report on author:", e)
   def top_3_books(self):
      books = []
      try:
          self.cur.execute("SELECT Books.BookId, Books.Title, COUNT(*) AS TotalSales FROM Books INNER JOIN Sales ON Books.BookId = Sales.BooksId GROUP BY Books.BookId ORDER BY TotalSales DESC LIMIT 3")
          rows = self.cur.fetchall()
          for row in rows:
                BookId, Title, TotalSales = row
                books.append((BookId, Title, TotalSales))
          return books
      except sqlite3.Error as e:
            print("Error getting top 3 books:", e)
   def top_3_authors(self):
      auhtors = []
      try:
          self.cur.execute("SELECT Authors.AuthorId, Authors.Name, COUNT(Sales.BooksId) AS TotalSales FROM Authors LEFT JOIN Books ON Authors.AuthorId = Books.AuthorId LEFT JOIN Sales ON Books.BookId = Sales.BooksId GROUP BY Authors.AuthorId ORDER BY TotalSales DESC LIMIT 3;")
          rows = self.cur.fetchall()
          for row in rows:
                AuthorId, Name, TotalSales = row
                auhtors.append((AuthorId, Name, TotalSales))
          return auhtors
      except sqlite3.Error as e:
            print("Error getting top 3 authors:", e)