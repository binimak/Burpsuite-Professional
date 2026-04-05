from flask import Flask, request

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

    return "Registered Successfully!"

if __name__ == "__main__":
    app.run(port=5000)
