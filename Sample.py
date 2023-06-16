from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine
# from pymongo import MongoClient

app = Flask(__name__)




db = MongoEngine()



app.config['MONGODB_DB'] = 'COB'
app.config['MONGODB_HOST'] = '20.232.134.13'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'MongoAdmin'
app.config['MONGODB_PASSWORD'] = 'Mongo2022'
# print(db)
db.init_app(app)


class Patient(db.Document):
    Name = db.StringField()
    # Id = db.StringField()
    Family_Name = db.StringField()
    Benificiary_Id = db.StringField()
    Dob = db.StringField()
    Gender = db.StringField()
    Relationship = db.StringField()



    def to_json(self):
        #convert this document to JSON
        return {
            "Name": self.Name,
            # "Id": self.Id,
            "Family_Name": self.Family_Name,
            "Beneficiary_Id": self.Benificiary_Id,
            "Dob": self.Dob,
            "Gender": self.Gender,
            "Relationship": self.Relationship

        }
'''
POST /api/db_populate -> Populates the DB and returns 201 success code (empty response body)

GET /api/Patient -> Return the detail of all Insurence (with 200 success code)

POST /api/Patient -> Creates a new Insurance record and return 201 success code (empty response body).

GET /api/patient/{family_Name} /{4 more information} /SSN key -> Return detail of Family_Name (with 200 success code if document found, 404 if document not found)
'''

@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    data1 = Patient(Name="Barack Obama",  Family_Name ="Obama",Benificiary_Id="1010101",Dob="1961-08-04",Gender="Male")
    data2 = Patient(Name="Michelle Obama",  Family_Name ="Obama",Benificiary_Id="1010101",Dob="1964-01-17",Gender="Female")
    data3 = Patient(Name="Malia Obama",  Family_Name ="Obama",Benificiary_Id="1010101",Dob="1998-07-04",Gender="Female")
    data4 = Patient(Name="Sasha Obama",  Family_Name ="Obama",Benificiary_Id="1010101",Dob="2001-06-10",Gender="Female")
    data1.save()
    data2.save()
    data3.save()
    data4.save()
    return make_response("Done", 201)


@app.route('/api/Patient', methods=['GET'])
def api_patient():
    if request.method == "GET":
        print(request.method)
        Member = []
        for patient in Patient.objects:
            Member.append(patient)
        return make_response(jsonify(Member),200)
    

@app.route('/api/Patient/<Family_Name>', methods=['GET'])
def db_each_patient(Family_Name):
    if request.method == "GET":
        Member_obj= Patient.objects(Family_Name = Family_Name)
        if Member_obj:
            return make_response(Member_obj.to_json(),200)

# @app.route('/api/db_populate', methods=['GET'])
# def db_each_patient():
#     pass


if __name__ == '__main__':
    app.run()