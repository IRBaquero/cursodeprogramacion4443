document.getElementById("encuesta").addEventListener("submit", function(event) {
    event.preventDefault();
    var respuesta = "";
    var respuesta = "";
    var presupuesto = document.querySelector('input[name="presupuesto"]:checked').value;
    var modelo = document.querySelector('input[name="modelo"]:checked').value;
    var uso = document.querySelector('input[name="uso"]:checked').value;
    var tecnologia = document.querySelector('input[name="tecnologia"]:checked').value;
    var desgaste = document.querySelector('input[name="desgaste"]:checked').value;
    var ahorro = document.querySelector('input[name="ahorro"]:checked').value;


    if (presupuesto === "bajo" && desgaste === "no" && ahorro !== "no_importante") {
        respuesta = "Te recomendamos comprar una moto usada.";
    } else {
        respuesta = "Te recomendamos comprar una moto nueva.";
    }
    document.getElementById("respuesta").textContent = respuesta;
});