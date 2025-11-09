from django.shortcuts import render, redirect
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ---------------------------
# Admin Login View
# ---------------------------
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

       
        if username == 'admin' and password == 'admin123':
            # Login success → Go to dashboard
            return redirect('admin_dashboard')
        else:
            
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})

    # GET request → show login page
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')



def add_employee(request):
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        userid = request.POST.get('userid')
        password = request.POST.get('password')

       
        Employee.objects.create(
            emp_id=emp_id,
            name=name,
            email=email,
            phone=phone,
            userid=userid,
            password=password
        )

        return render(request, 'admin_dashboard.html', {'msg': 'Employee added successfully!'})

    return redirect('admin_dashboard')


# ---------------------------
# 4️⃣ View All Employees
# ---------------------------
def view_employees(request):
    employees = Employee.objects.all()  # Fetch all records
    return render(request, 'view_employees.html', {'employees': employees})


# ---------------------------
# 5️⃣ User Login
# ---------------------------
def user_login(request):
    userid = request.data.get('userid')
    password = request.data.get('password')

    if Employee.objects.filter(userid=userid, password=password).exists():
        employee = Employee.objects.get(userid=userid)
        return Response({
            'status': 'success',
            'message': 'Login successful',
            'name': employee.name,
            'userid': employee.userid,
        })
    else:
        return Response({
            'status': 'error',
            'message': 'Invalid UserID or Password'
        }, status=400)
