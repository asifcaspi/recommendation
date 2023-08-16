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

def compare(features1, features2): # mse i think should be lower then 0.05
    mse = torch.mean(torch.square(features1 - features2))
    print("Mean Squared Error between features:", mse.item())