from app import app, db
import views # it will reference to the app which is already in memory
import models
import admin
from documents.blueprint import documents

app.register_blueprint(documents, url_prefix='/documents')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
