import flask

from flask import request

app = flask.Flask(__name__)

app.config["DEBUG"] = True


from fask_cors import CORS

CORS(app)


# main index page route

@app.route('/')

def home():

    return '<h1>API is working.. </h1>'




@app.route('/predict',methods=['GET'])

def predict():
 
   from sklearn.externals import joblib
 
   model = joblib.load('marriage_age_predict_model.ml')
 
   predicted_age_of_marriage = model.predict([[(request.args['gender']),
            
                            (request.args['religion']),

                            (request.args['caste']),

                            (request.args['mother_tongue']),

                            (request.args['country']),
 
                           (request.args['height_cms']),

                           ]])

    return str(round(predicted_age_of_marriage[0],2))
#return str(predicted_age_of_marriage)

 
if __name__ == "__main__":
 
   app.run(debug=True)
