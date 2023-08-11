import torchvision.models as models
import torchvision.transforms as transforms
import torch
from PIL import Image
import json

model_transfer = models.resnet50(pretrained=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
weights_path = "./dog_transfer.pt"

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
for param in model_transfer.parameters():
    param.requires_grad = False
model_transfer.fc = torch.nn.Linear(2048, 133, bias=True)
fc_parameters = model_transfer.fc.parameters()
for param in fc_parameters:
    param.requires_grad = True
with open('./dogs.json', 'r') as f: 
    dogs_names = json.load(f)
model_transfer.load_state_dict(torch.load(weights_path, map_location=device))
model_transfer.fc = torch.nn.Identity()

def load_input_image(image):    
    prediction_transform = transforms.Compose([transforms.Resize(size=(224, 224)),
                                     transforms.ToTensor(), 
                                     normalize])

    # discard the transparent, alpha channel (that's the :3) and add the batch dimension
    image = prediction_transform(image).unsqueeze(0)
    return image

def predict_breed_transfer(img):
    # load the image and return the predicted breed
    img = load_input_image(img)
    model_transfer1 = model_transfer.cpu()
    model_transfer1.eval()
    return model_transfer1(img)
    
def compare1(output1, output2): # i think should be under 20
    euclidean_distance = torch.norm(output1 - output2, p=2)
    print("Euclidean Distance:", euclidean_distance.item())

