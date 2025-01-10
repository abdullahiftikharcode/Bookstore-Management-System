class Customer:
    def __init__(self,name,email,adress,phonenumber):
        self.m_name=name
        self.m_email=email
        self.m_address=adress
        self.m_phonenumber=phonenumber
    def get_name(self):
        return self.m_name

    def get_email(self):
        return self.m_email

    def get_address(self):
        return self.m_address

    def get_phonenumber(self):
        return self.m_phonenumber

    def set_name(self, name):
        self.m_name = name

    def set_email(self, email):
        self.m_email = email

    def set_address(self, address):
        self.m_address = address

    def set_phonenumber(self, phonenumber):
        self.m_phonenumber = phonenumber




