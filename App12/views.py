from django.shortcuts import render, redirect, get_object_or_404
from App12.models import *
from App12.forms import GoodsForm,CustomerForm
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'Home.html')

def showGoodsList(request):
    GoodsList = Goods.objects.all()
    context = {'Goods': GoodsList}
    return render(request,'showGoodsList.html',context)

def showGoodsOne(request,gid):
    GoodsList = Goods.objects.get(gid=gid)
    context = {'Goods': GoodsList}
    return render(request,'showGoodsOne.html',context)

def showCustomerList(request):
    CustomerList = Customer.objects.all()
    context = {'Customer': CustomerList}
    return render(request,'showCustomerList.html',context)

def showCustomerOne(request,cid):
    CustomerList = Customer.objects.get(cid=cid)
    context = {'Customer': CustomerList}
    return render(request,'showCustomerOne.html',context)

def newGoods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'บันทึกเรียบร้อย')
            return redirect('showGoodsList')
        else:
            Good = Goods.objects.get(gid=request.POST['gid'])
            if Good:
                messages.add_message(request, messages.WARNING,
                                     'รหัสซ้ำ')
            else:
                messages.add_message(request, messages.WARNING,
                                     'ข้อมูลไม่ถูกต้อง')
    else:
        form = GoodsForm()
    context = {'form':form}
    return render(request,'newGoods.html',context)

def updateGoods(request,gid):
    Good = Goods.objects.get(gid=gid)
    obj = get_object_or_404(Goods,gid=gid)
    form = GoodsForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'แก้ไขเรียบร้อย')
            return redirect('showGoodsList')
        else:
            messages.add_message(request, messages.WARNING,
                                 'ข้อมูลไม่ถูกต้อง')
    form.GoodsEditForm()
    context = {'form':form}
    return render(request, 'updateGoods.html',context)

def deleteGoods(request,gid=None):
    if request.method == 'POST':
        gid = request.POST['gid']
        Good = Goods.objects.get(gid=gid)
        if Good:
            Good.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'ลบเรียบร้อย')
            return redirect('showGoodsList')
        else:
            messages.add_message(request, messages.WARNING,
                                 'ไม่พบสินค้า')
    else:
        Good = Goods.objects.get(gid=gid)
        context = {'Goods': Good}
        return render(request, 'deleteGoods.html', context)

def newCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'บันทึกเรียบร้อย')
            return redirect('showCustomerList')
        else:
            Customers = Customer.objects.get(cid=request.POST['cid'])
            if Customers:
                messages.add_message(request, messages.WARNING,'รหัสซ้ำ')
            else:
                messages.add_message(request, messages.WARNING, 'ข้อมูลไม่ถูกต้อง')
    else:
        form = CustomerForm()
    context = {'form':form}
    return render(request,'newCustomer.html',context)

def updateCustomer(request,cid):
    Customers = Customer.objects.get(cid=cid)
    obj = get_object_or_404(Customer,cid=cid)
    form = CustomerForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขเรียบร้อย')
            return redirect('showCustomerList')
        else:
            messages.add_message(request, messages.WARNING, 'ข้อมูลไม่ถูกต้อง')
    form.CustomerEditForm()
    context = {'form':form}
    return render(request, 'updateCustomer.html',context)

def deleteCustomer(request,cid=None):
    if request.method == 'POST':
        cid = request.POST['cid']
        Customers = Customer.objects.get(cid=cid)
        if Customers:
            Customers.delete()
            messages.add_message(request, messages.SUCCESS, 'ลบเรียบร้อย')
            return redirect('showCustomerList')
        else:
            messages.add_message(request, messages.WARNING, 'ไม่พบสินค้า')
    else:
        Customers = Customer.objects.get(cid=cid)
        context = {'Customer': Customers}
        return render(request, 'deleteCustomer.html', context)