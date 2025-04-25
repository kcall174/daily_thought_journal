from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#temporary storage (will reset when app restats)
thoughts = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    thought = request.form['thought']
    thoughts.append(thought)
    return redirect(url_for('view_thoughts'))

@app.route('/thoughts')
def view_thoughts():
    return render_template('thoughts.html', thoughts=thoughts)

if __name__ == "__main__":
    app.run(debug=True)



