from flask import Flask, request
from flask import render_template
import spider
import npl

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def helloWorld():
    text = request.args.get('text')
    gt=' '
    wt=' '
    dt=' '
    finaltext=' '
    if text != None:
        gt=spider.google('jp','en',text)
        dt=spider.deepl('jp','en',text)
        wt=spider.weblio('jp','en',text)
        finaltext=npl.compare(gt,dt,wt)

    
    return render_template('a.html',**locals())
    
if __name__ == '__main__':
    app.run()
