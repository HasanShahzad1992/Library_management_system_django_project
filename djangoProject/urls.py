"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flight_app import views as flight_app_view
from library_app import views as library_app_view
from hospital_app import views as hospital_app_view
from school_app import views as school_app_view
from employee_app import views as employee_app_view
from django.conf import settings
from django.conf.urls.static import static

#we import views from the application that is on the left bar, my application name is django_application and basit's name was my_app.
#first, we get a data from front_end which is initiating the request. I write the request in postman as a form of dictionary(json)
# in the side bar of django_application, when we click down_arrow there is views.py file, so we need to import views. Views act as a controller
# in path, we give name of pipeline(sign_up/) through which front end and back end is connected
#after sign_up/, we tell where the data from the front end is routed towards
#it goes to views.sign_up, sign_up is a def function in views.py, take note that the route should be views.sign_up, not views.sign_up()
#we need to give a name to the pipeline also so that it gets an identity
#front end, always initiates a request and gets a response from back end. backend, never initiates a request
# front_end would only connect with back_end when back_end server is running
#in terminal, we write python manage.py runserver to make the server run

# in postman, we go to body

urlpatterns = [path('admin/', admin.site.urls),
               path("load_customer_add_html",library_app_view.load_customer_add_html),
               path("add_customer_html",library_app_view.add_customer_html),
               path("view_all_customer_library",library_app_view.view_all_customer_library),

               path("load_customer_update_html",library_app_view.load_customer_update_html),
               path("update_customer_library_html/<customer_library_id>",library_app_view.update_customer_library_html),

               path("load_book_add_html",library_app_view.load_book_add_html),
               path("add_book_html",library_app_view.add_book_html),
               path("view_all_books",library_app_view.view_all_books),

               path("load_books_library_update_html",library_app_view.load_books_library_update_html),
               path("update_books_library_html/<book_library_id>",library_app_view.update_books_library_html),

               path("load_customer_book_combined_add_html",library_app_view.load_customer_book_combined_add_html),
               path("add_customer_book_combined_html",library_app_view.add_customer_book_combined_html),
               path("view_customer_book_combined_html",library_app_view.view_customer_book_combined_html),

               path("load_customer_book_combined_update_html",library_app_view.load_customer_book_combined_update_html),
               path("update_customer_book_combined_html/<updated_customer_book_id>",library_app_view.update_customer_book_combined_html),

               path("load_library_system_signup",library_app_view.load_library_system_signup),
               path("signup_library_system",library_app_view.signup_library_system),
               path("load_library_system_login",library_app_view.load_library_system_login,name="load_library_system_login"),
               path("login_library_system",library_app_view.login_library_system),
               path("load_admin_library_system_home",library_app_view.load_admin_library_system_home,name="load_admin_library_system_home"),
               path("load_entry_library_system_home",library_app_view.load_entry_library_system_home,name="load_entry_library_system_home"),
               path("logout_library_system",library_app_view.logout_library_system),

               path("upload_picture_library/<userid>",library_app_view.upload_picture_library,name="upload_picture_library"),



               path("load_passenger_flight_add_html",flight_app_view.load_passenger_flight_add_html),
               path("add_passenger_flight_html",flight_app_view.add_passenger_flight_html),
               path("view_all_passenger_flight_html",flight_app_view.view_all_passenger_flight_html),
               path("load_update_passenger_flight_html",flight_app_view.load_update_passenger_flight_html),
               path("update_passenger_flight_html/<passenger_update_id>",flight_app_view.update_passenger_flight_html),
               path("load_passenger_flight_delete_html",flight_app_view.load_passenger_flight_delete_html),
               path("delete_passenger_flight_html/<delete_passenger_id>",flight_app_view.delete_passenger_flight_html),

               path("load_flight_add_html",flight_app_view.load_flight_add_html),
               path("add_flight_html",flight_app_view.add_flight_html),
               path("view_all_flights_html",flight_app_view.view_all_flights_html),
               path("load_flights_update_html",flight_app_view.load_flights_update_html),
               path("update_flights_html/<flight_update_id>",flight_app_view.update_flights_html),
               path("load_flights_delete_html",flight_app_view.load_flights_delete_html),
               path("delete_flights_html/<flight_delete_id>",flight_app_view.delete_flights_html),

               path("load_passenger_flight_combined_add_html",flight_app_view.load_passenger_flight_combined_add_html),
               path("add_passenger_flight_combined_html",flight_app_view.add_passenger_flight_combined_html),
               path("view_all_passenger_flight_combined_html",flight_app_view.view_all_passenger_flight_combined_html),
               path("load_passenger_flight_combined_update",flight_app_view.load_passenger_flight_combined_update),
               path("update_passenger_flight_combined/<passenger_flight_combined_id>",flight_app_view.update_passenger_flight_combined),
               path("load_passenger_flight_combined_delete_html",flight_app_view.load_passenger_flight_combined_delete_html),
               path("delete_passenger_flight_combined_html/<delete_flight_combined_id>",flight_app_view.delete_passenger_flight_combined_html),

               path("load_flight_system_signup",flight_app_view.load_flight_system_signup),
               path("signup_flight_system",flight_app_view.signup_flight_system),
               path("load_flight_system_login",flight_app_view.load_flight_system_login,name="load_flight_system_login"),
               path("login_flight_system",flight_app_view.login_flight_system),
               path("load_entry_flight_system_home",flight_app_view.load_entry_flight_system_home,name="load_entry_flight_system_home"),
               path("load_admin_flight_system_home",flight_app_view.load_admin_flight_system_home,name="load_admin_flight_system_home"),
               path("logout_flight_system",flight_app_view.logout_flight_system),

               path("upload_image/<userid>",flight_app_view.upload_image),




               path("load_hospital_add_html",hospital_app_view.load_hospital_add_html),
               path("add_hospital_html",hospital_app_view.add_hospital_html),

               path("view_all_hospitals_html",hospital_app_view.view_all_hospitals_html),

               path("load_hospital_update_html",hospital_app_view.load_hospital_update_html),
               path("update_hospital_html/<updated_hospital_id>",hospital_app_view.update_hospital_html),
               path("load_hospital_delete_html",hospital_app_view.load_hospital_delete_html),
               path("delete_hospital_html/<deleted_hospital_id>",hospital_app_view.delete_hospital_html),

               path("load_doctor_add_html",hospital_app_view.load_doctor_add_html),
               path("add_doctor_html",hospital_app_view.add_doctor_html),
               path("view_all_doctor_html",hospital_app_view.view_all_doctor_html),
               path("load_doctor_update_html",hospital_app_view.load_doctor_update_html),
               path("update_doctor_html/<updated_doctor_id>",hospital_app_view.update_doctor_html),
               path("load_doctor_html_delete",hospital_app_view.load_doctor_html_delete),
               path("delete_doctor_html/<delete_doctor_id>",hospital_app_view.delete_doctor_html),

               path("load_hospital_doctor_combined_add_html",hospital_app_view.load_hospital_doctor_combined_add_html),
               path("add_hospital_doctor_combined",hospital_app_view.add_hospital_doctor_combined),
               path("view_all_hospital_doctor_combined",hospital_app_view.view_all_hospital_doctor_combined),
               path("load_hospital_doctor_combined_update_html",hospital_app_view.load_hospital_doctor_combined_update_html),
               path("update_hospital_doctor_html/<updated_hospital_doctor_combined_id>",hospital_app_view.update_hospital_doctor_html),

               path("load_hospital_doctor_combined_delete",hospital_app_view.load_hospital_doctor_combined_delete),
               path("delete_hospital_doctor_combined/<delete_hospital_doctor_combined_id>",hospital_app_view.delete_hospital_doctor_combined),

               path("load_medical_system_signup",hospital_app_view.load_medical_system_signup),
               path("signup_medical_system",hospital_app_view.signup_medical_system),
               path("load_medical_system_login",hospital_app_view.load_medical_system_login,name="load_medical_system_login"),
               path("login_medical_system",hospital_app_view.login_medical_system),
               path("load_admin_medical_system_home_page",hospital_app_view.load_admin_medical_system_home_page,name="load_admin_medical_system_home_page"),
               path("load_entry_medical_system_home_page",hospital_app_view.load_entry_medical_system_home_page,name="load_entry_medical_system_home_page"),
               path("logout_medical_system",hospital_app_view.logout_medical_system),

               path("upload_picture/<userid>",hospital_app_view.upload_picture),

               path("load_student_add",school_app_view.load_student_add),
               path("add_student",school_app_view.add_student),
               path("view_all_students",school_app_view.view_all_students),
               path("load_student_update",school_app_view.load_student_update),
               path("student_update/<student_id>",school_app_view.student_update),
               path("load_student_delete",school_app_view.load_student_delete),
               path("delete_student/<student_id>",school_app_view.delete_student),


               path("load_teacher_add",school_app_view.load_teacher_add),
               path("add_teacher",school_app_view.add_teacher),
               path("view_all_teachers",school_app_view.view_all_teachers),
               path("load_teacher_update",school_app_view.load_teacher_update),
               path("teacher_update/<teacher_id>",school_app_view.teacher_update),
               path("load_teacher_delete",school_app_view.load_teacher_delete),
               path("delete_teacher/<teacher_id>",school_app_view.delete_teacher),

               path("load_class_add",school_app_view.load_class_add),
               path("add_class",school_app_view.add_class),
               path("view_all_classes",school_app_view.view_all_classes),
               path("load_class_update",school_app_view.load_class_update),
               path("class_update/<id_class>",school_app_view.class_update),
               path("load_class_delete",school_app_view.load_class_delete),
               path("delete_class/<id_class>",school_app_view.delete_class),

               path("load_subject_add",school_app_view.load_subject_add),
               path("add_subject",school_app_view.add_subject),
               path("view_all_subjects",school_app_view.view_all_subjects),
               path("load_subject_update",school_app_view.load_subject_update),
               path("subject_update/<id_subject>",school_app_view.subject_update),
               path("load_subject_delete",school_app_view.load_subject_delete),
               path("delete_subject/<id_subject>",school_app_view.delete_subject),

               path("load_student_class_combined_add",school_app_view.load_student_class_combined_add),
               path("student_class_combined_add",school_app_view.student_class_combined_add),
               path("view_all_student_class_combined",school_app_view.view_all_student_class_combined),
               path("load_student_class_combined_update",school_app_view.load_student_class_combined_update),
               path("student_class_combined_update/<student_class_id>",school_app_view.student_class_combined_update),
               path("load_student_class_combined_delete",school_app_view.load_student_class_combined_delete),
               path("student_class_combined_delete/<student_class_id>",school_app_view.student_class_combined_delete),

               path("load_class_subject_teacher_combined_add",school_app_view.load_class_subject_teacher_combined_add),
               path("class_subject_teacher_combined_add",school_app_view.class_subject_teacher_combined_add),
               path("view_all_class_subject_teacher_combined",school_app_view.view_all_class_subject_teacher_combined),
               path("load_class_subject_teacher_combined_update",school_app_view.load_class_subject_teacher_combined_update),
               path("class_subject_teacher_combined_update/<class_subject_teacher_id>",school_app_view.class_subject_teacher_combined_update),
               path("load_class_subject_teacher_combined_delete",school_app_view.load_class_subject_teacher_combined_delete),
               path("class_subject_teacher_combined_delete/<class_subject_teacher_id>",school_app_view.class_subject_teacher_combined_delete),

               path("load_user_signup",school_app_view.load_user_signup),
               path("user_signup",school_app_view.user_signup),
               path("load_user_login_school",school_app_view.load_user_login_school,name="load_user_login_school"),
               path("user_login_school",school_app_view.user_login_school),
               path("load_admin_home_page_school",school_app_view.load_admin_home_page_school,name="load_admin_home_page_school"),
               path("load_entry_home_page_school",school_app_view.load_entry_home_page_school,name="load_entry_home_page_school"),
               path("logout_school",school_app_view.logout_school)




               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)