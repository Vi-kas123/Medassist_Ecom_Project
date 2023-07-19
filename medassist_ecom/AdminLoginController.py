from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def Login_Interface(request):
    return render(request,"Adminlogin.html")

def Admin_Logout(request):
    return render(request,"Adminlogin.html")


def Check_Admin(request):
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
            return render(request, 'DashBoard.html',{'AdminData':row})
        else:
            return render(request, 'Adminlogin.html', {'message': 'Invalid EmailId/Password'})
        DB.close()

    except Exception as e:
        print("Error", e)
        return render(request, 'Adminlogin.html', {'message': 'Something Went Wrong'})
