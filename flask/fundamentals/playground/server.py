from ast import Num
from flask import Flask, render_template
app = Flask(__name__)                     
    

@app.route('/play')
def lvl_one():
    return render_template("index.html", num=3, color="blue")  

@app.route('/play/<int:num>/color0')
def box():
    return
    
if __name__=="__main__":
    app.run(debug=True)                   

