import joblib, os, datetime
class ETAPredictor:
    def __init__(self, model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.model = joblib.load(model_path)

        print("=" * 60)
        print("Model loaded successfully")
        print("Number of features expected:", len(self.model.feature_name_))
        print(self.model.feature_name_)
        print("=" * 60)