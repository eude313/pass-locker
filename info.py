class Info:
    #class that generates new credential for users 
    pass
    infomation_array = []
    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.email = email
        self.password = password
        
 #save_contact method saves info       
    def save_info(self):    
        Info.infomation_array.append(self) 
 #method that returns the infomation array     
    @classmethod
    def display_info(cls):   
        return cls.infomation_array