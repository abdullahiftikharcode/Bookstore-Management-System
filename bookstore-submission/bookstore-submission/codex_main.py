#bscs23070
#bscs23031
#bcss230145
from codex_Bookstore import Bookstore
from codex_UI import menu

def mainfunc():
    bookstore=Bookstore("DB/bookstore.db");
    menu(bookstore)
    
if __name__=="__main__":
    mainfunc()