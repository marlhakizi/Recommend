from flask import Flask,request,render_template
from flask import jsonify
from getsimilar import display_similar
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')
#def hello():
#    """Return a friendly HTTP greeting."""
   # print("hello")
    #return ("Hello and  Welcome! <br> If you need to check which meal time it is, check the meal path. ")

    
#@app.route('/meal/<name>')
@app.route('/',methods=['POST'])
def my_form_post():
    #print("okay")
    #print(display_similar(info, num=5))
    info=request.form.get("productid")
    data = display_similar(info, num=5)
    # return jsonify({"lolz":data})
    return render_template('results.html', title='Results', data=data)



if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(debug=True)