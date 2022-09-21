function valid(){
    let u=document.getElementById('name').value;
    let p=document.getElementById('pass').value;
     
    let uregex=/^[[A-Z]{1}[a-z]{5,8}]\ $/;

    if(uregex.test(u)){
        console.log('successfull');
    }

}