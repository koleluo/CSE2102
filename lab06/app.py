from flask import Flask, request, jsonify

#Create a new Flask web application instance

app = Flask(__name__)

#Define a URL path; this oen responds to the homepage
@app.route('/')

def hello_world():
    return '<h1>Hello CSE2102 student, from Flask & Docker <h1>'


@app.route("/get_example")
def get_example():
    value = request.args.get("myvalue")
    return f"<h1>My value is: {value}</h1>"


@app.route("/post_example", methods  = ["POST"])
def post_example():
    postparm = request.json["mypostparm"]
    {
    "mypostparm": "uconn",
    "parm2": "huskies"
    }
    return jsonify({"received": postparm})

#Start flask development server when script is ran

if __name__ == "__main__":
    app.run(debug=True)
