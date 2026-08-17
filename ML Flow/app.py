import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np

#tracking Uri
import dagshub
dagshub.init(repo_owner='gppatil2306', repo_name='ML-Flow', mlflow=True)
remote_setup = "https://dagshub.com/gppatil2306/ML-Flow.mlflow"
mlflow.set_tracking_uri(remote_setup)

# Enable autologging
mlflow.sklearn.autolog()

# Load Wine dataset
data = load_wine()
X = data.data
# For regression demo, we'll use the 'alcohol' feature as a continuous target
y = data.target.astype(float) + np.random.normal(0, 0.5, size=len(data.target))
# (Above: added noise to make it more realistic for regression)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True, False]
}

# Train model - MLflow automatically logs everything!
with mlflow.start_run():
    # Initialize Random Forest Regressor
    rf = RandomForestRegressor(random_state=42)

    # Define hyperparameter grid
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'max_features': ['sqrt', 'log2'],
        'bootstrap': [True, False]
    }

    # Setup GridSearchCV
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        verbose=2,
        scoring='r2'  # Optimize for R² score
    )

    # Fit the model
    grid_search.fit(X_train, y_train)

    # Best parameters and CV score
    print("\nBest Parameters:", grid_search.best_params_)
    print("Best Cross-Validation R²:", grid_search.best_score_)

    # Evaluate on test set
    best_rf = grid_search.best_estimator_
    y_pred = best_rf.predict(X_test)

    # Metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Test R² Score: {r2:.4f}")
    print(f"Test Mean Absolute Error (MAE): {mae:.4f}")



