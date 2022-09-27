function serv_slidel(){
       const p=document.getElementsByClassName('serv_slide')[0];
       p.scrollBy(-700,0)
}

function serv_slider(){
    const p=document.getElementsByClassName('serv_slide')[0];
    p.scrollBy(700,0);
}

function next_slide(c){
    const p=document.getElementsByClassName('serv_slide')[0];
    const l=document.getElementsByClassName('serv_card') [c];

    l.style.display='none';
}

function prev_slide(c){
    const l=document.getElementsByClassName('serv_card') [c];
    l.style.display='flex'
}