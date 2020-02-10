import numpy as np
import torchvision
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.model_zoo as model_zoo
import pylab
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import shutil
from PIL import Image

from torchvision import models
import csv
import re

img_path = []
img_labels_tmp = []
label_content = {}
label_index = {}
index = 0
mv_index = 0
mv2_index = 0
with open('eButton_Data/result_final.csv') as csvfile:
    # reader = csvfile.readline(csvfile, delimiter=',')
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        tmp = re.search('ID0142(.*)', row[0])
        if tmp:
            file_path = 'eButton_Data/eButton_Data/Camera/'+str(tmp.group())
            img_path.append(file_path)
            label = []
            flag = False
            for i in range(1, 21):
                if row[i] not in label_index:
                    label_index[row[i]] = index
                    label_content[index] = row[i]
                    index += 1
                if row[i] == 'food':
                    shutil.copyfile(
                        file_path, './eButton_Data/food/'+str(mv_index))
                    mv_index += 1
                    flag = True
            if flag == False:
                shutil.copyfile(
                    file_path, './eButton_Data/nofood/'+str(mv2_index))
                mv2_index += 1

                label.append(label_index[row[i]])
            img_labels_tmp.append(label)
exit()
# print(len(label_index))
# print(len(label_content))
img_labels = []
for i in range(len(img_labels_tmp)):
    tmp = [0 for i in range(809)]
    for j in img_labels_tmp[i]:
        tmp[j] = 1
    img_labels.append(tmp)


# exit()

resnet = models.ResNet(models.resnet.BasicBlock, [3, 4, 6, 3], num_classes=809)
resnet_dict = resnet.state_dict()
pretrained_dict = torch.load("./resnet34.pth")
pretrained_dict = {k: v for k, v in pretrained_dict.items()
                   if k in resnet_dict and k != 'fc.weight' and k != 'fc.bias'}

resnet_dict.update(pretrained_dict)
resnet.load_state_dict(resnet_dict)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
criterion = nn.NLLLoss()
optimizer = optim.SGD(resnet.parameters(), lr=0.001, momentum=0.9)

resnet.to(device)
train_data = []

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])


for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    i = 0
    for i in range(len(img_path)):
        # get the inputs; data is a list of [inputs, labels]
        # inputs = torch.unsqueeze(
        #     transform(Image.open(img_path[i])), 0).to(device)
        labels = img_labels[i]
        labels = torch.Tensor(labels).long()
        labels = labels.view(1, -1).to(device)

        img = Image.open(img_path[i])
        img_t = transform(img)
        inputs = torch.unsqueeze(img_t, 0).to(device)
        optimizer.zero_grad()

        # forward + backward + optimize

        outputs = resnet(inputs)
        # print(type(inputs))
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
torch.save(resnet.state_dict(), "./resnet_new.pth")
