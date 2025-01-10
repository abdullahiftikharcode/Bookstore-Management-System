class Book:
    def __init__(self,title,authorid,price,year,edition,publisher):
        self.m_title=title
        self.m_authorid=authorid
        self.m_price=price
        self.m_year=year
        self.m_edition=edition
        self.m_publisher=publisher
    def get_title(self):
        return self.m_title

    def get_authorid(self):
        return self.m_authorid

    def get_price(self):
        return self.m_price

    def get_year(self):
        return self.m_year

    def get_edition(self):
        return self.m_edition

    def get_publisher(self):
        return self.m_publisher

    def set_title(self, title):
        self.m_title = title

    def set_authorid(self, authorid):
        self.m_authorid = authorid

    def set_price(self, price):
        self.m_price = price

    def set_year(self, year):
        self.m_year = year

    def set_edition(self, edition):
        self.m_edition = edition

    def set_publisher(self, publisher):
        self.m_publisher = publisher
        




