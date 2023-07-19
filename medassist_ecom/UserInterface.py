from django.shortcuts import render
from . import pool
import json
from django.http import JsonResponse
from urllib.parse import unquote  # url decode

def Addtocart(request):
   try:
     products = request.GET['product']
     qty=request.GET['qty']
     products = products.replace("'","\"")
     products = json.loads(products)
     products['qty']=qty
     # qty=request.GET['qty']
     # products['qty']=qty
     # print('UPDATED PRODUCTS : ',type(products))
     # print('UPDATED PRODUCTS : ',products)
     #create cart container using session
     try:
         CART_CONTAINER=request.session['CART_CONTAINER']
         CART_CONTAINER[str(products['productid'])]=products
         request.session['CART_CONTAINER'] = CART_CONTAINER
         print(CART_CONTAINER)

     except:
         CART_CONTAINER={}
         CART_CONTAINER={str(products['productid']):products}
         request.session['CART_CONTAINER']=CART_CONTAINER
         print("Error : ")
     # print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
     return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr : ",err)
     return JsonResponse({'data':[]}, safe="False")

def RemoveFromCart(request):
   try:
       productid = request.GET['productid']
       CART_CONTAINER=request.session['CART_CONTAINER']
       del CART_CONTAINER[productid]
       request.session['CART_CONTAINER'] = CART_CONTAINER
       # print("REMOVE CART_CONTAINER:",CART_CONTAINER)
       CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
       return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr : ",err)
     return JsonResponse({'data':[]}, safe="False")


def FetchCart(request):
   try:

     try:
         CART_CONTAINER=request.session['CART_CONTAINER']

     except:
         CART_CONTAINER={}
     # print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
     return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr : ",err)
     return JsonResponse({'data':[]}, safe="False")



def Index(request):
    return render(request,"index.html")


def MyShoppingCart(request):
    try:

        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
            total=0
            totalprice=0
            totalsaving=0
            for records in CART_CONTAINER.keys():
               amt=(CART_CONTAINER[records]['price']-CART_CONTAINER[records]['offerprice'])
               CART_CONTAINER[records]['save']=amt*int(CART_CONTAINER[records]['qty'])
               CART_CONTAINER[records]['productprice']=CART_CONTAINER[records]['offerprice']*int(CART_CONTAINER[records]['qty'])
               total+=CART_CONTAINER[records]['offerprice']*int(CART_CONTAINER[records]['qty'])
               totalprice+=CART_CONTAINER[records]['price']*int(CART_CONTAINER[records]['qty'])
               totalsaving+=CART_CONTAINER[records]['save']


        except Exception as err:
            print("Errroorrrr : ",err)
            CART_CONTAINER = {}


        print("My Shopping CART_CONTAINER:", CART_CONTAINER.values())
        #CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
        return render(request, "mycart.html",{'data': CART_CONTAINER.values(),'totalamount': total,'totalproducts':len(CART_CONTAINER.keys()),'totalprice': totalprice,'totalsaving': totalsaving})

    except Exception as err:
        print("Errorrr : ", err)
        return render(request, "mycart.html",{'data': {}})



def BuyProduct(request):
    product=unquote(request.GET['product'])
    product=json.loads(product)
    print("zzzzz",product,type(product))
    return render(request,"Buy_product.html",{'product':product})

def Fetch_All_Category_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from categories"
      CMD.execute(Q)
      records = CMD.fetchall()
      #print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error : ",e)
      return render(request, 'index.html', {'data': None})

def Fetch_ALl_Products(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        Q = "select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=B.subcategoryid) as scname,(select k.brandname from brands k where k.brandid=B.brandid) as bname from products B"
        CMD.execute(Q)
        products = CMD.fetchall()
        #print(records)
        DB.close()
        return JsonResponse({'data': products}, safe=False)

    except Exception as e:
        return JsonResponse({'data': []}, safe=False)

def Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from subcategories"
      CMD.execute(Q)
      records = CMD.fetchall()
      # print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error : ",e)
      return JsonResponse({'data': []}, safe=False)

def Fetch_All_Brand_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from brands"
      CMD.execute(Q)
      records = CMD.fetchall()
      # print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error : ",e)
      return JsonResponse({'data': []}, safe=False)

def  CheckUserMobileno(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from  users where mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('User:', record)
      if(record):
          return JsonResponse({'data': record,'status':True}, safe=False)
      else:
          return JsonResponse({'data':[], 'status': False}, safe=False)
      DB.close()

    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)

def  InsertUser(request):
    mobileno=request.GET['mobileno']
    emailid = request.GET['emailid']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    password = request.GET['password']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "insert into users values('{0}','{1}','{2}','{3}','{4}')".format(emailid,mobileno,firstname,lastname,password)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return JsonResponse({'status':True}, safe=False)


    except Exception as e:
      print('Error:', e)
      return JsonResponse({'status':False}, safe=False)


def  CheckUserMobilenoForAddress(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select UA.*,(select U.firstname from users U where U.mobileno=UA.mobileno) as firstname,(select U.lastname from users U where U.mobileno=UA.mobileno) as lastname  from  users_address UA where UA.mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('User:', record)
      if(record):
          return JsonResponse({'data': record,'status':True}, safe=False)
      else:
          return JsonResponse({'data':[], 'status': False}, safe=False)
      DB.close()

    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)


def  InsertUserAddress(request):
    mobileno=request.GET['mobileno']
    emailid = request.GET['emailid']
    address1 = request.GET['addressone']
    address2 = request.GET['addresstwo']
    landmark = request.GET['landmark']
    city = request.GET['city']
    state = request.GET['state']
    zipcode = request.GET['zipcode']

    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "insert into users_address(mobileno, emailid, address1, address2, landmark, city, state, zipcode) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(mobileno,emailid,address1,address2,landmark,city,state,zipcode)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return JsonResponse({'status':True}, safe=False)


    except Exception as e:
      print('Error:', e)
      return JsonResponse({'status':False}, safe=False)

def userdashboard(request):
    return render(request,'userdashboard.html')

