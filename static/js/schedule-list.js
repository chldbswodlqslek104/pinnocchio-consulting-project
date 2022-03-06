const listElement = document.querySelectorAll(
  ".table-component__list__element"
);
let scheduleElement = document.querySelectorAll(".result-schedule__element");

let length = scheduleElement.length;

//api 요청
// console.log(JSON.parse(localStorage.getItem("cast")));

const handleListClick = (event) => {
  event.preventDefault();
  const selectedElement = document.createElement("li");
  selectedElement.classList.add("table-component__list__element");
  selectedElement.classList.add("result-schedule__element");

  const inText = event.path[0].innerText;
  console.log(event);

  selectedElement.innerHTML = `<a>
        <span>${inText}</span>
        <i class="fa-solid fa-chevron-right fa-lg"></i>
    </a>`;
  document.querySelector(".result-schedule").appendChild(selectedElement);

  scheduleElement = document.querySelectorAll(".result-schedule__element");
  length = scheduleElement.length;
  console.log(scheduleElement);

  for (let i = 0; i < length; i++) {
    scheduleElement[i].addEventListener("click", handleS);
  }
};

const handleS = (event) => {
  event.preventDefault();
  const chosenItem = event.currentTarget;
  console.log(chosenItem.parentNode.removeChild(chosenItem));
};

for (let i = 0; i < listElement.length; i++) {
  listElement[i].addEventListener("click", handleListClick);
}
