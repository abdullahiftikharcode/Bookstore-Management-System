class Sale:
    def __init__(self,orderdate,customerid,bookid,discount,total):
        self.m_orderdate=orderdate
        self.m_customerid=customerid
        self.m_bookid=bookid
        self.m_discount=discount
        self.m_total=total
    def get_orderdate(self):
        return self.m_orderdate
    def get_customerid(self):
        return self.m_customerid

    def get_bookid(self):
        return self.m_bookid

    def get_discount(self):
        return self.m_discount

    def get_total(self):
        return self.m_total
    
    def set_orderdate(self, orderdate):
        self.m_orderdate = orderdate
        
    def set_customerid(self, customerid):
        self.m_customerid = customerid

    def set_bookid(self, bookid):
        self.m_bookid = bookid

    def set_discount(self, discount):
        self.m_discount = discount

    def set_total(self, total):
        self.m_total = total
        




