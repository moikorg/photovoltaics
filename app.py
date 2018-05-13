from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    return render_template("base.html")


class SonnenBattery(db.Model):
    consumption = db.Column(db.Integer)
    frequency = db.Column(db.Integer)
    # gridConsumption:
    #   negativ value = energy consumption from grid
    #   positiv value = energy feed-in to the grid
    gridConsumption = db.Column(db.Integer)
    #   isSystemInstalled = db.Boolean(blank=True, null=True)
    # pacTotal:
    #   negativ value = battery is charging
    #   postitv value = battery is discharging
    pacTotal = db.Column(db.Integer)
    production = db.Column(db.Integer)
    rsoc = db.Column(db.Integer)   # remain state of charge
    timestamp = db.Column(db.DateTime, primary_key=True )
    usoc = db.Column(db.Integer)
    uAC = db.Column(db.Integer)
    uBat = db.Column(db.Integer)


if __name__ == '__main__':
    app.run()
