from torchvision import models
import torch
# from summary import summary
from torchsummary import summary
import torch.utils.model_zoo as model_zoo
import torchvision.datasets as dset
import torchvision.transforms as transforms

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

resnet = models.ResNet(models.resnet.BasicBlock, [3, 4, 6, 3], num_classes=20)
resnet_dict = resnet.state_dict()
pretrained_dict = torch.load("./resnet34.pth")
pretrained_dict = {k: v for k, v in pretrained_dict.items()
                   if k in resnet_dict and k != 'fc.weight' and k != 'fc.bias'}

resnet_dict.update(pretrained_dict)
resnet.load_state_dict(resnet_dict)

# cap = dset.CocoCaptions(root='', annFile='', transform=transforms.ToTensor)
###################################
# coco
dataDir = 'train2017'
dataType = 'train2017'
annFile = 'coco_data/annotations/instances_train2017.json'
# 初始化标注数据的 COCO api
coco = COCO(annFile)


cats = coco.loadCats(coco.getCatIds())
# nms = [cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

foods = []
for cat in cats:
    if cat['supercategory'] == 'food':
        foods.append(cat['id'])
        print(cat['name'])

# nms = set([cat['supercategory'] for cat in cats])
# print('COCO supercategories: \n{}'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=foods)

imgIds = []
for i in foods:
    imgIds.append(coco.catToImgs[i])

# img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]


for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data
        # zero the parameter gradients
        optimizer.zero_grad()
        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')
