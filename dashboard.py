from flask import Flask, jsonify, render_template_string
import json

app = Flask(_name_)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Voting Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
        }

        h1 {
            margin-top: 20px;
        }

        .card {
            background: white;
            color: black;
            width: 60%;
            margin: auto;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
        }
    </style>
</head>

<body>

<h1>??? Live Voting Dashboard</h1>

<div class="card">
    <canvas id="voteChart"></canvas>
</div>

<script>
let chart;

// Create chart first time
function createChart(labels, values) {
    const data = {
        labels: labels,
        datasets: [{
            label: 'Votes',
            data: values,
            backgroundColor: ['red','green','orange','purple','blue']
        }]
    };

    chart = new Chart(document.getElementById('voteChart'), {
        type: 'bar',
        data: data,
        options: {
            animation: false,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// Update chart
function updateChart(labels, values) {
    chart.data.labels = labels;
    chart.data.datasets[0].data = values;
    chart.update();
}

// Fetch data from server
async function fetchData() {
    const res = await fetch('/data');
    const data = await res.json();

    const labels = Object.keys(data);
    const values = Object.values(data);

    if (!chart) {
        createChart(labels, values);
    } else {
        updateChart(labels, values);
    }
}

// ?? Call every 1 second
setInterval(fetchData, 1000);

// Initial load
fetchData();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

# ?? API endpoint (very important)
@app.route("/data")
def data():
    with open("votes.json", "r") as f:
        counts = json.load(f)
    return jsonify(counts)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)