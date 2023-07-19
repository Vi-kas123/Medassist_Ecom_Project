from django.shortcuts import render
from . import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def BrandInterface(request):
    return render(request,"BrandInterface.html")

@xframe_options_exempt
def SubmitBrand(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandname = request.POST['brandname']
        contactperson = request.POST['contactperson']
        mobilenumber= request.POST['mobilenumber']
        brandicon = request.FILES['brandicon']
        status = request.POST['status']

        Q = "insert into brands(categoryid,subcategoryid,brandname,contactperson,mobilenumber,brandicon,status) values({0},{1},'{2}','{3}','{4}','{5}',{6})".format(categoryid,subcategoryid,brandname,contactperson,mobilenumber,brandicon,status)
        F = open("e:/medassist_ecom/assets/" + brandicon.name, 'wb')
        for chunk in brandicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'BrandInterface.html', {'message': 'Record Submitted'})

    except Exception as e:
        print("Error", e)
        return render(request, 'BrandInterface.html', {'message': 'Fail to Submit record'})

@xframe_options_exempt
def Display_All_Brand(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        Q = "select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=B.subcategoryid) as scname from brands B"
        CMD.execute(Q)
        records = CMD.fetchall()
        # print(records)
        DB.close()
        return render(request, 'DisplayAllBrands.html', {'records': records})

    except Exception as e:
            return render(request, 'DisplayAllBrands.html', {'records', None})

@xframe_options_exempt
def Fetch_All_Brand_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      subcategoryid=request.GET['subcategoryid']
      Q = "select * from brands where subcategoryid={0}".format(subcategoryid)
      CMD.execute(Q)
      records = CMD.fetchall()
      #print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error :",e)
      return render(request, 'ProductInterface.html', {'data': None})

@xframe_options_exempt
def Delete_Brand(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    brandid = request.GET['brandid']

    Q="delete from brands where  brandid={0}".format(brandid)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_BrandIcon(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        brandid = request.POST['brandid']
        brandicon = request.FILES['brandicon']

        Q = "update brands set brandicon='{0}' where brandid={1}".format(
            brandicon.name,brandid)
        #print("Quer: ",Q)
        F = open("e:/medassist_ecom/assets/" + brandicon.name, 'wb')

        for chunk in brandicon.chunks():
            F.write(chunk)

        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error1 :", e)
        return JsonResponse({'result': False}, safe=False)

@xframe_options_exempt
def Edit_Brand(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        subcategoryid = request.GET['subcategoryid']
        brandname = request.GET['brandname']
        categoryid = request.GET['categoryid']
        brandid=request.GET['brandid']
        contactperson = request.GET['contactperson']
        mobilenumber = request.GET['mobilenumber']
        status = request.GET['status']
        print(status)
        Q = "update brands set brandname='{0}',categoryid={1},subcategoryid={2},contactperson='{3}',mobilenumber='{4}',status='{5}' where brandid={6}".format(
            brandname,categoryid,subcategoryid,contactperson,mobilenumber,status,brandid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error :", e)
        return JsonResponse({'result': False}, safe=False)
