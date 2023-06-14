


from flask import Flask, request
app = Flask(__name__)
import random
import string


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/signup')
def signup():
    return "You have signed up for this website"


@app.route('/grade/<int:num>')
def grade(num):
    if num >=90:
        return 'A'

@app.route('/username')
def username():
    name = request.args.get("name", "none")

    return f"The username {name} does not exist"

@app.route('/password/<int:num>')
def password(num):
    final_pass = []
    upper = request.args.get("upper", True)
    digits = request.args.get('digits', True)
    special = request.args.get("special", True)
    pass_character = list(string.ascii_lowercase +(string.ascii_uppercase if upper == True else "")+ (string.digits if digits ==True else "")+ (string.punctuation if special == True else ""))

#Address/?upper=(BOOL)&digits=(BOOL)&special=(BOOL)

    for char in range(num):
        final_pass.append(random.choice(pass_character))
    print(pass_character)        
    return "".join(final_pass)


app.run(debug=True)

