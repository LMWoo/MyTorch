import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import time
import numpy as np
import cpp as cpp

# matMul test
x = cpp.cppTensor(np.ones((512, 257)))
x.cuda()
y = cpp.cppTensor(np.ones((257, 512)))
y.cuda()
y_t = cpp.cppTensor(np.ones((512, 257)))
y_t.cuda()
result = cpp.cppTensor(np.zeros((512, 512)))
result.cuda()

start_time = time.time()
for i in range(10000):
    cpp.matMul_gpu(result, x, y, False)
print("time : {}".format(time.time() - start_time))

start_time = time.time()
for i in range(10000):
    cpp.transpose_gpu(y_t, y)
    cpp.transpose_matMul_gpu(result, x, y_t)
print("time : {}".format(time.time() - start_time))

start_time = time.time()
for i in range(10000):
    cpp.matMul_gpu(result, x, y, False)
print("time : {}".format(time.time() - start_time))

start_time = time.time()
for i in range(10000):
    cpp.transpose_gpu(y_t, y)
    cpp.transpose_matMul_gpu(result, x, y_t)
print("time : {}".format(time.time() - start_time))