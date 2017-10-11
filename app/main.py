from app import app
import views # it will reference to the app which is already in memory
from documents.blueprint import documents
#from documents.blueprint import english

app.register_blueprint(documents, url_prefix='/documents')
#app.register_blueprint(english, url_prefix='/english')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
