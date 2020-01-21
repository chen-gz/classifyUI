# # cap = dset.CocoCaptions(root='', annFile='', transform=transforms.ToTensor)
# ###################################
# # coco
# dataDir = 'train2017'
# dataType = 'train2017'
# annFile = 'coco_data/annotations/instances_train2017.json'
# # 初始化标注数据的 COCO api
# coco = COCO(annFile)

# cats = coco.loadCats(coco.getCatIds())
# nms = [cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

# foods = []
# for cat in cats:
#     if cat['supercategory'] == 'food':
#         foods.append(cat['id'])
#         print(cat['name'])

# nms = set([cat['supercategory'] for cat in cats])
# print('COCO supercategories: \n{}'.format(' '.join(nms)))

# catIds = coco.getCatIds(catNms=foods)

# imgIds = []
# for i in foods:
#     imgIds.append(coco.catToImgs[i])

# img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]
