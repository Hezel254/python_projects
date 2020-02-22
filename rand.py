import random
Meals_list = ['Tea','Coffee','Beans','Eggs','chapo','chipo']
random.seed(2)
sample_list = random.sample(Meals_list,2)

print(random.sample(sample_list,2))

random.seed(3)
sample_list = random.sample(Meals_list,2)
print(sample_list)