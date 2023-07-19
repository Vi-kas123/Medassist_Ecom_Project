from django.shortcuts import render
from . import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Electro_Product_Interface(request):
    return render(request,"ElectroProductInterface.html")
@xframe_options_exempt
def Submit_All_Electro_Products(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        productname = request.POST['productname']
        price = request.POST['price']
        offerprice = request.POST['offerprice']
        brandid = request.POST['brandid']
        quantity = request.POST['quantity']
        rating = request.POST['rating']
        status = request.POST['status']
        producticon = request.FILES['producticon']
        salestatus=request.POST['salestatus']


        Q = "insert into electroproducts(categoryid,subcategoryid,brandid,salestatus,productname,price,offerprice,rating,quantity,status,producticon) values({0},{1},{2},'{3}','{4}','{5}',{6},'{7}','{8}','{9}','{10}')".format(
            categoryid,subcategoryid,brandid,salestatus,productname,price,offerprice,rating,quantity,status,producticon)
        F = open("e:/medassist_ecom/assets/" + producticon.name, 'wb')
        for chunk in producticon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'ElectroProductInterface.html', {'message': 'Record Submitted'})

    except Exception as e:
        print("Error", e)
        return render(request, 'ElectroProductInterface.html', {'message': 'Fail to Submit record'})
@xframe_options_exempt
def Display_All_Electro_Products(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        Q = "select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=B.subcategoryid) as scname,(select k.brandname from brands k where k.brandid=B.brandid) as bname from electroproducts B"
        CMD.execute(Q)
        records = CMD.fetchall()
        # print(records)
        DB.close()
        return render(request, 'DisplayAllElectroProducts.html', {'records': records})

    except Exception as e:
            return render(request, 'DisplayAllElectroProducts.html', {'records', None})

@xframe_options_exempt
def Delete_Electro_Product(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    productid = request.GET['productid']

    Q="delete from electroproducts where  productid={0}".format(productid)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Edit_Electro_Product(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productname = request.GET['productname']
        price = request.GET['price']
        offerprice = request.GET['offerprice']
        brandid = request.GET['brandid']
        quantity = request.GET['quantity']
        rating = request.GET['rating']
        status = request.GET['status']
        salestatus = request.GET['salestatus']
        productid=request.GET['productid']


        Q = "update electroproducts set categoryid={0},subcategoryid={1},brandid={2},salestatus='{3}',productname='{4}',price='{5}',offerprice='{6}',rating='{7}',quantity='{8}',status='{9}' where productid={10}".format(
            categoryid,subcategoryid,brandid,salestatus,productname,price,offerprice,rating,quantity,status,productid)

        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error :", e)
        return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def Edit_Electro_ProductIcon(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        productid = request.POST['productid']
        producticon = request.FILES['producticon']

        Q = "update electroproducts set producticon='{0}' where productid={1}".format(
            producticon.name,productid)
        print("Quer: ",Q)
        F = open("e:/medassist_ecom/assets/" +producticon.name, 'wb')

        for chunk in producticon.chunks():
            F.write(chunk)

        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error1 :", e)
        return JsonResponse({'result': False}, safe=False)
