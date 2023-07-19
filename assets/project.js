$(document).ready(function () {
    $.getJSON('http://localhost:8000/fetchallcategoryjson',function(data){
//         alert(JSON.stringify(data))
          var records=data.data
//          alert(JSON.stringify(data.data)
          records.map((item)=>{
                 $('#categoryid').append($("<option>").text(item.categoryname).val(item.categoryid))

          })
          $('select').formSelect();
    })

});