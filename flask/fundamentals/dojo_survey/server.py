from flask import Flask, redirect, render_template, redirect, request, session 

app = Flask (__name__)
app.secret_key = "turtledove"



@app.route('/')
def survey():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    print (request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/')

@app.route('/show')
def show():
    return render_template('=show.html')



if __name__=="__main__":
    app.run(debug=True)