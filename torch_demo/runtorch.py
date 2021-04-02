import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


if __name__ == "__main__":
    torch.manual_seed(1)
    lin = nn.Linear(5, 3)  # maps from R^5 to R^3, parameters A, b
    # data is 2x5.  A maps from 5 to 3... can we map "data" under A?
    data = torch.randn(2, 5)
    print(lin(data))  # yes