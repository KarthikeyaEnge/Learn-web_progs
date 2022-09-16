
function valid(){
    user=prompt('Enter Your Name:');
    pass=prompt('Enter your Password');
    u=document.getElementById('name').value;
    p=document.getElementById('pass').value;
    if(u===user && p===pass ){
        document.getElementById('out').value='successfull';
        
    }

    else{
        document.getElementById('out').value='Un-successfull';
    }
}



function evaluation(s){
    document.getElementById('ex').value=eval(s);
}

function exp(s){
    document.getElementById('ex').value+=s
}

function remove(){
    sol=document.getElementById('ex').value
    document.getElementById('ex').value=sol.slice(0,sol.length-1);
}
