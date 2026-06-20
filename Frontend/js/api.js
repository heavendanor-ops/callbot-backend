const API_URL = "http://127.0.0.1:8000";

export async function hacerLlamada(data) {
    try {
        const response = await fetch(`${API_URL}/call`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        return result;

    } catch (error) {
        console.error("Error:", error);
    }
}