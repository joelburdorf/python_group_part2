from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        return "I posted", 201
    else:
        return "Not a post"

if __name__ == "__main__":
    app.run()

