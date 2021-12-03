let ul = document.querySelector("ul");
let input = document.querySelector(".to-do__write");



input.onkeypress = function(event) {

    if (event.keyCode === 13) {

        let li = document.createElement("li");

        li.innerHTML = input.value;

        document.querySelector("ul").appendChild(li);

        input.value = "";

    }

};
document.querySelector("ul").onclick = function(event) {
    let target = event.target;
    if (target.tagName == 'LI') {
        target.classList.toggle('finish');
    }
}