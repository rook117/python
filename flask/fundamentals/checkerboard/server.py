from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def checker():
    return render_template('index.html', num = 8)

@app.route('/<int:num>')
def lvl_one(num):
    return render_template('index.html', num = num)

@app.route('/<int:x>/<int:y>')
def lvl_two(x, y):
    return render_template('index.html', num = x * y)






if __name__=="__main__":
    app.run(debug=True)