from User import User
class Staff(User):
    def __init__(self,username, email, password, is_admin):
        super().__init__(username,email,password)


    def set_

