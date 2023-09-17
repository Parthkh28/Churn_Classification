import pickle
import pandas as pd
from flask import Flask, request, render_template, jsonify
import tensorflow as tf

# Load your models and scalers here
lr_model = pickle.load(open('models/best_lr_model.pkl', 'rb'))
rf_model = pickle.load(open('models/best_rf_model.pkl', 'rb'))
xgb_model = pickle.load(open('models/best_xgb_model.pkl', 'rb'))
nn_model = tf.keras.models.load_model('models/best_nn_model.h5')

# Load Label Encoders and Scalers
with open('encoders_and_scalers/label_encoder_gender.pkl', 'rb') as f:
    le_gender = pickle.load(f)
with open('encoders_and_scalers/label_encoder_location.pkl', 'rb') as f:
    le_location = pickle.load(f)
with open('encoders_and_scalers/age_group_columns.pkl', 'rb') as f:
    age_group_columns = pickle.load(f)
with open('encoders_and_scalers/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('encoders_and_scalers/scaler_nn.pkl', 'rb') as f:
    scaler_nn = pickle.load(f)

# Function to preprocess and perform prediction
def preprocess_and_predict(data, model_choice):
    # Convert data into DataFrame
    df = pd.DataFrame([data])

    # Convert columns to numeric
    df['Total_Usage_GB'] = pd.to_numeric(df['Total_Usage_GB'])
    df['Subscription_Length_Months'] = pd.to_numeric(df['Subscription_Length_Months'])

    # Label Encoding
    df['Gender'] = le_gender.transform(df['Gender'])
    df['Location'] = le_location.transform(df['Location'])

    # Create feature: Usage_per_Month
    df['Usage_per_Month'] = df['Total_Usage_GB'] / df['Subscription_Length_Months']
    bins = [18, 30, 50, 70, 100]
    labels = ['18-30', '30-50', '50-70', '70+']
    df['Age'] = pd.to_numeric(df['Age'])
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    df = pd.get_dummies(df, columns=['Age_Group'])
    
    # Prepare the final feature vector X (Dropping unnecessary columns)
    X = df.drop(['CustomerID', 'Name', 'Age'], axis=1)
    X = X.astype('float32')
    
    # Apply the correct scaler based on the model choice
    if model_choice in ['lr', 'rf', 'xgb']:
        features = ['Monthly_Bill', 'Total_Usage_GB', 'Subscription_Length_Months', 'Usage_per_Month']
        X[features] = scaler.transform(X[features])
    elif model_choice == 'nn':
        X = scaler_nn.transform(X)  # Assuming that scaler_nn was fit on similar features as X
        # In preprocess_and_predict, print df and X to debug
    print("DataFrame after preprocessing: ", df)
    print("Feature Vector X: ", X)

    
    # Perform prediction based on user's model choice
    if model_choice == 'lr':
        prediction = lr_model.predict(X)[0]
    elif model_choice == 'rf':
        prediction = rf_model.predict(X)[0]
    elif model_choice == 'xgb':
        prediction = xgb_model.predict(X)[0]
    elif model_choice == 'nn':
        prediction = round(nn_model.predict(X)[0][0])

    return prediction


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/predict", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        data = request.form.to_dict()
        model_choice = data.pop("Model_Choice")
        # Inside index() function in Flask, print received data and prediction
        print("Received Data: ", data)
        print("Prediction: ", prediction)

        prediction = preprocess_and_predict(data, model_choice)
    return render_template("index.html", prediction=prediction)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.json
    model_choice = data.pop("Model_Choice")
    prediction = preprocess_and_predict(data, model_choice)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
