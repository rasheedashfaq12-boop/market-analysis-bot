async function getSignal() {
    const symbol = document.getElementById("symbol").value;
    const interval = document.getElementById("interval").value;

    try {
        const response = await fetch(`http://127.0.0.1:8000/signal?symbol=${symbol}&interval=${interval}`);
        const data = await response.json();

        document.getElementById("signal").innerText = `Signal: ${data.signal}`;
        document.getElementById("confidence").innerText = `Confidence: ${data.confidence}%`;
    } catch (error) {
        document.getElementById("signal").innerText = "Signal: Error";
        document.getElementById("confidence").innerText = "Confidence: -";
        console.error("Error fetching signal:", error);
    }
}
