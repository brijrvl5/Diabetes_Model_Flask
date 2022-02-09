from flask import Flask, render_template, request
from main import predict_value
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    print("All Set..!!")
    return render_template("index.html")

@app.route('/', methods=["POST"])
def predict():
    preg__count = request.form['preg_coun']
    glu_ = request.form['glu']
    blood_pre_ = request.form['blood_pre']
    skin_thickness = request.form['skin_thick']
    insulin = request.form['insu']
    b_m_i = request.form['bmi']
    dia_pede = request.form['dia_pedegree']
    age_ = request.form['age']

    res = predict_value(preg__count,glu_,blood_pre_,skin_thickness,insulin,b_m_i,dia_pede,age_)

    if (res == True):
        return render_template("False.html")
    else :
        return render_template("True.html")


if (__name__ == '__main__'):
    app.run(debug=True)