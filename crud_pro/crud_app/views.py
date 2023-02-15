import os

from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def load_form(request):
    form=EmployeeForm
    return render(request,'add_user.html',{'form':form})

def add(request):
    form=EmployeeForm(request.POST)
    form.save()
    return redirect(show)

def show(request):
    employee=Employee.objects.all()
    return render(request,'show_users.html',{'employee':employee})


#edit/id
#Edit button
def edit(request,id):
    employee=Employee.objects.get(id=id)  # .get to get 1 single data
    return render(request,'edit_user.html',{'employee':employee})


def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect(show)

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    form.save()
    return redirect(show)



def index(request):
    return render(request,'index.html')

def load(request):
    form=RegisterForm
    return render(request,'load.html',{'form':form})

def add2(request):
    form=RegisterForm(request.POST)
    form.save()
    return redirect(show_card)

def show_card(request):
    reg=Register.objects.all()
    return render(request,'show_card.html',{'reg':reg})

def edit_card(request,id):
    reg=Register.objects.get(id=id)
    return render(request,'edit_card.html',{'reg':reg})

def update_card(request,id):
    reg=Register.objects.get(id=id)
    form=RegisterForm(request.POST,instance=reg)
    form.save()
    return redirect(show_card)

def delete_card(request,id):
    reg=Register.objects.get(id=id)
    reg.delete()
    return redirect(show_card)


def add_item(request):
    if request.method=='POST':
        a=Itemform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['iname']
            pr=a.cleaned_data['price']
            ds=a.cleaned_data['des']
            im=a.cleaned_data['image']
            b=ItemModel(iname=nm,price=pr,des=ds,image=im)
            b.save()
            return redirect(display_item)
        else:
            return HttpResponse("Failed")
    else:
        return render(request,'add_item.html')


def display_item(request):
    a=ItemModel.objects.all()
    li=[]
    name=[]
    dis1=[]
    price=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        nm=i.iname
        name.append(nm)
        pri = i.price
        price.append(pri)
        dis=i.des
        dis1.append(dis)
        path = i.image
        li.append(str(path).split("/")[-1])
    print(li)
    mylist=zip(name,dis1,price,li,id)
    return render(request,'display_item.html',{'mylist':mylist})

def edit_item(request,id):
    prod=ItemModel.objects.get(id=id)
    li=str(prod.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:              # to check whether the file is not empty
            if len(prod.image) > 0:
                os.remove(prod.image.path)      # to remove path of old image
            prod.image=request.FILES['image']   # new image saved
        prod.iname=request.POST.get('iname')
        prod.des=request.POST.get('des')
        prod.price=request.POST.get('price')
        prod.save()
        return redirect(display_item)
    context={'prod':prod,'li':li}
    return render(request,'edit_item.html',context)

#delete item
def delete_item(request,id):
    prod=ItemModel.objects.get(id=id)
    if len(prod.image) > 0:             # deleting file
        os.remove(prod.image.path)
    prod.delete()
    return redirect(display_item)


