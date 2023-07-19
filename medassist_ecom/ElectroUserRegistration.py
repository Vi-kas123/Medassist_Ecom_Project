from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def User_Registration(request):
    return render(request,"ElectroUserRegistration.html")

def SubmitUserData(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        gender = request.GET['gender']
        number= request.GET['number']
        password = request.GET['password']
        cpassword = request.GET['cpassword']

        Q = "insert into userregistration(firstname,lastname,number,gender,password,cpassword,email) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(fname,lname,number,gender,password,cpassword,email)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'ElectroUserRegistration.html', {'message': 'Record Submitted'})

    except Exception as e:
        print("Error", e)
        return render(request, 'ElectroUserRegistration.html', {'message': 'Fail to Submit record'})

