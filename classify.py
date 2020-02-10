import os
import json
from PIL import Image
from torchvision import models
import torch
from torchvision import transforms


class classify:
    def __init__(self):
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )])
        with open('./labels.json') as f:
            labels = json.load(f)
        with open('./food.json') as f:
            food_labels = json.load(f)
            self.food_labels = {int(key): value for key,
                                value in food_labels.items()}
        self.resnet = models.resnet34(pretrained=False)
        self.resnet.load_state_dict(torch.load('./resnet34.pth'))

        self.resnet.eval()
        # self.resnet.cuda()

    def getClass(self, path, name):
        # preprocess
        # print(path)
        # print(path + '/' + name)
        img = Image.open(path + '/' + name)
        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t, 0)
        # batch_t = batch_t.cuda(non_blocking=True)

        # get answer
        out = self.resnet(batch_t)
        _, indices = torch.sort(out, descending=True)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

        have_food = False
        for idx in indices[0][:5]:
            if self.food_labels.get(int(idx)) != None:
                have_food = True
        return have_food

    def getAllClass(self, path, names):
        csv = csv = open(path + '/classify.csv', 'w')
        for name in names:
            csv.write(path + '/' + name + ',' + name + '    ,')
            have_food = self.getClass(path, name)
            if have_food:
                csv.write('1\n')
            else:
                csv.write('0\n')
        csv.close()
