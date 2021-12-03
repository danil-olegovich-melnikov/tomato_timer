let input = document.querySelector(".to-do__write");


input.onkeypress = function (event) {
    if (event.keyCode === 13 && input.value) {
        let li = document.createElement("li");
        li.innerHTML = input.value;
        document.querySelector("ul").appendChild(li);
        input.value = "";
    }

};

let todos = document.querySelector("ul");
todos.onclick = function (event) {
    let target = event.target;
    if (target.tagName === 'LI') {
        target.classList.toggle('finish');
    }
}

document.querySelector(".add").onclick = function (event) {
    if (input.value) {
        let li = document.createElement("li");
        li.innerHTML = input.value;
        todos.appendChild(li);
        input.value = "";
    }
}


document.querySelector(".delete").onclick = function (event){
    todos.innerHTML = ""
}