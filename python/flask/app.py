from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return render_template('home.html',name=name)
    return '''
    <form method="post">
    Name: <input type="text" name="name">
    <input type="submit">
    '''
# @app.route('/<name>')
# def home(name):
#     # return f"Hello World, {name}"
#     return render_template('home.html',name=name)

if __name__=='__main__':
    app.run(debug=True)

