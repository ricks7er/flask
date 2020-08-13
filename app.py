from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',current_title='Custom Title')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)