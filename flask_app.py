from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    color_ = {}
    color_['bg_color'] = "#F5F5F5"
    color_['f_color'] = "#383838"
    return render_template('FinalDModel01.html', color = color_)
    # return render_template('FinalDModel01.html', bg_color = "#F5F5F5", f_color = "#383838")

@app.route('/', methods=['POST'])
def home_post():
    color_ = {}
    color_['bg_color'] = request.form['l_bg_clr']
    color_['f_color'] = request.form['l_f_clr']
    
    return render_template('FinalDModel01.html', color=color_)

if __name__ == '__main__':
   app.run(debug = True)