import argparse
import pandas as pd
import os
import joblib
import mlflow


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--input_data", type=str)
    parser.add_argument("--input_model", type=str)
    parser.add_argument("--output_folder", type=str)
    parser.add_argument("--output_asset", type=str)
    # parse args
    args = parser.parse_args()
    # return args
    return args


def main(args):
    test_data_orig = pd.read_csv(args.input_data)
    test_data = test_data_orig.drop("Churn", axis=1)
    test_data["Partner"] = test_data["Partner"].map({"Yes": True, "No": False})
    test_data["Dependents"] = test_data["Dependents"].map({"Yes": True, "No": False})
    test_data["PhoneService"] = test_data["PhoneService"].map({"Yes": True, "No": False})
    test_data["PaperlessBilling"] = test_data["PaperlessBilling"].map({"Yes": True, "No": False})
    print(test_data_orig.head(10))


    model_path = os.path.join(args.input_model, "model.pkl")
    model = joblib.load(model_path)

    result = model.predict(test_data)
    mlflow.log_metric("result length", len(result))
    test_data_orig["Churn_Prediction"] = result
    test_data_orig['Churn_Prediction'] = test_data_orig['Churn_Prediction'].map({True: 'Yes', False: 'No'})

    output_path = os.path.join(args.output_folder, "wa_telco_customer_churn_predictions.csv")
    test_data_orig.to_csv(output_path)
    


# run script
if __name__ == "__main__":
    # parse args
    args = parse_args()

    # run main function
    main(args)
