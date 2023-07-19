$(document).ready(function(){
   $.getJSON('http://localhost:8000/fetch_all_user_category',function(data){
       var htm=''
       data.data.map((item)=>{
           htm+=`<li><a href="http://localhost:8000/home">${item.categoryname}</a></li>`

       })
       $('.navigation').html(htm)

     })

})