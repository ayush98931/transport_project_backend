from cryptography.fernet import Fernet

class user_types:
    client = "CLIENT"
    transporter = "TRANSPORTER"

class database:
    user = "root"
    password = "shourya121"
    dbname = "transport"
    host = "localhost"
    port = "3306"
    
class encrypt:
    key = b'Wjt8z-_jMaYElyOuFU-3H4Hy6AUEI7ezKDdfg5f-kMY='
    f = Fernet(key)
    
    @classmethod
    def encrypt_string(cls, s ):
        return cls.f.encrypt(s.encode()).decode()
    
    @classmethod
    def decrypt_string(cls , s):
        return cls.f.decrypt(s.encode()).decode()
    
    
class smtp_mail:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp-relay.sendinblue.com' 
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'shouryarajsinghgoud@gmail.com'
    EMAIL_HOST_PASSWORD = 'ypc2QJCY01A9kjGH'