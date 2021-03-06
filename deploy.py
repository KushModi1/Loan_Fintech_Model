from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
# Load the Model
model = pickle.load(open('Loanmodel.sav','rb'))

@app.route('/')
def home():
    return render_template('Index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents = int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        Credit_History = float(request.form['Credit_History'])
        Property_Area = int(request.form['Property_Area'])
        ApplicantIncomeLog = float(request.form['ApplicantIncomeLog'])
        LoanAmountLog = float(request.form['LoanAmountLog'])
        Loan_Amount_Term_Log = float(request.form['Loan_Amount_Term_Log'])
        Total_Income_Log = float(request.form['Total_Income_Log'])
        result = model.predict([[Gender,Married,Dependents,Education,Self_Employed,Credit_History,Property_Area,ApplicantIncomeLog,LoanAmountLog,Loan_Amount_Term_Log,Total_Income_Log]])[0]
        
        # print(Prediction)
        if (result=="N"):
            result= "Rejected"
        else:
            result="Approved"
        return render_template('Prediction.html',**locals())
    else:
        return render_template('Prediction.html',**locals())



            



if __name__ == '__main__':
    app.run(debug=True)
