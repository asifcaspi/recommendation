from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch
from constants.cats import max_mse

extractor = AutoFeatureExtractor.from_pretrained("harish03/catbreed")
model = AutoModelForImageClassification.from_pretrained("harish03/catbreed")
model = model.base_model

def predict(image):
    inputs = extractor(images=image, return_tensors="pt")

    # Make predictions using the modified model
    with torch.no_grad():
        features = model(**inputs)  # the output features of the modified model

    return features.last_hidden_state

def compare_cats(img1, img2):
    features1, features2 = predict(img1), predict(img2)
    mse = torch.mean(torch.square(features1 - features2))
    r_squared = 1 - mse / max_mse
    percentage_similarity = r_squared * 100
    return percentage_similarity