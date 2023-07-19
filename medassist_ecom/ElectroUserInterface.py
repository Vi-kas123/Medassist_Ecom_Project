from django.shortcuts import render
from . import pool
import json
from django.http import JsonResponse
from urllib.parse import unquote  # url decode

def ElectroAddtocart(request):
   try:
     products = unquote(request.GET['product'])
     qty=request.GET['qty']
     products = products.replace("'","\"")
     products = json.loads(products)
     products['qty']=qty
     # qty=request.GET['qty']
     # products['qty']=qty
     # print('UPDATED PRODUCTS : ',type(products))
     print('UPDATED PRODUCTS : ',products)
     #create cart container using session
     try:
         CART_CONTAINER=request.session['CART_CONTAINER']
         CART_CONTAINER[str(products['productid'])]=products
         request.session['CART_CONTAINER'] = CART_CONTAINER

     except:
         CART_CONTAINER={}
         CART_CONTAINER={str(products['productid']):products}
         request.session['CART_CONTAINER']=CART_CONTAINER
         print("Error add1: ")
     print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
     return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr add2: ",err)
     return JsonResponse({'data':[]}, safe="False")

def ElectroRemoveFromCart(request):
   try:
       productid = request.GET['productid']
       CART_CONTAINER=request.session['CART_CONTAINER']
       del CART_CONTAINER[productid]
       request.session['CART_CONTAINER'] = CART_CONTAINER
       print("REMOVE CART_CONTAINER:",CART_CONTAINER)
       CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
       return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr remove  : ",err)
     return JsonResponse({'data':[]}, safe="False")


def MyShoppingCart(request):
    try:

        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
        except:
            print("Errroorrrr")
            CART_CONTAINER = {}


        print("My Shopping CART_CONTAINER:", CART_CONTAINER.values())
        #CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
        return render(request, "electromycart.html",{'data': CART_CONTAINER.values()})

    except Exception as err:
        print("Errorrr : ", err)
        return render(request, "electromycart.html",{'data': {}})



def ElectroFetchCart(request):
   try:

     try:
         CART_CONTAINER=request.session['CART_CONTAINER']

     except:
         CART_CONTAINER={}
     print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")
     return JsonResponse({'data': CART_CONTAINER },safe="False")

   except Exception as err:
     print("Errorrr fetch: ",err)
     return JsonResponse({'data':[]}, safe="False")




def Electr_Index(request):
    return render(request,"Electroindex.html")

def Elecro_BuyProduct(request):
    product=unquote(request.GET['product'])
    product=json.loads(product)
    print("zzzzz",product,type(product))
    return render(request,"Buy_Electro_product.html",{'product':product})

def Electro_Fetch_All_Category_JSON(request):
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
      return render(request, 'Electroindex.html', {'data': None})

def Electro_Fetch_ALl_Products(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        Q = "select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select s.subcategoryname from subcategories s where s.subcategoryid=B.subcategoryid) as scname,(select k.brandname from brands k where k.brandid=B.brandid) as bname from electroproducts B"
        CMD.execute(Q)
        products = CMD.fetchall()
        #print(records)
        DB.close()
        return JsonResponse({'data': products}, safe=False)

    except Exception as e:
        return JsonResponse({'data': []}, safe=False)

def Electro_Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      Q = "select * from subcategories"
      CMD.execute(Q)
      records = CMD.fetchall()
      print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error : ",e)
      return JsonResponse({'data': []}, safe=False)

