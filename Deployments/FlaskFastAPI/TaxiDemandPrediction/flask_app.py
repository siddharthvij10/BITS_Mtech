from flask import Flask, request
import score


# start app
app = Flask(__name__)


# render default webpage
@app.route('/')
def home():
    return 'Hello world!. Ths is Flask APP default page'


# when the post method detect, then redirect to success function
@app.route('/predict', methods=["POST"])
def get_data():
    data = request.get_json(force=True)
    return "demand percent is {}".format(score.run(data))


#  flask -A flask_app --debug run
