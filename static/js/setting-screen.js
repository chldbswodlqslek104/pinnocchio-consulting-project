//html 요소 선택자
const listElement = document.querySelectorAll(
  ".table-component__list__element"
);
const listTitle = document.querySelector(".table-component__header h4");
const progressNum = document.querySelector("main>span");

//변수
let currentProgress = 1;
let userChoice = [];

//필요한 데이터

//필요한 데이터 -- 제목 리스트
const title = {
  department: "내 소속 학과는?",
  admissionPath: "내 입과 경로는?",
  admissionYear: "내 학번은?",
  detailedMajor: "내 세부 전공은?",
  track: "내 트랙은?",
};

//필요한 데이터 -- 선택지
const options = {
  department: ["공공인재학부", "소프트웨어학부"],
  admissionPath: ["신입학", "전과", "편입학"],
  admissionYear: ["2022", "2021", "2020", "2019", "2018"],
  detailedMajor: [
    "전공심화",
    "복수전공 (주전공)",
    "복수전공 (부전공)",
    "연계전공 이름",
  ],
  track: ["해당없음", "행정학 트랙", "정책학 트랙", "엔터프라이즈 SW"],
};

//필요한 데이터 -- 더미데이터
const selectedDepartment = {
  공공인재학부: {
    detailedMajor: ["공공인재1", "공공인재2"],
    track: ["공공인재3", "공공인재4"],
  },
  소프트웨어학부: {
    detailedMajor: ["소프트웨어1", "소프트웨어2"],
    track: ["소프트웨어3", "소프트웨어4"],
  },
};

//필요한 데이터 -- key 배열
const keyLists = [
  "department",
  "admissionPath",
  "admissionYear",
  "detailedMajor",
  "track",
];

//inner 함수
const moveToSchedulePage = () => {
  location.href = "schedulling-page.html";
};

const optionWriter = (optionText) => {
  const optionElment = document.createElement("li");
  optionElment.classList.add("table-component__list__element");
  optionElment.innerHTML = `<a>
      <span>${optionText}</span>
      <i class="fa-solid fa-chevron-right fa-lg"></i>
  </a>`;

  document.querySelector(".table-component__list").appendChild(optionElment);
};

const optionCleaner = () => {
  let optionTable = document.querySelector(".table-component__list");
  optionTable.innerHTML = "";
};

const optionsReSetter = (selected) => {
  options.detailedMajor = selectedDepartment[selected].detailedMajor;
  options.track = selectedDepartment[selected].track;
};

//핸들러
const handleOptionButtonClick = (event) => {
  currentProgress += 1;
  if (currentProgress <= keyLists.length) {
    CURRENTINDEX = keyLists[currentProgress - 1];

    if (CURRENTINDEX === "admissionPath") {
      optionsReSetter(event.currentTarget.innerText);
    }

    console.log(event);
    userChoice.push(event.currentTarget.innerText);
    console.log(userChoice);
    console.log(CURRENTINDEX);

    //핸들러__제목 띄우기
    listTitle.innerText = title[CURRENTINDEX];

    //핸들러__선택지 띄우기
    optionCleaner();
    for (
      optionNumber = 0;
      optionNumber < options[CURRENTINDEX].length;
      optionNumber++
    ) {
      optionWriter(options[CURRENTINDEX][optionNumber]);
    }

    optionElement = document.querySelectorAll(
      ".table-component__list__element"
    );
    length = optionElement.length;
    console.log(optionElement);

    //핸들러__이벤트 핸들러 재추가
    for (let i = 0; i < length; i++) {
      optionElement[i].addEventListener("click", handleOptionButtonClick);
    }

    //핸들러__하단 현재 페이지 설정
    progressNum.innerText = `${currentProgress}/5`;
  } else {
    //api 요청
    const cast = {
      department: userChoice[0],
      major: userChoice[1],
      track: userChoice[2],
      entry_year: userChoice[3],
    };
    console.log(cast);
    localStorage.setItem("cast", JSON.stringify(cast));
    moveToSchedulePage();
  }
};

//이벤트 핸들러 추가
for (let i = 0; i < listElement.length; i++) {
  listElement[i].addEventListener("click", handleOptionButtonClick);
}
