from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
            create and saves user with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user


    
    def create_superuser(self, email, password=None):
        """
            create and saves a superuser iwth given email and password
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    
    def has_perm(self, perm, obj=None):
        " Does the user have a specific permission? "
        #simplest possible answer: yes, always
        return True

    
    def has_module_perms(self, app_lebel):
        "Does the user have permissions to view the app `app_lebel` "
        #simplest possible answer: yes always
        return True
