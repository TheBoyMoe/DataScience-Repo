import numpy as np

cupcakes = np.array([2.0, 0.75, 2.0, 1.0, 0.5])

# each row represents a recipe, each column an ingredient
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

eggs = recipes[:, 2]  # select entire 3rd column

# which recipes require exactly 1 egg
require_one_egg = recipes[(eggs == 1)]
print(require_one_egg)

# select the 3rd row, every column
cookies = recipes[2, :]
print(cookies)

# ingredients for a double batch of cupcakes
double_batch = cupcakes * 2
print(double_batch)

grocery_list = cookies + double_batch
print(grocery_list)
