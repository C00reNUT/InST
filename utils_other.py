import numpy as np
import torch
def gen_checkerboard(height,width,grid_size):
    '''
        Return : checkerboard [1,1,H,W] Tensor Boolean
    '''
    assert height%grid_size==0 & width%grid_size==0
    grid_x_num = width // grid_size
    grid_y_num = height // grid_size
    row_1 = [i%2 for i in range(grid_x_num)]
    row_2 = [(i+1)%2 for i in range(grid_x_num)]
    grid = []
    for c in range(grid_y_num):
        r = row_1 if c % 2 else row_2
        grid.extend(r)
    grid = torch.Tensor(grid).view(1,1,grid_x_num,1,grid_y_num,1)
    checkerboard = grid.repeat(1,1,1,grid_size,1,grid_size).view(1,1,width,height).bool()    # [1,1,H,W]
    return checkerboard