$(document).ready(function () {
    $.getJSON('http://localhost:8000/fetchallcategoryjson',function(data){
//         alert(JSON.stringify(data))
          var records=data.data
          records.map((item)=>{
                 $('#categoryid').append($("<option>").text(item.categoryname).val(item.categoryid))

          })
          $('select').formSelect();
    })


    $('#categoryid').change(function(){
     //alert("X")
     $('#subcategoryid').empty()
          $.getJSON('http://localhost:8000/fetchallsubcategoryjson',{categoryid:$('#categoryid').val()},function(data){
           $('#subcategoryid').append($("<option>").text('-Select SubCategory-'))
           //alert(JSON.stringify(data))
          var records=data.data
//          alert(JSON.stringify(data.data)
          records.map((item)=>{
                 $('#subcategoryid').append($("<option>").text(item.subcategoryname).val(item.subcategoryid))

          })
          $('select').formSelect();
    })

    })
    $('#subcategoryid').change(function(){
     //alert("X")
     $('#brandid').empty()
          $.getJSON('http://localhost:8000/fetchallbrandjson',{subcategoryid:$('#subcategoryid').val()},function(data){
           $('#brandid').append($("<option>").text('-Select Brand-'))
           //alert(JSON.stringify(data))
          var records=data.data
//          alert(JSON.stringify(data.data)
          records.map((item)=>{
                 $('#brandid').append($("<option>").text(item.brandname).val(item.brandid))

          })
          $('select').formSelect();
    })

    })

})