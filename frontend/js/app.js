const list = document.querySelector(".list");
const submit = document.querySelector(".btn");

window.addEventListener("DOMContentLoaded", displayTasks);

async function displayTasks() {
  //get("http://127.0.0.1:8000/tasks/").then((res) => console.log(res));
  const res = await fetch("http://127.0.0.1:8000/tasks/");
  const data = await res.json();
  console.log(data);
  let x = document.createElement("div");
  x.className = "card";
  let output = "";
  data.forEach((d) => {
    output += `
      <div class="list-item">
      <p>${d.title}</p>
      <p>${d.note}
      </div>
      `;
  });
  list.innerHTML = output;
}

btn = document.querySelector(".btn");

btn.addEventListener("click", submitTask);

async function submitTask(e) {
  title = document.querySelector("#title").value;
  note = document.querySelector("#note").value;
  const data = {
    title,
    note,
  };
  if (title === "" || note === "") {
    alert("Please Fill The Form!!");
  } else {
    const response = await fetch("http://127.0.0.1:8000/tasks/", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const resData = await response.json();
    console.log(resData);
  }
  e.preventDefault();
}
