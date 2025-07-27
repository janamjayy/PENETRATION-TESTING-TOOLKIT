from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded valid credentials for brute-force testing
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

HTML_FORM = """
<!doctype html>
<title>Login Page</title>
<h2>Login</h2>
<form method="post">
  Username: <input type="text" name="username" /><br><br>
  Password: <input type="password" name="password" /><br><br>
  <input type="submit" value="Login" />
</form>
{% if message %}
<p style="color: red;">{{ message }}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return "Welcome, admin!"
        else:
            message = "Login failed"

    return render_template_string(HTML_FORM, message=message)

if __name__ == '__main__':
    app.run(debug=True)
