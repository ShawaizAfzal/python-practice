from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():     
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    result = num1 + num2

    return jsonify({"sum": result})



if __name__ == "__main__":
    app.run(debug=True)
