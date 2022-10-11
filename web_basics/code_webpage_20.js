function exp(s){
    document.getElementById('ex').value+=s;
}

function evaluation(s){

    if(s.charAt(0)>='a' && s.charAt(0)<='z'){
        document.getElementById('ex').value=eval(`with(Math) ${s}`);
    }

    else{
        document.getElementById('ex').value=eval(s);
    }
}

function rem(){
    sol=document.getElementById('ex').value
    document.getElementById('ex').value=sol.slice(0,sol.length-1);
}

function clean(){
    document.getElementById('ex').value="";
}

function deg(s){
      return s*(Math.PI/180);
}
