from flask import Flask, request, render_template
import re

app = Flask(__name__, static_url_path='/static', static_folder='static')

def find_match(test, regex):
    matches = re.finditer(regex, test)
    match_list = []
    for match in matches:
        match_list.append(match.group())
    return match_list

def check_mail(email_input):
    # Regular expression for email validation
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:in|com)'
    return re.match(email_pattern, email_input) is not None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        test = request.form["test"]
        regex = request.form["regex"]
        matches = find_match(test, regex)
        return render_template("home.html", matches=matches)
    return render_template("home.html")

@app.route("/validate-email", methods=["GET", "POST"])
def validate_mail():
    if request.method == "POST":
        email_input = request.form["email_input"]
        valid = check_mail(email_input)
        return render_template("mail.html", email_input=email_input, valid=valid)
    return render_template("mail.html")

if __name__ == "__main__":
   app.run(debug = True, 
   host = "0.0.0.0", port  = 5000)