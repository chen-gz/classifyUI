from torchvision import models
import torch
# from summary import summary
from torchsummary import summary
import torch.utils.model_zoo as model_zoo

model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
}

# resnet = models.resnet34(pretrained=True)
# print(resnet)
# summary(resnet, (3, 512, 512))
# resnet.summary()
resnet = models.ResNet(models.resnet.BasicBlock, [3, 4, 6, 3], num_classes=20)
resnet_dict = resnet.state_dict()
pretrained_dict = torch.load("./resnet34.pth")
pretrained_dict = {k: v for k, v in pretrained_dict.items()
                   if k in resnet_dict and k != 'fc.weight' and k != 'fc.bias'}

resnet_dict.update(pretrained_dict)
resnet.load_state_dict(resnet_dict)
