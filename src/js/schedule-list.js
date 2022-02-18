const listElement = document.querySelectorAll(".table-component__list__element");
let scheduleElement = document.querySelectorAll(".result-schedule__element");

let length = scheduleElement.length;

const handleListClick = (event) => {
    // event.preventdefault();
    event.preventDefault();
    console.log("hello");
    const test = document.createElement("div");
    const inText = event.path[0].innerText;
    console.log(event);
    

    test.innerHTML =`<li class="table-component__list__element result-schedule__element">
    <a>
        <span>${inText}</span>
        <i class="fa-solid fa-chevron-right fa-lg"></i>
    </a>
</li>`;
    document.querySelector(".result-schedule").appendChild(test);

    scheduleElement = document.querySelectorAll(".result-schedule__element");
    length = scheduleElement.length;
    console.log(scheduleElement);
    
    for(let i = 0; i<length; i++){
        scheduleElement[i].addEventListener("click",handleS);
    }
}

const handleS = (event) => {
    event.preventDefault();
    const chosenItem = event.currentTarget.parentNode
    console.log(chosenItem.parentNode.removeChild(chosenItem));
}




for(let i = 0; i<listElement.length; i++){
    listElement[i].addEventListener("click",handleListClick);
}

