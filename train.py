import joblib
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def train():

    mlflow.set_experiment("Wine_Classification_Experiment")
    
    with mlflow.start_run() as run:
        wine = load_wine()
        X, y = wine.data, wine.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        n_estimators = 15
        max_depth = 2
        random_state = 42
        

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", random_state)
        

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
        model.fit(X_train, y_train)
        

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='macro')
        

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score_macro", f1)
        

        joblib.dump(model, "model.joblib")
        
        mlflow.sklearn.log_model(
            sk_model=model,
            name="random_forest_model",
            registered_model_name="Wine_RF_Model",
            input_example=X_train[:1]
        )
        
        print(f"Run ID: {run.info.run_id}")
        print(f"Accuracy: {acc:.4f}, F1: {f1:.4f}")
        print("Model saved to model.joblib and registered in MLflow.")

if __name__ == "__main__":
    train()
