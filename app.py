from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dice1 = 1
    dice2 = 1
    total = 0
    two_mode = False
    
    if request.method == 'POST':
        two_mode = request.form.get('two_mode') == 'on'
        dice1 = random.randint(1, 6)
        
        if two_mode:
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
        else:
            total = dice1
    
    return render_template('index.html', 
                         dice1=dice1, 
                         dice2=dice2, 
                         total=total, 
                         two_mode=two_mode,
                         dice1_path=f'images/dice_{dice1}.png',
                         dice2_path=f'images/dice_{dice2}.png')

if __name__ == '__main__':
    app.run(debug=True)
