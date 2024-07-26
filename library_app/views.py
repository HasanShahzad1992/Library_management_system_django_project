from django.shortcuts import render,redirect
from library_app import models
from django.views.decorators.csrf import csrf_exempt

def load_customer_add_html(initial_request_from_front_end):
    try:
        username=initial_request_from_front_end.session["username"]
        user_type=initial_request_from_front_end.session["user_type"]
        if user_type=="admin":
            return render(initial_request_from_front_end, "load_add_customer.html",{"username":username})
        elif user_type=="entry":
            return redirect("load_entry_library_system_home")
    except:
        return redirect("load_library_system_login")
def add_customer_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        name_of_customer_library=initial_request_from_front_end.POST.get("library_customer_name")
        age_customer_library=initial_request_from_front_end.POST.get("library_customer_age")
        cnic_customer_library=initial_request_from_front_end.POST.get("library_customer_cnic")
        customer_add_object=models.Customer_Library.objects.create(customer_name=name_of_customer_library,age=age_customer_library,cnic=cnic_customer_library)
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_add_customer.html",{"message":"customer_library_added_successfully","username":username})
def view_all_customer_library(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            if user_type=="admin":
                all_customer_library_objects=models.Customer_Library.objects.all()
                return render(initial_request_from_front_end,"view_customers_library.html",{"all_customer":all_customer_library_objects,"user_name":user_name})
            elif user_type=="entry":
                return redirect("load_entry_library_system_home")
        except:
            return redirect("load_library_system_login")


def load_customer_update_html(initial_request_from_front_end):
    try:
        user_name=initial_request_from_front_end.session["username"]
        user_type=initial_request_from_front_end.session["user_type"]
        if user_type=="admin":
            all_customer_objects = models.Customer_Library.objects.all()
            return render(initial_request_from_front_end, "load_update_customer_library.html",{"all_customers": all_customer_objects,"username":user_name})
        elif user_type=="entry":
            return redirect("load_entry_library_system_home")
    except:
        return redirect("load_library_system_login")

    all_customer_objects=models.Customer_Library.objects.all()
    return render(initial_request_from_front_end,"load_update_customer_library.html",{"all_customers":all_customer_objects})

def update_customer_library_html(initial_request_from_front_end,customer_library_id):
    all_customer_library_objects = models.Customer_Library.objects.all()
    particular_customer_object_from_data_base=models.Customer_Library.objects.get(customer_id=customer_library_id)
    updated_customer_library_name=initial_request_from_front_end.POST.get("name_of_customer")
    updated_customer_library_cnic=initial_request_from_front_end.POST.get("cnic_of_customer")
    updated_customer_library_age=initial_request_from_front_end.POST.get("age_of_customer")
    particular_customer_object_from_data_base.customer_name=updated_customer_library_name
    particular_customer_object_from_data_base.age=updated_customer_library_age
    particular_customer_object_from_data_base.cnic=updated_customer_library_cnic
    particular_customer_object_from_data_base.save()
    user_name=initial_request_from_front_end.session["username"]
    user_type=initial_request_from_front_end.session["user_type"]
    return render(initial_request_from_front_end,"load_update_customer_library.html",{"username":user_name,"all_customers":all_customer_library_objects,"message":"updated_successfully"})


def load_book_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            if user_type=="admin":
                return render(initial_request_from_front_end, "load_add_books.html",{"username":username})
            elif user_type=="entry":
                return redirect("load_entry_library_system_home")
        except:
            return redirect("load_library_system_login")
@csrf_exempt
def add_book_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        book_name=initial_request_from_front_end.POST.get("name_of_book")
        author_name=initial_request_from_front_end.POST.get("name_of_author")
        publishing_year=initial_request_from_front_end.POST.get("year_of_publishing")
        book_object=models.Book.objects.create(book_name=book_name,author_name=author_name,publishing_year=publishing_year)
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_add_books.html",{"message":"book data has been added","username":username})
def view_all_books(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            if user_type=="admin":
                all_book_objects = models.Book.objects.all()
                return render(initial_request_from_front_end, "view_all_books_library.html", {"all_books": all_book_objects,"username":username})
            elif user_type=="entry":
                return redirect("load_entry_library_system_home")
        except:
            return redirect("load_library_system_login")

def load_books_library_update_html(initial_request_from_front_end):
    try:
        user_name=initial_request_from_front_end.session["username"]
        user_type=initial_request_from_front_end.session["user_type"]
        if user_type=="admin":
            all_books_objects=models.Book.objects.all()
            return render(initial_request_from_front_end,"load_update_book_library.html",{"all_books":all_books_objects,"user_name":user_name})
        elif user_type=="entry":
            return redirect("load_entry_library_system_home")
    except:
        return redirect("load_library_system_login")
def update_books_library_html(initial_request_from_front_end,book_library_id):
    all_book_objects=models.Book.objects.all()
    particular_object_from_database_which_has_been_updated=models.Book.objects.get(book_id=book_library_id)
    updated_book_name=initial_request_from_front_end.POST.get("Name_of_book")
    updated_author_name=initial_request_from_front_end.POST.get("Author_of_Book")
    updated_publishing_year=initial_request_from_front_end.POST.get("Publishing year of book")
    particular_object_from_database_which_has_been_updated.book_name=updated_book_name
    particular_object_from_database_which_has_been_updated.author_name=updated_author_name
    particular_object_from_database_which_has_been_updated.publishing_year=updated_publishing_year
    particular_object_from_database_which_has_been_updated.save()
    user_name=initial_request_from_front_end.session["username"]
    return render(initial_request_from_front_end,"load_update_book_library.html",{"all_books":all_book_objects,"user_name":user_name,"message":"updated_successfully!!!"})

def load_customer_book_combined_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            all_customer_objects = models.Customer_Library.objects.all()
            all_book_objects = models.Book.objects.all()
            return render(initial_request_from_front_end, "load_add_customer_book_combined.html",{"all_customers": all_customer_objects, "all_books": all_book_objects,"user_name":user_name})
        except:
            return redirect("load_library_system_login")
def add_customer_book_combined_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        all_customer_objects=models.Customer_Library.objects.all()
        all_book_objects=models.Book.objects.all()
        customer_detail=initial_request_from_front_end.POST.get("select_customer")
        book_detail=initial_request_from_front_end.POST.get("select_book")
        book_issue_date_details=initial_request_from_front_end.POST.get("book_issue_date")
        combined_customer_book_object=models.Customer_Book_Combined.objects.create(customer_id=customer_detail,book_id=book_detail,book_issuance_date=book_issue_date_details)
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_add_customer_book_combined.html",{"message":"combined data of customer book added","all_customers":all_customer_objects,"all_books": all_book_objects,"username":username})
#here the assumption is that combined table is full and we just want to read it
def view_customer_book_combined_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            all_customer_book_combined_objects=models.Customer_Book_Combined.objects.all()
            return render(initial_request_from_front_end,"view_customer_book_combined.html",{"all_customer_book_combined":all_customer_book_combined_objects,"user_name":user_name})
        except:
            return render("load_library_system_login")

#here first we view all objects of transaction, then we call extra all_customer and all_book object for editing
def load_customer_book_combined_update_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            customer_book_combined_objects=models.Customer_Book_Combined.objects.all()
            all_customers_objects=models.Customer_Library.objects.all()
            all_books_objects=models.Book.objects.all()
            return render(initial_request_from_front_end,"load_customer_book_combined_update.html",{"customer_book_combined":customer_book_combined_objects,"all_customers":all_customers_objects,"all_books":all_books_objects,"user_name":user_name,"user_type":user_type})
        except:
            return redirect("load_library_system_login")
def update_customer_book_combined_html(initial_request_from_front_end,updated_customer_book_id):
    if initial_request_from_front_end.method=="POST":
        customer_book_combined_objects = models.Customer_Book_Combined.objects.all()
        all_customers_objects = models.Customer_Library.objects.all()
        all_books_objects = models.Book.objects.all()
        new_customer_id=initial_request_from_front_end.POST.get("customer_id_to_be_updated")
        new_book_id=initial_request_from_front_end.POST.get("book_id_to_be_updated")
        new_issuance_date=initial_request_from_front_end.POST.get("new_issuance_date")
        particular_customer_book_combined_object=models.Customer_Book_Combined.objects.get(customer_book_id=updated_customer_book_id)
        particular_customer_book_combined_object.customer_id=new_customer_id
        particular_customer_book_combined_object.book_id=new_book_id
        particular_customer_book_combined_object.book_issuance_date=new_issuance_date
        particular_customer_book_combined_object.save()
        user_name=initial_request_from_front_end.session["username"]
        user_type=initial_request_from_front_end.session["user_type"]
        return render(initial_request_from_front_end,"load_customer_book_combined_update.html",{"customer_book_combined":customer_book_combined_objects,"all_customers":all_customers_objects,"all_books":all_books_objects,"message":"updated_successfully","user_name":user_name,"user_type":user_type})

def load_library_system_signup(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        return render(initial_request_from_front_end,"load_signup_library_system.html")
def signup_library_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email_user=initial_request_from_front_end.POST.get("email_typed_by_user")
        password_user=initial_request_from_front_end.POST.get("password_typed_by_user")
        username_user=initial_request_from_front_end.POST.get("username chosen by user")
        particular_library_system_object=models.Library_System_Users.objects.create(library_user_email=email_user,library_user_password=password_user,library_user_username=username_user,library_user_type="admin")
        return render(initial_request_from_front_end,"load_signup_library_system.html",{"username":particular_library_system_object.library_user_username})
def load_library_system_login(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name_variable=initial_request_from_front_end.session["username"]
            return redirect("load_library_system_home")
        except:
            return render(initial_request_from_front_end, "load_login_library_system.html")
def login_library_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email_user=initial_request_from_front_end.POST.get("email written by user in login")
        password_user=initial_request_from_front_end.POST.get("password written by user in login")
        try:
            particular_library_system_user_object=models.Library_System_Users.objects.get(library_user_email=email_user,library_user_password=password_user)
            initial_request_from_front_end.session["username"]=particular_library_system_user_object.library_user_username
            initial_request_from_front_end.session["user_type"]=particular_library_system_user_object.library_user_type
            initial_request_from_front_end.session["userid"]=particular_library_system_user_object.library_user_id
            initial_request_from_front_end.session["picture_key"]=particular_library_system_user_object.picture_upload.url
            if particular_library_system_user_object.library_user_type=="entry":
                return redirect("load_entry_library_system_home")
            elif particular_library_system_user_object.library_user_type=="admin":
                return redirect("load_admin_library_system_home")
        except:
            return render(initial_request_from_front_end,"load_login_library_system.html.html",{"message":"wrong password or email"})
def load_admin_library_system_home(initial_request_from_fron_end):
    if initial_request_from_fron_end.method=="GET":
        try:
            username_variable=initial_request_from_fron_end.session["username"]
            user_type=initial_request_from_fron_end.session["user_type"]
            userid=initial_request_from_fron_end.session["userid"]
            picture=initial_request_from_fron_end.session["picture_key"]
            if user_type=="admin":
                return render(initial_request_from_fron_end,"load_admin_home_library_system.html",{"user_name":username_variable,"userid":userid,"picture_key":picture})
            elif user_type=="entry":
                return redirect("load_entry_library_system_home")
        except:
            return redirect("load_library_system_login")
def load_entry_library_system_home(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username_variable=initial_request_from_front_end.session["username"]
            user_type=initial_request_from_front_end.session["user_type"]
            userdid=initial_request_from_front_end.session["userid"]
            picture=initial_request_from_front_end.session["picture_key"]
            if user_type=="entry":
                return render(initial_request_from_front_end,"load_entry_home_library_system.html",{"user_name":username_variable,"userid":userdid,"picture_key":picture})
            elif user_type=="admin":
                return redirect("load_admin_library_system_home")
        except:
            return redirect("load_library_system_login")
def logout_library_system(initial_request_from_front_end):
    initial_request_from_front_end.session.flush()
    return redirect("load_library_system_login")

def upload_picture_library(initial_request_from_front_end,userid):
    if initial_request_from_front_end.method=="POST":
        picture_uploaded=initial_request_from_front_end.FILES.get("picture_to_be_uploaded")
        particular_image_object=models.Library_System_Users.objects.get(library_user_id=userid)
        particular_image_object.picture_upload=picture_uploaded
        particular_image_object.save()
        if initial_request_from_front_end.session["user_type"]=="entry":
            return redirect("load_entry_library_system_home")
        elif initial_request_from_front_end.session["user_type"]=="admin":
            return redirect("load_admin_library_system_home")












