from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import category_db,product_db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Webapp.models import contact_db
from django.contrib import messages



# Create your views here.
def index_page(request):
    return render(request,'index.html')

def category_page(request):
    return render(request,'category.html')

def save_category(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        de = request.POST.get('description')
        ph = request.FILES['photo']
        obj = category_db(Name=cn,Description=de,Photo=ph)
        obj.save()
        messages.success(request,"Category Saved Successfully")
        return redirect(category_page)

def display_category(request):
    data = category_db.objects.all()
    return render(request,"display_category.html",{'data':data})

def edit_category(request,cat_id):
    data = category_db.objects.get(id=cat_id)
    return render(request,"edit_category.html",{'data':data})

def update_category(request,cat_id):
    if request.method == "POST":
        cn = request.POST.get('cname')
        de = request.POST.get('description')
        try:
            ph = request.FILES['photo']
            fs = FileSystemStorage()
            file = fs.save(ph.name,ph)
        except MultiValueDictKeyError:
            file = category_db.objects.get(id=cat_id).Photo
        category_db.objects.filter(id=cat_id).update(Name=cn,Description=de,Photo=file)
        messages.success(request,"Updated Successfully")
        return redirect(display_category)

def delete_category(request,cat_id):
    x = category_db.objects.filter(id=cat_id)
    x.delete()
    messages.error(request, "Deleted Successfully")

    return redirect(display_category)

def admin_login(request):
    return render(request,'login.html')

def login_page(request):
    if request.method == "POST":
        un=request.POST.get('username')
        ps=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=ps)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=ps
                messages.success(request, "Welcome..!")

                return redirect(index_page)
            else :
                messages.error(request, "Incorrect Password")

                return redirect(admin_login)
        else :
            messages.error(request, "No USER Found")

            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully !")

    return redirect(admin_login)

def product_page(request):
    cat = category_db.objects.all()
    return render(request,'products.html',{'cat':cat})

def save_product(request):
    if request.method== "POST":
        pn = request.POST.get('pname')
        pc = request.POST.get('select')
        pr = request.POST.get('price')
        pd = request.POST.get('pdescription')
        ph = request.FILES['product_photo']
        obj = product_db(Product_Name=pn,Category=pc,Price=pr,Product_Description=pd,Product_Photo=ph)
        obj.save()
        messages.success(request, "Product Saved Successfully")
        return redirect(product_page)

def display_product(request):
    pro = product_db.objects.all()
    return render(request,'display_product.html',{'pro':pro})


def edit_product(request,pro_id):
    pro = product_db.objects.get(id=pro_id)
    cat = category_db.objects.all()
    return render(request,"edit_product.html",{'pro':pro,'cat':cat})

def update_product(request,pro_id):
    if request.method == "POST":
        pn = request.POST.get('pname')
        pc = request.POST.get('select')
        pr = request.POST.get('price')
        pd = request.POST.get('pdescription')

        try:
            ph = request.FILES['product_photo']
            fs = FileSystemStorage()
            file = fs.save(ph.name,ph)
        except MultiValueDictKeyError:
            file = product_db.objects.get(id=pro_id).Product_Photo
        product_db.objects.filter(id=pro_id).update(Product_Name=pn, Category=pc, Price=pr, Product_Description=pd, Product_Photo=file)
        messages.success(request,"Updated Successfully")

        return redirect(product_page)



def delete_product(request,pro_id):
    x = product_db.objects.filter(id=pro_id)
    x.delete()
    messages.error(request, "Deleted Successfully")

    return redirect(display_product)

def display_contact(request):
    data=contact_db.objects.all()
    return render(request,'contact_data.html',{'data':data})


def delete_contact(request,contact_id):
    x = contact_db.objects.filter(id=contact_id)
    x.delete()
    return redirect(display_contact)









