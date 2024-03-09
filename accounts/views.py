from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from .models import Sale
from django.db.models import Sum
import openpyxl
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('login')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        print("user data saved successfully")
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        
    else:
        return render(request,'accounts/login.html')
    


def logout(request):
    auth_logout(request)
    return redirect('login')





def home(request):
    if request.method == 'POST':
        date = request.POST['date']
        book_name = request.POST['book_name']
        number_of_books = request.POST['number_of_books']
        amount = request.POST['amount']
        Sale.objects.create(date=date, book_name=book_name, number_of_books=number_of_books, amount=amount)
        return redirect('home')

    sales = Sale.objects.values('date').annotate(total_amount=Sum('amount'))
    return render(request, 'accounts/home.html', {'sales': sales})




def export_sales_to_excel(request, date):
    sales = Sale.objects.filter(date=date)
    
    # Create a workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Book Name', 'Number of Books', 'Amount'])
    
    # Add sales data to the worksheet
    for sale in sales:
        ws.append([sale.book_name, sale.number_of_books, sale.amount])
    
    # Save the workbook to a HttpResponse
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=sales_{date}.xlsx'
    wb.save(response)
    
    return response
