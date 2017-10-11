from app import app #normally is already be in memory as main.py calls it before views.py
from flask import render_template, request, redirect, url_for

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# @app.route("/login/", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         form = LoginForm(request.form)
#         if form.validate():
#             login_user(form.user, remember=form.remember_me.data) #sets correct session values
#             flash("Successfully logged in as %s." % form.user.email, "success")
#             return redirect(request.args.get("next") or url_for("homepage"))
#     else:
#         form = LoginForm()
#     return render_template("login.html", form=form)
