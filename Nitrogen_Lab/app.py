from flask import Flask, render_template_string
import pandas as pd
import plotly.express as px

# Flask app
app = Flask(__name__)

# Example lab data (replace with actual data if available)
data = {
    "Days": [7, 14, 21],
    "Treatment_A": [5, 7, 8],
    "Treatment_B": [15, 25, 30],
    "Treatment_C": [10, 18, 22]
}
df = pd.DataFrame(data)

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Nitrogen Fertilization Experiment</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; text-align: center; }
        .container { display: flex; flex-direction: column; align-items: center; }
        table { margin: 20px auto; border-collapse: collapse; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
    </style>
</head>
<body>
    <h1>Nitrogen Fertilization Experiment</h1>
    <p>This application displays the results of nitrogen concentration changes across different soil treatments.</p>

    <h2>Interactive Visualization</h2>
    <div id="graph">{{ graph | safe }}</div>

    <h2>Data Table</h2>
    <table>
        <tr>
            <th>Days</th>
            <th>Treatment A</th>
            <th>Treatment B</th>
            <th>Treatment C</th>
        </tr>
        {% for _, row in table.iterrows() %}
        <tr>
            <td>{{ row['Days'] }}</td>
            <td>{{ row['Treatment_A'] }}</td>
            <td>{{ row['Treatment_B'] }}</td>
            <td>{{ row['Treatment_C'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def home():
    # Generate the interactive plot
    fig = px.line(
        df, 
        x="Days", 
        y=["Treatment_A", "Treatment_B", "Treatment_C"],
        title="Nitrogen Concentration Over Time",
        labels={"value": "Concentration (mg/kg)", "variable": "Treatment", "Days": "Days"}
    )
    graph = fig.to_html(full_html=False)

    # Render the HTML page with the graph and table
    return render_template_string(html_template, graph=graph, table=df)

if __name__ == "__main__":
    app.run(debug=True)
