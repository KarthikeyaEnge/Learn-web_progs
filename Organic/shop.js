function quan_inc(c){
    const p=document.getElementsByClassName('quan')[c];
    
    const a=parseInt(p.value);
    p.value=a+1;

}
function quan_dec(c){
    const p=document.getElementsByClassName('quan')[c];
    
    const a=parseInt(p.value);
    
    if(a>0) p.value=a-1;
}

function scroll_right(c){
    const s=document.getElementsByClassName('scroll_menu')[c];
    s.scrollBy(300,0)
}

function scroll_left(c){
    const s=document.getElementsByClassName('scroll_menu')[c];
    s.scrollBy(-300,0)
}
