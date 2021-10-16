import torch
import numpy as np
import cpp as cpp

# x = torch.randn(4)
# y = torch.randn(4)
# print(ncpp.sigmoid_add(x, y))

# shape = ncpp.Shape(5, 3)
# cArray = ncpp.NdArray(shape)
# ret = cArray.ones()
# cArray = ncpp.zeros_like(cArray);
# print(type(cArray));
# print(type(cArray.getNumpyArray()));
# print(cArray.getNumpyArray());
# print(ncpp.toNumCpp(cArray.getNumpyArray()));

def printResult(x, y):
    print('numpy')
    print(x @ y)

    x = cpp.NdArray(x)
    y = cpp.NdArray(y)
    print('numcpp')
    print(cpp.dot(x, y).getNumpyArray())

garbageCollector = list()

def dot_test():
    x = np.random.randn(5, 3)
    x = cpp.NdArray(x)
    y = np.random.randn(3, 5)
    y = cpp.NdArray(y)  

    result = cpp.dot(x, y)
    return result

# def addGarbage(x):
#     garbageCollector.append(x)
#     return x

# def garbageClean():
#     for i in range(len(garbageCollector)):
#         garbageCollector[i].memoryFree()


# for i in range(1):
#     x = np.random.randn(5, 3)
#     y = np.random.randn(3, 5)
#     x = cpp.NdArray(x)
#     y = cpp.NdArray(y)
#     addGarbage(cpp.dot(x, y))
#     garbageClean()
#     print('==============================')

for i in range(1):
    r = cpp.rnn(0.01, 28, 28, 128, 10)
    cpp.memoryFree()

    # images = np.random.randn(28, 1, 28)
    # hprev = np.random.randn(128, 1)
    # labels = np.array([[2],])
    # labels = cpp.NdArray(labels)

    # addGarbage(r.forward(images, hprev))

# xx.print()

# cpp.test_gpu()
# cpp.test_gpu_matrix_add()

# print(np.random.random((3, 4)))

# r = cpp.rnn(0.01, 28, 28, 128, 10)
# images = np.random.randn(28, 1, 28)
# hprev = np.random.randn(128, 1)
# labels = np.array([[2],])
# labels = cpp.NdArray(labels)

# print("one")
# outputs = r.forward(images, hprev)
# print("two")
# outputs = r.forward(images, hprev)

# outputs = r.forward(images, hprev)
# Y, loss = r.cross_entropy_loss(outputs, labels)
# gradients = r.backward(r.deriv_softmax(Y, labels))
# r.optimizer(gradients)

# test = cpp.bindTest()
# x = test.return_test()
# test.memoryFree()
# x.memoryFree()