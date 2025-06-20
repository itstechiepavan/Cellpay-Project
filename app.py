from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to CellPay - A simple money transfer service"

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        amount = request.form["amount"]
        return f"{amount} sent from {sender} to {receiver}!"
    return render_template("send.html")

@app.route("/receive", methods=["GET", "POST"])
def receive():
    if request.method == "POST":
        receiver = request.form["receiver"]
        amount = request.form["amount"]
        return f"{receiver} has received {amount}!"
    return render_template("receive.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
