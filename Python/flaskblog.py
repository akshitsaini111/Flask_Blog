from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect


app= Flask(__name__)

# app.config["SECRET_kEY"]="Akshit_saini"
app.secret_key="Akshit_saini"
csrf = CSRFProtect(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]




@app.route("/",methods=["GET"])
def home():
    return render_template("home.html", posts=posts, title="AKshit")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["POST","GET"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For!','success')
        return redirect(url_for("home"))
    return render_template("register.html",title="Register", form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template("login.html",title="Login", form=form)


if __name__ =="__main__":
    app.run(debug=True)
    csrf.init_app(app)
    