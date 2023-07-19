"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Category_Controller
from . import Subcategory_Controller
from . import BrandController
from . import ProductController
from . import AdminLoginController
from . import ElectroProductController
from . import UserInterface
from . import AdminLoginElectrocart
from . import ElectroUserRegistration
from . import ElectroUserInterface
urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoryinterface/',Category_Controller.Category_Interface),
    path('submitcategory', Category_Controller.Submit_Category),
    path('subcategoryinterface/',Subcategory_Controller.Subcategory_Interface),
    path('submitsubcategory',Subcategory_Controller.Submit_subcategory),
    path('displayallcategories',Category_Controller.Display_All_Category),
    path('displayallsubcategories', Subcategory_Controller.Display_All_Subcategory),
    path('editcategory/', Category_Controller.Edit_Category),
    path('deletecategory/', Category_Controller.Delete_Category),
    path('editsubcategory/', Subcategory_Controller.Edit_subcategory),
    path('deletesubcategory/', Subcategory_Controller.Delete_SubCategory),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('editsubcategoryicon', Subcategory_Controller.Edit_subcategoryIcon),
    path('fetchallcategoryjson',Category_Controller.Fetch_All_Category_JSON),
    path('brandinterface',BrandController.BrandInterface),
    path('fetchallsubcategoryjson',Subcategory_Controller.Fetch_All_SubCategory_JSON),
    path('submitbrand',BrandController.SubmitBrand),
    path('displayallbrands',BrandController.Display_All_Brand),
    path('productinterface',ProductController.ProductInterface),
    path('fetchallbrandjson',BrandController.Fetch_All_Brand_JSON),
    path('submitproduct',ProductController.Submit_All_Products),
    path('displayallproducts',ProductController.Display_All_Products),
    path('deletebrand/',BrandController.Delete_Brand),
    path('editbrandicon', BrandController.Edit_BrandIcon),
    path('editbrand/', BrandController.Edit_Brand),
    path('editproducticon', ProductController.Edit_ProductIcon),
    path('deleteproduct/', ProductController.Delete_Product),
    path('editproduct/', ProductController.Edit_Product),
    path('adminlogin', AdminLoginController.Login_Interface),
    path('admincheck',AdminLoginController.Check_Admin),
    path('adminlogout',AdminLoginController.Admin_Logout),




    path('electroproductinterface',ElectroProductController.Electro_Product_Interface),
    path('submitelectroproduct',ElectroProductController.Submit_All_Electro_Products),
    path('displayallelectroproducts',ElectroProductController.Display_All_Electro_Products),
    path('deleteelectroproduct/',ElectroProductController.Delete_Electro_Product),
    path('editelectroproduct/',ElectroProductController.Edit_Electro_Product),
    path('editelectroproducticon',ElectroProductController.Edit_Electro_ProductIcon),
    path('electroadminlogin',AdminLoginElectrocart.Electro_Login_Interface),
    path('electroadminlogout', AdminLoginElectrocart.Electro_Admin_Logout),
    path('electroadmincheck', AdminLoginElectrocart.Electro_Check_Admin),
    path('electrouserregistration', ElectroUserRegistration.User_Registration),
    path('submituserdata/', ElectroUserRegistration.SubmitUserData),
    # path('my_shopping_cart/', ElectroUserInterface.MyShoppingCart),

    #User paths
    path('home/',UserInterface.Index),
    path('fetch_all_user_category/',UserInterface.Fetch_All_Category_JSON),
    path('fetch_all_user_subcategory/', UserInterface.Fetch_All_SubCategory_JSON),
    path('fetch_all_products/',UserInterface.Fetch_ALl_Products),
    path('buy_product', UserInterface.BuyProduct),
    path('add_to_cart', UserInterface.Addtocart),
    path('fetch_cart/', UserInterface.FetchCart),
    path('remove_from_cart/', UserInterface.RemoveFromCart),
    path('my_shopping_cart/', UserInterface.MyShoppingCart),
    path('check_user_mobileno/',UserInterface.CheckUserMobileno),
    path('insert_user/', UserInterface.InsertUser),
    path('check_user_mobileno_for_address/',UserInterface.CheckUserMobilenoForAddress),
    path('insert_user_address/', UserInterface.InsertUserAddress),
    path('userdashboard/',UserInterface.userdashboard),

    #Electro user path
    path('home1/',ElectroUserInterface.Electr_Index),
    path('fetch_all_electro_user_category/',ElectroUserInterface.Electro_Fetch_All_Category_JSON),
    path('fetch_all_electro_user_subcategory/', ElectroUserInterface.Electro_Fetch_All_SubCategory_JSON),
    path('fetch_all_electro_products/',ElectroUserInterface.Electro_Fetch_ALl_Products),
    path('electro_buy_product/', ElectroUserInterface.Elecro_BuyProduct),
    path('electro_add_to_cart/', ElectroUserInterface.ElectroAddtocart),
    path('electro_fetch_cart/',ElectroUserInterface.ElectroFetchCart),
    path('electro_remove_from_cart/', ElectroUserInterface.ElectroRemoveFromCart)

]
