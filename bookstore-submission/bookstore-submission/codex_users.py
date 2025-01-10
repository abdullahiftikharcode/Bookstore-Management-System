class Users:
    def __init__(self,username,password,faculty,image,userid):
        self.m_username=username
        self.m_faculty=faculty
        self.m_password=password
        self.m_image=image
        self.m_userid=id
    def get_username(self):
        return self.m_username

    def get_image(self):
        return self.m_image
    def set_username(self, username):
        self.m_username = username

    
    def get_authority(self):
        return self.m_faculty

    
    def set_authority(self, faculty):
        self.m_faculty = faculty

   
    def get_password(self):
        return self.m_password

    
    def set_password(self, password):
        self.m_password = password
    def set_userid(self, userid):
        self.m_userid =userid
    def get_userid(self):
       return  self.m_userid
