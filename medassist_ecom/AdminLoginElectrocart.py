from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def Electro_Login_Interface(request):
    return render(request,"index1.html")

def Electro_Admin_Logout(request):
    return render(request,"index1.html")

def Electro_Check_Admin(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        email = request.POST['emailid']
        password = request.POST['password']

        Q = "select * from adminlogin where email='{0}' and password='{1}'".format(email,password)
        CMD.execute(Q)
        print(Q)
        row = CMD.fetchone()
        #print(Q)
        print(row)

        if(row):

            return render(request, 'DashBoard1.html',{'AdminData':row})
        else:
            return render(request, 'index1.html', {'message': 'Invalid EmailId/Password'})
        DB.close()

    except Exception as e:
        print("Error", e)
        return render(request, 'index1.html', {'message': 'Something Went Wrong'})
