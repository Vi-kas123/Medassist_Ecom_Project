$(document).ready(function(){

 var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1);
//      alert(hashes)
      var i=hashes.indexOf(":")+1
      var j=hashes.indexOf(",")
//      alert(i+","+j)
      pid=hashes.slice(i,j)

      $.getJSON('/fetch_cart',function(data){
     //alert(data.data)
 var cart = JSON.parse(data.data)
     var key=Object.keys(cart)
     $('#shoppingcart').html(`(${key.length}) Articles &nbsp;&nbsp;&nbsp;&nbsp;`)
//       alert(key.includes(pid))
       if(key.includes(pid)){
           $('.addtocart').hide()
           $('#qtycomponent').show()
           $('#qty').html(cart[pid]['qty'])
       }
       else
       {
               $('#qtycomponent').hide()

       }
     })
     $('#qtycomponent').hide()
     $("#user-menu-button").click(function(){
          $('#dropdown').toggle()
     })
     $.getJSON('http://localhost:8000/fetch_all_user_category',function(data){
       var htm=''
       //alert(JSON.stringify(data.data))
       var htm1=''
       data.data.map((item)=>{
           htm+=`<li><a href="http://localhost:8000/home" style="text-decoration: none; color: black;">${item.categoryname}</a></li>`
           htm1+=`<li><a href="/home" style="text-decoration: none; color: black;">${item.categoryname}</a></li>`

          // htm+=`<a href="#" class="bg-gray-900 text-white px-3 py-2 rounded-md text-sm font-medium" aria-current="page">${item.categoyname}</a>`
       })
       $('.mainmenu').html(htm)
       $('.mainmenu1').html(htm1)

     })


      $.getJSON('http://localhost:8000/fetch_all_products',function(data){
       htm=''

       data.data.map(item=>{
         var price
         var offerprice
         var save
         if(item.offerprice>0)
         {
              price="<s style='color: red;'>"+item.price+"</s>"
              offerprice=item.offerprice
              save=item.price-item.offerprice
         }
         else
         {
            offer=item.price
            price="<div</div>"
            save="<div></div>"
         }

         var data=JSON.stringify(item)
//         alert(data.length)
         htm+=`<a href='http://localhost:8000/buy_product?product=${data}' style="text-decoration: none;color: black;" ><div style="display: flex; flex-direction: column; margin: 10px;align-items: center; width: 250px; height: 300px; padding: 5px; border: 1px solid #bdc3c7;box-shadow: 2px 2px #ecf0f1;elevation: below;border-radius: 10px;">
      <div><img src="http://localhost:8000/static/${item.producticon}" style="width: 150px;height: 150px;"></div>

      <div style="padding: 5px; display: flex;">
         <div style="font-weight: bolder;width:200px;text-align:left;">${item.productname} ${item.scname}</div>
      </div>
      <div style="width:200px;text-align:left;font-size:10px;"><i>Mkt: ${item.bname}</i></div>
      <div style="width:200px;text-align:left;font-weight: bold;">MRP: &#8377 ${price}</div>
      <div style="width:200px;text-align:left;font-weight: bold;">Offer: &#8377 ${offerprice}</div>
      <div style="width:200px;text-align:left;color: green;font-weight: bold;"><i>You save &#8377 ${save}</i></div>


      </div></a>`
     })
       $('#productlist').html(htm)
     })



         $.getJSON('http://localhost:8000/fetch_all_user_subcategory',function(data){
       var htm=''
       //alert(JSON.stringify(data.data))
       data.data.map((item)=>{
           htm+=`<div style="width: 400px;margin: 5px; padding: 10px; background: #f5f6fa; height: 80px; border-radius: 10px;display: flex;flex-direction: row;">`
           htm+=`<div style="padding: 5px;"><img src="/static/${item.subcategoryicon}" width="40" height="40"></div>`
           htm+=`<div><div style="padding: 5px;font-weight:bold;display: flex;flex-direction: column;">${item.subcategoryname}</div><div style="color: green">Save upto 15%</div></div>`
           htm+=`</div>`
       })
              $('#subcategorylist').html(htm)

       })
 $('.plus').click(function(){
           var v=$('#qty').html()
           if(v<=4){
             v++}
           $('#qty').html(v)

          cartContainer($(this).attr('product'),$('#qty').html())

       })

    $('.minus').click(function(){
           var v=$('#qty').html()
           if(v>=1){
              v--}
           if(v==0)
           {
               $('.addtocart').show()
            $('#qtycomponent').hide()
//           alert($(this).attr('productid'))
             removeCart($(this).attr('productid'))
             alert($(this).attr('productid'))
           }
           else{
           $('#qty').html(v)
//           alert(v)

            cartContainer($(this).attr('product'),$('#qty').html())
              }
       })
       $('.addtocart').click(function(){
            $('.addtocart').hide()
            $('#qtycomponent').show()
            $('#qty').html(1)
            cartContainer($(this).attr('product'),$('#qty').html())
       })

     function cartContainer(product,qty){
     $.getJSON('/add_to_cart',{'product': product,'qty': qty},function(data){
     alert(JSON.stringify(data))
     var cart = JSON.parse(data.data)
//     console.log("JSON.parse",data.data)
     var key=Object.keys(cart)
     $('#shoppingcart').html(`(${key.length}) Articles &nbsp;&nbsp;&nbsp;&nbsp;`)
})
     }

    function removeCart(productid){
        $.getJSON('/remove_from_cart',{'productid': productid},function(data){
//                 alert("Removed")
                var cart = JSON.parse(data.data)
     var key=Object.keys(cart)
     $('#shoppingcart').html(`(${key.length}) Articles &nbsp;&nbsp;&nbsp;&nbsp;`)
            })
    }

} )
