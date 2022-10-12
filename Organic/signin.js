
document.querySelector('#name , #uname').addEventListener("input",(event)=>{
    let u=document.getElementById('name').value;
    let ru=document.getElementById('uname').value;
    let uregex=/([A-Z]{1})(\w{5,20})/;
    const un=document.querySelector('#oname , #roname');
   
    if((!uregex.test(u) && u.length>0) || (!uregex.test(ru) && ru.length>0)){
        
        un.style.display='block';
    }

    else{
        un.style.display='none';
        console.log("valid")
    }
});

document.querySelector('#pass,#rpass').addEventListener("input",(event)=>{
    let p=document.getElementById('pass').value;
    let pregex=/[\w@#$%&]{8,24}/;
    const pn=document.querySelector('#opass , #ropass');

    if(!pregex.test(p)&& p.length>0){
        
        pn.style.display='block';
    }

    else{
        pn.style.display='none';
        console.log("valid")
    }
});

function change_s(){
    document.getElementById('signin').style.display='none';
    
    document.getElementById('signup').style.display='flex';

}
