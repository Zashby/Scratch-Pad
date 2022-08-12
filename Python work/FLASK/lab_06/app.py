
from flask import Flask, request, render_template
import string


def rot_cipher_lite(plain_text, rot=13):
    alphabet = []
    for x, y in zip(string.ascii_lowercase, string.ascii_uppercase):
        alphabet.append(x)
        alphabet.append(y)
    punc_list = list(string.punctuation)
    num_list = list(string.digits)
    plain_list = list(plain_text)
    for l in range(len(plain_list)):
        if plain_list[l] in alphabet:
            plain_list[l] = alphabet[(alphabet.index(plain_list[l])+(rot*2))%len(alphabet)]
        if plain_list[l] in punc_list:
            plain_list[l] = punc_list[(punc_list.index(plain_list[l])+rot)%len(punc_list)]
        if plain_list[l] in num_list:
            plain_list[l] = num_list[(num_list.index(plain_list[l])+rot)%len(num_list)]

    return "".join(plain_list)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    message = request.form.get("message", "")
    rotation = request.form.get("rotation", 13)
    encoded = rot_cipher_lite(message, int(rotation))
    return render_template("index.html", encoded=encoded)



app.run(debug=True)