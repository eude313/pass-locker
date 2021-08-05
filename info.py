class info:
    #class that generates new credential for users 
    pass
    infomation_array = []
    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.email = email
        self.password = password
        
 #save_contact method saves info       
    def save_info(self):    
        info.infomation_array.append(self) 