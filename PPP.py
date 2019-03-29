import argparse
import os
import numpy as np
import math

import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

import torch.nn as nn
import torch.nn.functional as F
import torch

os.makedirs("images",exist_ok=True)
parser = argparse.ArgumentParser()
parser.add_argument("--n_epochs",type=int,default=200,help="number of epochs of training")
parser.add_argument("--batch_size",type=int,default=64,help="size of the batches")
parser.add_argument("--lr",type=float,default=0.0002,help="adam: learning rate")
parser.add_argument("--b1",type=float,default=0.5, help="adam:decay of first order momentum of gradient")
parser.add_argument("--b2",type=float,default=0.999,help="adam: decay of second order momentum of gradient")
parser.add_argument("--n_cpu",type=int,default=8,help="number of cpu threads to use during batch generation")
parser.add_argument("--latent_dim",type=int, default=100,help="dimensionality of the latent space")
parser.add_argument("--n_classes",type=int, default=10,help="number of classes for dataset")
parser.add_argument("--image_size",type=int,default=32,help="size of each iamge dimension")
parser.add_argument("--channels",type=int,default=1,help="number of image channels")
parser.add_argument("--sample_interval",type=int,default=400,help="interval between image sampling")
opt=parser.parse_args()
print(opt)

img_shape=(opt.channels,opt.image_size,opt.image_size)
print(img_shape)

cuda = True if torch.cuda.is_available() else False
print(cuda)

class Generator(nn.Module):
	def __init__(self):
		super(Generator,self).__init__()
		self.label_emb = nn.Embedding(opt.n_classes,opt.n_classes)

		def block(in_feat,out_feat,normalize=True):
			layers = [nn.Linear(in_feat,out_feat)]
			if normalize:
				layers.append(nn.BatchNorm1d(out_feat,0.8))
			layers.append(nn.LeakyReLU(0.2,inplace=True))
			return layers

		self.model =  nn.Sequential(
			*block(opt.latent_dim+opt.n_classes,128,normalize=False),
		)