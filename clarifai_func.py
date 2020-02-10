#!/usr/bin/env python
# coding: utf-8

# 任何系统可以使用anaconda jupyter即可，因为clarifai种子可以处理的图片有限，大概3000左右。需要多次更改种子进行处理。
# 使用方法通过注释标注。
# clarifai的库需要在官网（www.clarifai.com）上下载。

# In[1]:


import os
import csv

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import Video as ClVideo


# In[2]:


import time


def tic():
    globals()['tt'] = time.perf_counter()


def toc():
    print('\nElapsed time: %.8f seconds\n' % (time.perf_counter()-globals()['tt']))

#api = ClarifaiApp(api_key='bd1cebb60c4046a4af86c01237447784')

def rec(Path, Api):

    api = ClarifaiApp(api_key=Api)

    # Input the image directory, For example: C:/Data/ID81_Oct.07/ :')
    # imagedir = 'G:\\har_dataset 2\\test set2 (September)\\writing'  #更改存储图片的路径
    imagedir = Path


    # To obtian the filename list of all of the images, which is recorded in variable filename
    print('Step1: Read the images from directory ', imagedir)
    filename = []
    for root, dirs, files in os.walk(imagedir):
        for fname in files:
            if fname.split('.')[-1].upper() == 'JPG':
                filename.append(os.path.join(root, fname))


    # In[3]:


    filename1 = filename  # 这里更改了名字，为了让进入循环的部分，保证可以被处理


    # In[10]:


    # 改变范围（根据seed情况）(这里是0~3000，3001~6000，6001~9000)更改对应前后的数字
    filename = filename1[:3000]


    # In[15]:


    print('Step2: Get Tags of images, every 100 images will take about 7 to 15 seconds.')

    tic()

    block = int(len(filename)/100)
    blockno = 0
    data_name = []
    data_value = []
    TagResults = []

    for blockno in range(1, block + 1):
        for fileno in range((blockno - 1) * 100, blockno * 100):
            print('blockno is', blockno, 'fileno is', fileno)
            print(filename[fileno])
            response = api.models.get(
                'general-v1.3').predict_by_filename(filename[fileno])
            concepts = response['outputs'][0]['data']['concepts']
            for concept in concepts:
                data_name.append(concept['name'])
                data_value.append(concept['value'])
            data = data_name + data_value
            data.insert(0, filename[fileno])
            TagResults.append(data)
            data_name = []
            data_value = []

    for fileno in range(blockno * 50, len(filename)):
        print('blockno is', (blockno + 1), 'fileno is', fileno)
        print(filename[fileno])
        response = api.models.get(
            'general-v1.3').predict_by_filename(filename[fileno])
        concepts = response['outputs'][0]['data']['concepts']
        for concept in concepts:
            data_name.append(concept['name'])
            data_value.append(concept['value'])
        data = data_name + data_value
        data.insert(0, filename[fileno])
        TagResults.append(data)
        data_name = []
        data_value = []

    # 这里需要更改，每次加入新的seed需要存储在新的result文件夹中，保证前后不会互相overwrite。
    outfilename = 'result3.csv'
    print('Save results to ', outfilename)
    with open(outfilename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(TagResults)
    toc()

def main():
    rec('./clarifai', 'e397b17472584e46b0e146a1ab1e7f75')

if __name__ == '__main__':
    main()

# In[14]:


# 当图片读取数量大于3000时，更改此处的API（邮箱申请），更改新的outfilename，更改filename = filename1[:3000]这里的范围。
# 更改好后，先运行本框，在运行filename = filename1框和之后下一框。
# 重复循环下去，直到所有图片被处理。
#api = ClarifaiApp(api_key='1b0c4f1c64b947fe8c1e4507e42e2eeb')


# In[ ]:
