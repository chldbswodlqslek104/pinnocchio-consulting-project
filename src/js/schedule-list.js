const listElement = document.querySelectorAll(".table-component__list__element");


const handleListClick = (event) => {
    console.log("hello");
    const test = document.createElement("div");
    const inText = event.path[0].innerText;
    console.log(event);
    test.innerHTML =`<a href = "#" class="table-component__list__element">
    <li>
        <span>${inText}</span>
        <!--todo: icon chevron-right-->
    </li>
</a>`;
    document.querySelector(".result-schedule").appendChild(test);
}

for(let i = 0; i<4; i++){
    listElement[i].addEventListener("click",handleListClick);
}