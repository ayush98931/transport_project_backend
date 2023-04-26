from django.db import models
import constants
# Create your models here.

class User(models.Model): 
    
    REQUIRED_FIELDS= [ 'name' , 'email' , 'password' , 'user_type']
    
    USERNAME_FIELD= 'user_id'
    
    
    is_anonymous=False
    is_authenticated=True
    
    user_types_choices = [
        (constants.user_types.transporter , "Transporter"),
        (constants.user_types.client , "Client"),
    ]
    
    
    user_id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=200 , null=False)
    email = models.EmailField(unique=True , null=False )
    password = models.CharField(max_length=500)
    join_date_time = models.DateTimeField( auto_now=True)
    user_type = models.CharField(max_length=100 , choices= user_types_choices)
    google_login = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    
    @staticmethod
    def encode_password(pswd):
        return constants.encrypt.encrypt_string(pswd)
    
    @staticmethod
    def decode_password(enpswd):
        return constants.encrypt.decrypt_string(enpswd)
    
    


    