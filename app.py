from flask import Flask, render_template, request
from calculator import calculate

print("🚀 Calculator App Starting...")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator_view():
    result = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        result = calculate(num1, num2, operation)
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
   # app.run(debug=False, use_reloader=False, port=5001)

 port = int(os.environ.get("PORT", 5001))
 app.run(host='0.0.0.0', port=port)

