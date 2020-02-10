from torchvision import models
import torch
# from summary import summary
# from torchsummary import summary
from PIL import Image
import torch.utils.model_zoo as model_zoo
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import pylab
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
import torchvision
import numpy as np


resnet = models.ResNet(models.resnet.BasicBlock, [3, 4, 6, 3], num_classes=20)
resnet_dict = resnet.state_dict()
pretrained_dict = torch.load("./resnet34.pth")
pretrained_dict = {k: v for k, v in pretrained_dict.items()
                   if k in resnet_dict and k != 'fc.weight' and k != 'fc.bias'}

resnet_dict.update(pretrained_dict)
resnet.load_state_dict(resnet_dict)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(resnet.parameters(), lr=0.001, momentum=0.9)

train_data = []


# input data pre process
# transform = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406],
#         std=[0.229, 0.224, 0.225]
#     )])
# file_path = './eButton_data/Camera/ID0117_Oct.19/1/0117_2018Oct19_010001_0.jpg'
# img = Image.open(file_path)
# img_t = transform(img)
# batch_t = torch.unsqueeze(img_t, 0)
# batch_t = batch_t.cuda(non_blocking=True)

for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    i = 0
    for data in train_data:
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data[0].to(device), data[1].to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = resnet(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        i += 1
        if i % 50 == 49:
            print(running_loss)
            running_loss = 0.0
print('Finished Training')

# transform = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406],
#         std=[0.229, 0.224, 0.225]
#     )])
# file_path = './eButton_data/Camera/ID0117_Oct.19/1/0117_2018Oct19_010001_0.jpg'
# img = Image.open(file_path)
# img_t = transform(img)
# batch_t = torch.unsqueeze(img_t, 0)
# # batch_t = batch_t.cuda(non_blocking=True)

# # get answer
# out = resnet(batch_t)
# print(out)
# _, indices = torch.sort(out, descending=True)
# print(_)
# print(indices)
