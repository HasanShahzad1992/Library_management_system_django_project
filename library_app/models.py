from django.db import models

class Customer_Library(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=35)
    age=models.IntegerField()
    cnic=models.CharField(max_length=20)
class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=40)
    author_name=models.CharField(max_length=35)
    publishing_year=models.IntegerField(default=0)
class Customer_Book_Combined(models.Model):
    customer_book_id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer_Library,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    book_issuance_date=models.DateField()
class Library_System_Users(models.Model):
    library_user_id=models.AutoField(primary_key=True)
    library_user_email=models.EmailField(unique=True)
    library_user_password=models.CharField(max_length=30)
    library_user_username=models.CharField(max_length=30)
    library_user_type=models.CharField(max_length=30)
    picture_upload=models.ImageField(upload_to="profile_picture_library",default=True)