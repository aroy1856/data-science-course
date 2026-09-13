from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    city = request.form['city']
    phone = request.form['phone']
    return render_template('success.html', name=name, city=city, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)