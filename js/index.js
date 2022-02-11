console.log("hello");

       
const listElement = document.querySelectorAll(".table-component__list__element");
const listTitle = document.querySelector(".table-component__header h4");
const progressNum = document.querySelector("main>span");
const optionList ={
    title : {
        department : "내 소속 학과는?",
        admissionPath : "내 입과 경로는?",
        admissionYear : "내 학번은?",
        detailedMajor : "내 세부 전공은?",
        track : "내 트랙은?"
    },

    department : ["공공인재학부","소프트웨어학부"],
    admissionPath : ["신입학","전과","편입학"],
    admissionYear : ["2022","2021","2020","2019","2018"],
    detailedMajor : ["전공심화","복수전공 (주전공)", "복수전공 (부전공)","연계전공 이름"],
    track : ["해당없음","행정학 트랙","정책학 트랙","엔터프라이즈 SW"],


};

const textList = ["department","admissionPath","admissionYear","detailedMajor","track"];

let ha = 1;



const handleListClick = ()=>{
    ha += 1;
    listTitle.innerText = optionList.title[textList[ha-1]];
    let number = 0;
    for(number =1; number < optionList[textList[ha-1]].length; number++){
        const mainChoice = document.querySelector(`.table-component__list__element:nth-child(${number})`);
        mainChoice.innerHTML = `<li>
        <span>${optionList[textList[ha-1]][number]}</span>
        <!--todo: icon chevron-right-->
    </li>`
    }
    progressNum.innerText = `${ha}/5`
}


listElement[0].addEventListener("click",handleListClick);



        