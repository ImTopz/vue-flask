from flask import Flask ,redirect, url_for

app = Flask(__name__)

#the formula for int/float
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/data')
def data_detect():
    return 'data test'


#url_jump
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('data_detect'))
   else:
      return redirect(url_for('show_blog',postID=3))

if __name__ == '__main__':
    app.run()
