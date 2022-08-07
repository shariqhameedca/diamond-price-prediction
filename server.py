# Import libraries
import numpy as np
from flask import Flask, request, render_template
import pickle
from cat_features import colors, clarity, cut

app = Flask(__name__)
# Load the model

with open('./saved_models/lin_model.pkl', 'rb') as savefile:
    lin_model = pickle.load(savefile)
    
with open('./saved_models/pol_model.pkl', 'rb') as savefile:
    pol_model = pickle.load(savefile)
    
with open('./saved_models/rf_model.pkl', 'rb') as savefile:
    rf_model = pickle.load(savefile)

models = {
    'Linear Regression': lin_model,
    'Polynomial Regression': pol_model,
    'Random Forest': rf_model
    }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == 'POST':
        data = request.form
        
    
    columns = ['x','y','z', 'carat']
    all_columns = ['carat', 'depth', 'x', 'y', 'z', 'cut', 'clarity', 'color']
    data_point = []
    for column in all_columns:
        if column in columns:
            data_point.append(np.log(float(data[column])))
        else:
            if column == 'cut':
                data_point.append(cut[data[column]])
            elif column == 'clarity':
                data_point.append(clarity[data[column]])
            elif column == 'color':
                data_point.append(colors[data[column]])
            else:
                data_point.append(data[column])
        
    
    data_point = np.array(data_point)
    data_point = data_point.reshape(1,-1)
    # Make prediction using model loaded from disk as per the data.
    prediction = models[data['model']].predict(data_point)
    # Take the first value of prediction
    result = np.exp(prediction[0])

    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(port=5000, debug=True)