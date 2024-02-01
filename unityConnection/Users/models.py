from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Введите username')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    fathername = models.CharField(max_length=50, verbose_name="Отчество")
    email = models.EmailField(verbose_name="Email")
    username = models.CharField(max_length=50, unique=True, verbose_name="Имя пользователя")
    
    dateOfBirth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name="Город")
    languages = models.CharField(max_length=200, verbose_name="Языки")
    
    univercity = models.CharField(max_length=50, verbose_name="Образование")
    specialization = models.CharField(max_length=50, verbose_name="Специализация")
    
    school = models.CharField(max_length=50, verbose_name="Школа")
    profile_pic = models.ImageField(upload_to='meida/profile', verbose_name="Изображение")

    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Название поста") 
    text = models.TextField()
    profile_pic = models.ImageField(upload_to='meida/post', verbose_name="Изображение")