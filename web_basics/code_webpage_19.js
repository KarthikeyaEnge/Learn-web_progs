document.addEventListener('readystatechange',(event) =>{
     if(event.target.readyState==='complete'){
              Init_ev()
     }
})

/**
 * element.addEventListener('eventName',function,usecapture=>(true/false))
 */

const Init_ev=()=>{
    const sec_1=document.querySelector('.sec_1')
    const sec_2=document.querySelector('.sec_2')
    const sec_3=document.querySelector('.sec_3')
    const t=document.querySelector('h2')

    sec_1.addEventListener('click',(event)=>{
        sec_1.style.backgroundColor="limegreen";
    })
    


    sec_2.addEventListener('click',(event)=>{
        sec_2.style.backgroundColor="lightblue";  
    },true)

    sec_3.addEventListener('mouseleave',(event)=>{
        sec_3.style.backgroundColor="peach";
    },true)

    t.addEventListener('click',(event)=>{
        t.textContent="cooridnates X:"+event.clientX+" Y: "+event.clientY;
    },true)

}
