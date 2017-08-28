from flask import Flask,flash,g, request,session
import config

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)# change accordingly

### TO verify If this code works !
@app.before_request
def _last_page_visited():
    if "current_page" in session:
        session["last_page"] = session["current_page"]
    session["current_page"] = request.path
