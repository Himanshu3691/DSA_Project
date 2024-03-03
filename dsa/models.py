from django.db import models 

class User(models.Model):
    First = models.CharField(max_length = 50, blank = True, null = True)
    last = models.CharField(max_length = 50, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    phone_no = models.CharField(max_length = 50, blank = True, null = True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return self.First
    
class UserCode(models.Model):
    user_code = models.ForeignKey(User,blank = True, null = True, on_delete = models.CASCADE, related_name = "user_code")
    day = models.CharField(max_length = 50, blank = True, null = True)
    code = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return self.code
    
class Variable(models.Model):
    user_var = models.ForeignKey(User,blank = True, null = True, on_delete = models.CASCADE, related_name = "user_var")
    variable_type = models.CharField(max_length = 50, blank = True, null = True)
    variable1 = models.CharField(max_length = 50, blank = True, null = True)
    variable2 = models.CharField(max_length = 50,blank = True, null = True)
    login = models.BooleanField(default = False)
    

    def __str__(self):
        return self.variable_type