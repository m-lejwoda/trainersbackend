function getdropdown(evt){
    console.log(evt.currentTarget)
    console.log("dropdown")
}

var element_dropdown = document.querySelector('.todaytrainings__element');
element_dropdown.addEventListener("click",getdropdown);

document.addEventListener("click", function(){
    document.getElementById("demo").innerHTML = "Hello World";
    console.log("click")
}); 

