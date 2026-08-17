from flask import Flask, request, jsonify
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# load model
model = joblib.load("best_model.joblib")

# root route
@app.get("/")
def home():
    return "Welcome to SuperKart"


# /predict route
@app.post("/v1/predict")
def predict():
    # get data from request
    data = request.get_json()

    fields = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_MRP": data["Product_MRP"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"],
        "Product_Id_First_2_Chars": data["Product_Id_First_2_Chars"],
        "Store_Age": data["Store_Age"],
        "Product_Type_Category": data["Product_Type_Category"]
    }

    input_data = pd.DataFrame([fields])
    prediction = model.predict(input_data)

    return jsonify({"predicted_sales": prediction})


if __name__ == "__main__":
    app.run(debug=True)
