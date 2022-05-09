from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "views" not in session:
        session['views'] = 0
    else:
        session['views'] = session['views'] + 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)