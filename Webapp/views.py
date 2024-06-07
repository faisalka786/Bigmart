from django.contrib import messages
from django.shortcuts import render, redirect
from Backend.models import product_db,category_db
from Webapp.models import contact_db, registration_db, cart_db


# Create your views here.

def homepage(request):
    cat = category_db.objects.all()
    return render(request,'home.html',{'category_key':cat})

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def shoppage(request):
    pro=product_db.objects.all()
    cat=category_db.objects.all()
    return render(request,'shop.html',{'product_key':pro,'category_key':cat})

def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        su=request.POST.get('subject')
        mo=request.POST.get('mobile')
        ms=request.POST.get('message')
        obj=contact_db(Name=na,Email=em,Subject=su,Mobile=mo,Message=ms)
        obj.save()
        return redirect(contactpage)

def filtered_products(request,cat_name):
    data = product_db.objects.filter(Category=cat_name)
    cat=category_db.objects.all()
    return render(request,'filtered_products.html',{'data':data, 'cat':cat})

def single_product(request,pro_id):
    data=product_db.objects.get(id=pro_id)
    return render(request,'single_product.html',{'data':data})

def registration(request):
    return render(request,'registration.html')

def userlogin(request):
    return render(request,'userlogin.html')


def save_registration(request):
    if request.method=="POST":
        us=request.POST.get("username")
        em=request.POST.get("email")
        p1=request.POST.get("pass1")
        obj=registration_db(Username=us,Email=em,Password=p1)
        if registration_db.objects.filter(Username=us).exists():
            messages.warning(request,"Username Already Registered")
        elif registration_db.objects.filter(Email=em).exists():
            messages.warning(request,"Email is already Exists")
        else:
            obj.save()
        return redirect(registration)

def user_login(request):
    if request.method=="POST":
        un=request.POST.get("username")
        pwd=request.POST.get("password")
        if registration_db.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, "Login Successfully !")
            return redirect(homepage)
        else:
            return redirect(registration)
    else:
        return redirect(registration)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout Successfully !")
    return redirect(homepage)

def save_cart(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        pn=request.POST.get("pname")
        qt=request.POST.get("quantity")
        tp=request.POST.get("price")
        obj=cart_db(Username=un,Product_Name=pn,Quantity=qt,Total_Price=tp)
        obj.save()
        messages.success(request, "Product added Successfully !")
        return redirect(homepage)

def cart_page(request):
    data = cart_db.objects.filter(Username=request.session['Username'])
    total=0
    final=0
    for i in data:
        total=total+i.Total_Price
    if total>500:
        delivery_charge=0
    else:
        delivery_charge=50
    final=total+delivery_charge
    return render(request,'cart.html',{'data':data,'total':total,'final':final,'delivery_charge':delivery_charge})

def delete_item(request,p_id):
    x = cart_db.objects.filter(id=p_id)
    x.delete()
    messages.success(request, "Deleted Successfully !")
    return redirect(cart_page)
