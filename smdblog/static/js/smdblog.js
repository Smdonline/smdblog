var hideBtn=document.getElementById("hideBtn");
var tagList=document.getElementById("tags");
hideBtn.onclick=apasa;
function apasa(){
    copii=tagList.getElementsByTagName("a");
    if(copii.length>2){
        for(var i=2;i<copii.length;i++){
            copii[i].classList.toggle("d-none");
        }
        if (this.innerHTML === "+"){
            this.innerHTML = "-";
    } else{
        this.innerHTML = "+";
    }
    }

}