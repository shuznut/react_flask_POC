from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICTIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class usecase(db.Model):
    usecase_id = db.Column(db.Integer, primary_key = True)
    usecase_name = db.Column(db.String(20))
    usecase_shortcode = db.Column(db.String(6))
    usecase_startDate = db.Column(db.DateTime)
    usecase_updateDate = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, usecase_name, usecase_shortcode, usecase_startDate):
        self.usecase_name = usecase_name
        self.usecase_shortcode = usecase_shortcode
        self.usecase_startDate = usecase_startDate

class UsecaseSchema(ma.Schema):
    class Meta: 
        fields = ('usecase_id','usecase_name', 'usecase_shortcode', 'usecase_startDate','usecase_updateDate')

usecase_schema = UsecaseSchema()
usecases_schema = UsecaseSchema(many=True)

@app.route('/get', methods = ['GET'])
def get_usecases():
    # return jsonify({"Hello":"World"})
    all_usecases = usecase.query.all()
    results = usecases_schema.dump(all_usecases)
    return jsonify(results)

@app.route('/get/<usecase_id>', methods = ['GET'])
def post_details(usecase_id):
     usecase_given_id = usecase.query.get(usecase_id)
     return usecase_schema.jsonify(usecase_given_id)

@app.route('/add', methods = ['POST'])
def add_usecase():
            usecase_name = request.json['usecase_name']
            usecase_shortcode = request.json['usecase_shortcode']
            usecase_startDate = request.json['usecase_startDate']

            usecases = usecase(usecase_name,usecase_shortcode,usecase_startDate)
            db.session.add(usecases)
            db.session.commit()
            return usecase_schema.jsonify(usecases)

@app.route('/update/<usecase_id>', methods = ['PUT'])
def update_usecase(usecase_id):
     usecase_upt = usecase.query.get(usecase_id)

     usecase_name_upt = request.json['usecase_name']
     usecase_shortcode_upt = request.json['usecase_shortcode']
     usecase_startDate_upt = request.json['usecase_startDate']

     usecase_upt.usecase_name = usecase_name_upt
     usecase_upt.usecase_shortcode = usecase_shortcode_upt
     usecase_upt.usecase_startDate = usecase_startDate_upt

     db.session.commit()
     return usecase_schema.jsonify(usecase_upt)

@app.route('/delete/<usecase_id>', methods = ['DELETE']) 
def delete_usecase(usecase_id):
     usecase_del = usecase.query.get(usecase_id)
     db.session.delete(usecase_del)
     db.session.commit()

     return usecase_schema.jsonify(usecase_del)

     

if __name__ == "__main__":
    app.run(debug=True)