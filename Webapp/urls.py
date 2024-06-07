from django.urls import path
from Webapp import views



urlpatterns =[
    path('',views.homepage,name="Home"),
    path('About/',views.aboutpage,name="About"),
    path('Contact/',views.contactpage,name="Contact"),
    path('Shop/',views.shoppage,name="Shop"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('registration/',views.registration,name="registration"),
    path('save_registration/',views.save_registration,name="save_registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_item/<int:p_id>/',views.delete_item,name="delete_item"),
    path('userlogin/',views.userlogin,name="userlogin"),

]