import glob
import os
import h5py
import numpy as np
from PIL import Image
images = []
sorry = os.path.join('/home/vivalab/Vijay/Selfie/Selfie/negatives/', '*')
png_files_path1 = glob.glob(os.path.join(sorry))
sorry = os.path.join('/home/vivalab/Vijay/Selfie/Selfie/positives/', '*')
png_files_path2 = glob.glob(os.path.join(sorry))

i=0
a=np.empty((len(png_files_path1)+len(png_files_path2),32,32,3))

for filename in png_files_path1:
    im = Image.open(filename)  # .convert("L")  # Convert to greyscale
    #im=im.convert('L')
    im = np.asarray(im, np.uint8)
    a[i,:,:,:] = im;
    # print(type(im))
    # get only images name, not path
    #image_name = filename.split('/')[-1].split('.')[0]
    #images = np.concatenate((im[...,np.newaxis],images[...,np.newaxis]),axis=-1)
    #image_name = 1
    #images.append([int(image_name), im])
    i=i+1
    print(i)

for filename in png_files_path2:
    im = Image.open(filename)  # .convert("L")  # Convert to greyscale
    #im=im.convert('L')
    im = np.asarray(im, np.uint8)
    a[i,:,:,:] = im;
    # print(type(im))
    # get only images name, not path
    #image_name = filename.split('/')[-1].split('.')[0]
    #images = np.concatenate((im[...,np.newaxis],images[...,np.newaxis]),axis=-1)
    #image_name = 1
    #images.append([int(image_name), im])
    i=i+1
    print(i)

#big = np.concatenate(tuple(images)) 

#images = sorted(images, key=lambda image: image[0])
negatives = np.zeros((len(png_files_path1), 1))
positives = np.ones((len(png_files_path2), 1))
labels = np.concatenate((negatives, positives), axis=0)

hf1 = h5py.File('data.h5', 'w')
hf1.create_dataset('dataset_1', data=a)
hf1.close()

hf2 = h5py.File('labels.h5', 'w')
hf2.create_dataset('dataset_1', data=labels)
hf2.close()

images_only = [np.asarray(image[1], np.uint8) for image in images]  # Use unint8 or you will be !!!
#images_only = np.array(images_only)
images_only = np.asarray(images_only)

print(images_only.shape)



[(random.randint(0,100), random.randint(0,200), 32, 32) for x in range(10)]
