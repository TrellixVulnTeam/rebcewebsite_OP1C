from flask import Flask,request
import config

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)# change accordingly
