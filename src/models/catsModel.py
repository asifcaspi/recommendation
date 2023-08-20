from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch

extractor = AutoFeatureExtractor.from_pretrained("harish03/catbreed")
model = AutoModelForImageClassification.from_pretrained("harish03/catbreed")
model = model.base_model

def predict(image):
    inputs = extractor(images=image, return_tensors="pt")

    # Make predictions using the modified model
    with torch.no_grad():
        features = model(**inputs)  # This will give you the output features of the modified model

    # You can now use these features for whatever downstream tasks you have in mind
    return features.last_hidden_state

def compare_cats(img1, img2):
    features1, features2 = predict(img1), predict(img2)
    mse = torch.mean(torch.square(features1 - features2))
    r_squared = 1 - mse / 0.5
    percentage_similarity = r_squared * 100
    return percentage_similarity