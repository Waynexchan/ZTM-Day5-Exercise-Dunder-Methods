#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]

  def __getattr__(self, name):
      return f'{name} not found'

  def __eq__(self, other):
      if isinstance(other, Toy):
        return self.color == other.color and self.age ==other.age
      return False
  def __hash__(self):
      return hash((self.color, self.age))

  
      
action_figure = Toy('red', 0)
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
print(action_figure.some_attribute)
action_figure2 = Toy('red', 5)
print(action_figure == action_figure2)
print(hash(action_figure))
    