from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/instructions')
def readme():
    return render_template('instructions.html')

@app.route('/project-evolution')
def project_evolution():
    return render_template('project-evolution.html')

@app.route('/attribution')
def attribution():
    return render_template('attribution.html')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)