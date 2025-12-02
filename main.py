# Code 1: Basic Grouping (distance between all points)
import torch

# Four points in 2D
data = torch.tensor([
    [1.0, 1.0],
    [8.0, 8.0],
    [2.0, 1.0],
    [9.0, 9.0]
])

# Distance between each pair of points
distances = torch.cdist(data, data)
print(distances)


# Code 2: Two-Cluster Pattern
(Near points cluster together)
import torch

# Two small points and two large points
data = torch.tensor([
    [1.0, 0.0],
    [2.0, 1.0],
    [8.0, 9.0],
    [9.0, 8.0]
])

distances = torch.cdist(data, data)
print(distances)


# Code 3: Find Who Is Closest To Whom
import torch

points = torch.tensor([
    [1.0, 1.0],
    [2.0, 2.0],
    [8.0, 8.0],
    [9.0, 9.0]
])

distance_matrix = torch.cdist(points, points)
print(distance_matrix)
