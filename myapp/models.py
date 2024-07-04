from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractBaseUser,UserManager,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Demo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    cost=models.DecimalField(decimal_places=3,max_digits=3)

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass
class CustomUserManager(UserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
          raise ValueError("Email couldn't fetched !!")
        email = self.normalize_email(email)   
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
        id=models.AutoField(primary_key=True)
        email=models.EmailField(max_length=30,unique=True)
        password=models.CharField(max_length=255)
        firstname=models.CharField(max_length=20)
        lastname=models.CharField(max_length=20)
        img=models.CharField(max_length=255,null=True)
        phone=models.CharField(
            max_length=10,
            validators=[MinLengthValidator(10),MaxLengthValidator(10)],
            unique=True
        )
        # address=models.ForeignKey('FullAddress',on_delete=models.CASCADE,
        #     blank=True,null=True,related_name='user_fulladress')
        date_joined=models.DateTimeField(auto_now_add=True)

        object = CustomUserManager()

        USERNAME_FIELD='email'
        EMAIL_FILED='email'
        REQUIRED_FIELDS=[]

        # def _str_(self):
        #     return self.firstname + " " + self.lastname


            
                
            
            #     class Meta:
            #         verbose_namemodel(email=email,**extra_fields 
            #         user.set_password(password)
            #         user.save(using=self_db)
            #         return user        verbose_name_pluralmodel(email=email,**extra_fields 
            #         user.set_password(password)
            #         user.save(using=self_db)
            #         return user 
            #     def __str__(self):
            #         return self.name
            
            #     def get_absolute_url(self):
            #         return revmodel(email=email,**extra_fieldsr
            #         user.set_password(password)
            #         user.save(using=self_db)
            #         return users={"pk": self.pk})
            # (models.Model):
            
                
            
            #     class Meta:
            #         verbose_namemodel(email=email,**extra_fields)
            #         user.set_password(password)
            #         user.save(using=self_db)
            #         return user
                    
                        
                    
                #         class Meta:
                #             verbose_namemodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user                verbose_name_pluralmodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user         
                #         def __str__(self):
                #             return self.name
                    
                #         def get_absolute_url(self):
                #             return revmodel(email=email,**extra_fieldsr
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return users={"pk": self.pk})
                #     ")
                #     verbose_name_pluralmodel(email=email,**extra_fields)
                #     user.set_password(password)
                #     user.save(using=self_db)
                #     return user
                    
                        
                    
                #         class Meta:
                #             verbose_namemodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user                verbose_name_pluralmodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user         
                #         def __str__(self):
                #             return self.name
                    
                #         def get_absolute_url(self):
                #             return revmodel(email=email,**extra_fieldsr
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return users={"pk": self.pk})
                #     s")
            
                # def __str__(self):
                #     return self.name
            
                # def get_absolute_url(self):
                #     return revmodel(email=email,**extra_fields)
                #     user.set_password(password)
                #     user.save(using=self_db)
                #     return user
                    
                        
                    
                #         class Meta:
                #             verbose_namemodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user                verbose_name_pluralmodel(email=email,**extra_fields 
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return user         
                #         def __str__(self):
                #             return self.name
                    
                #         def get_absolute_url(self):
                #             return revmodel(email=email,**extra_fieldsr
                #             user.set_password(password)
                #             user.save(using=self_db)
                #             return users={"pk": self.pk})
                #     _detail", kwargs={"pk": self.pk})
             