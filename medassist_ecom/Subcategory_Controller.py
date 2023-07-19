from django.shortcuts import render
from . import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Subcategory_Interface(request):
    return render(request,'SubcategoryInterface.html')
@xframe_options_exempt
def Submit_subcategory(request):
     try:
         DB,CMD=pool.ConnectionPooling()
         categoryid = request.POST['categoryid']
         subcategoryname=request.POST['subcategoryname']
         subcategoryicon=request.FILES['subcategoryicon']

         Q="insert into subcategories(categoryid,subcategoryname,subcategoryicon) values('{0}','{1}','{2}')".format(categoryid,subcategoryname,subcategoryicon.name)
         F=open("e:/medassist_ecom/assets/"+subcategoryicon.name,'wb')

         for chunk in subcategoryicon.chunks():
             F.write(chunk)

         F.close()
         CMD.execute(Q)
         DB.commit()
         DB.close()
         return render(request,"SubcategoryInterface.html",{'message':'Record Submitted successfully'})


     except Exception as e:
         print("Error :",e)
         return render(request,"SubcategoryInterface.html",{'message':'Failed to Submit Record'})

@xframe_options_exempt
def Display_All_Subcategory(request):
    try:
      DB,CMD=pool.ConnectionPooling()
      Q="select S.*,(select C.categoryname from categories C where C.categoryid=S.categoryid) as cname from subcategories S"
      CMD.execute(Q)
      records=CMD.fetchall()
      #print(records)
      DB.close()
      return render(request,'DisplayAllSubcategories.html',{'records':records})


    except Exception as e:
        return render(request,'DisplayAllSubcategories.html',{'records',None})

@xframe_options_exempt
def Edit_subcategory(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        subcategoryid = request.GET['subcategoryid']
        subcategoryname = request.GET['subcategoryname']
        categoryid = request.GET['categoryid']

        Q = "update subcategories set subcategoryname='{0}',categoryid={1} where subcategoryid={2}".format(
            subcategoryname,categoryid,subcategoryid)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error :", e)
        return JsonResponse({'result': False}, safe=False)

@xframe_options_exempt
def Delete_SubCategory(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    subcategoryid = request.GET['subcategoryid']

    Q="delete from subcategories where  subcategoryid={0}".format(subcategoryid)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)








# from django.shortcuts import render
# from . import pool
# def Category_Interface(request):
#     return render(request,'SubcategoryInterface.html')
# def Submit_Category(request):
#   try:
#     DB,CMD=pool.ConnectionPooling()
#     categoryid=request.POST['categoryid']
#     subcategoryname=request.POST['subcategoryname']
#     subcategoryicon=request.POST['subcategoryicon']
#     Q="insert into categories(categoryname,categoryicon) values('{0}','{1}')".format(categoryname,categoryicon)
#     CMD.execute(Q)
#     DB.commit()
#     DB.close()
#     return render(request, 'CategoryInterface.html',{'message':'Record Submitted Succesfully'})
#   except Exception as e:
#       print("Error:",e)
#       return render(request, 'CategoryInterface.html', {'message': 'Fail to Submit Record'})


def Edit_subcategoryIcon(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        subcategoryid = request.POST['subcategoryid']
        subcategoryicon = request.FILES['subcategoryicon']

        Q = "update subcategories set subcategoryicon='{0}' where subcategoryid={1}".format(
            subcategoryicon.name,subcategoryid)
        #print("Quer: ",Q)
        F = open("e:/medassist_ecom/assets/" + subcategoryicon.name, 'wb')

        for chunk in subcategoryicon.chunks():
            F.write(chunk)

        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error1 :", e)
        return JsonResponse({'result': False}, safe=False)

def Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      categoryid=request.GET['categoryid']
      Q = "select * from subcategories where categoryid={0}".format(categoryid)
      CMD.execute(Q)
      records = CMD.fetchall()
      #print(records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)

    except Exception as e:
      print("Error :",e)
      return render(request, 'BrandInterface.html', {'data': None})

