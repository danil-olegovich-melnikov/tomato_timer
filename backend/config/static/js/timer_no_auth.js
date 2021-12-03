const time = document.querySelector(".timer__time")
const start_timer = document.querySelector("#start_timer")
const reset_timer = document.querySelector("#reset_timer")
const end_timer = document.querySelector("#end_timer")

const default_time = 5
let timer_is_active = false;


let initial_time = localStorage.getItem("initial_time");
if (!initial_time) {
    initial_time = default_time
}

let current_time = initial_time;


start_timer.onclick = function () {
    timer_is_active = true
}

reset_timer.onclick = function () {
    timer_is_active = false;
    current_time = default_time;
    set()
}

end_timer.onclick = function () {
    timer_is_active = false
}


function seconds_to_time(s) {
    return (s - (s %= 60)) / 60 + (9 < s ? ':' : ':0') + s
}


function set() {
    time.innerHTML = seconds_to_time(current_time);
    localStorage.setItem("initial_time", current_time)
}


function is_finished() {
    if (current_time === 0) {
        current_time = default_time;
        timer_is_active = false;
        set()
    }
}

function update() {
    if (timer_is_active) {
        current_time -= 1;
        set()
        is_finished()
    }
}

set()
setInterval(update, 1000);
