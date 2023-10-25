async function generateData() {
    const input = document.getElementById("input").value;
    const type = document.getElementById("type").value;
    const baseURL = "http://localhost:8080"

    const response = await fetch(`${baseURL}/get-data`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ input, type }),
    });

    const data = await response.json();
    document.getElementById("output").innerText = data.response;
}