import { hacerLlamada } from "./api.js";

document.getElementById("btnLlamar").addEventListener("click", async () => {
    
    const data = {
        nombre: "Cliente prueba"
    };

    const respuesta = await hacerLlamada(data);

    console.log(respuesta);
});