import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVISES'] = '-1'

import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers,models, optimizers,datasets,losses
from tensorflow.keras.models import Model,Sequential,load_model,save_model,load_model,model_from_json,model_from_yaml,model_from_config
from tensorflow.keras.layers import Dense,Dropout,Flatten,Conv2D,Input,Activation,MaxPooling2D,BatchNormalization,LSTM,Embedding,MaxPool2D,UpSampling2D,concatenate
from tensorflow.keras.layers import Reshape, Concatenate,LeakyReLU
from tensorflow.keras.optimizers import Adam,SGD,RMSprop,Nadam,Adadelta,Adamax
from tensorflow.keras.preprocessing import image,sequence,text
from tensorflow.keras.utils import plot_model,to_categorical,Sequence,multi_gpu_model,normalize
from tensorflow.keras.datasets import mnist,cifar10,fashion_mnist,imdb,cifar100,reuters,boston_housing
from tensorflow.keras.losses import binary_crossentropy,categorical_crossentropy,mse,mean_absolute_error,mean_squared_error,sparse_categorical_crossentropy
from tensorflow.keras.losses import kullback_leibler_divergence,kullback_leibler_divergence,squared_hinge,mean_squared_logarithmic_error,poisson
from tensorflow.keras.applications import resnet50,inception_v3,inception_resnet_v2,mobilenet,vgg19,mobilenet_v2
from tensorflow.keras.activations import relu, softmax, sigmoid, tanh, deserialize, elu, exponential, linear, softplus, softsign, selu

import numpy as np

x = np.linspace(-5, 5, 100)
plt.plot(x, relu(x))
plt.plot(x, LeakyReLU(alpha=0.2)(x))
plt.plot(x, sigmoid(x))
plt.plot(x, tanh(x))
plt.plot(x, elu(x))
plt.plot(x, softsign(x))
plt.plot(x, softsign(x))
plt.legend(['relu', 'LeakyReLU','sigmoid','tanh','elu','softsign', 'softmax'])
plt.show()




