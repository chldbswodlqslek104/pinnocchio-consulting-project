console.log("hello");

       
const listElement = document.querySelector(".table-component__list__element:first-child");
const chare = document.querySelector("main>span");
let ha = 1;

const handleListClick = ()=>{
    ha += 1;
    let number = 0;
    for(number =1; number < 5;number++){
        const main = document.querySelector(`.table-component__list__element:nth-child(${number})`);
        main.innerHTML = `<li>
        <span>공공인재학부${number}</span>
        <!--todo: icon chevron-right-->
    </li>`
    }
    chare.innerText = `${ha}/5`
}


listElement.addEventListener("click",handleListClick);



        