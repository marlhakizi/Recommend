from flask import Flask,request,render_template
from flask import jsonify
from getsimilar import display_similar
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')

    
#@app.route('/meal/<name>')
@app.route('/',methods=['POST'])
def my_form_post():
    info=request.form.get("productid")
    product,data = display_similar(info, num=5)
    return render_template('results.html', title='Results', data=data,dat=product)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)