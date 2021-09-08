document.addEventListener("DOMContentLoaded", function(event){
const xhttp = new XMLHttpRequest();
let led_matrix = []
for (let i = 0; i < 64; i++) {
    led_matrix.push(0);
}

function toggle_pixel(pixel_id) {
    let matrix_element = document.getElementById(pixel_id);
    
    if (matrix_element.classList.contains("active")) {
        matrix_element.classList.remove("active");
        led_matrix[pixel_id] = 0;
    } else {
        matrix_element.classList.add("active");
        led_matrix[pixel_id] = 1;
    }
}

function reset_matrix() {
    //reset the array
    for (let i = 0; i < 64; i++) {
        led_matrix[i] = 0;
    }
    //reset the matrix in the html
    matrix_elements.forEach(el => el.classList.remove("active"));
    //reset the matrix at the pi
    xhttp.open("POST", "/led-matrix", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({"befehl":"reset"}));
}
//Matrix-Element wird gedrückt -> dieses Element wird auf "active" gesetzt
const matrix_elements = document.querySelectorAll(".matrix-element");

matrix_elements.forEach(el => el.addEventListener("click", event => {
    let pixel_id = event.target.getAttribute("id");
    toggle_pixel(pixel_id);
}));
//Anzeigen-Knopf wird gedrückt -> Bild wird auf der Matrix angezeigt
const send_btn = document.querySelector("#send_matrix")

send_btn.addEventListener("click", event => {
    xhttp.open("POST", "/led-matrix", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({"matrix-board":led_matrix}));
});
//Reset-Knopf wird gedrückt -> Matrix wird resetet
const reset_btn = document.querySelector("#reset_matrix")

reset_btn.addEventListener("click", reset_matrix);
//Text-Input wird submitet -> diesen Text anzeigen
const input_form = document.querySelector("#matrix-texteingabe");

input_form.addEventListener("submit", event => {
    event.preventDefault();
    let text_input = document.querySelector("#usertext").value
    xhttp.open("POST", "/led-matrix", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({"usertext":text_input}));
});
//Beispielbild wird gedrückt -> dieses Bild anzeigen
const image_examples = document.querySelectorAll(".example_img");

image_examples.forEach(el => el.addEventListener("click", event => {
    let image_id = event.target.getAttribute("id");
    xhttp.open("POST", "/led-matrix", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({"matrix-example":image_id}));
}));

});