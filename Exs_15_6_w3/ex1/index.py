import torch
import torch.nn as nn
import softmax

data = torch.Tensor([1, 2, 3])
softmax1 = softmax.Softmax()
print(softmax1.calc(data))

# data = torch.Tensor([1, 2, 3])
# softmax_function = nn.Softmax(dim=0)
# output = softmax_function(data)
# assert round(output[0].item(), 2) == 0.09
# print(output)
