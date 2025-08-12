function loadTemperatureChart(data) {
    const ctx = document.getElementById('tempChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            datasets: [{
                label: 'Temperature (°C)',
                data: data,
                borderColor: '#ff6600',
                backgroundColor: 'rgba(255, 102, 0, 0.2)',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
}
