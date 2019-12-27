def sum_up(*args, **kwargs):
   # args -> [1, 2, 3, 4]
   # kwargs -> {'name': 'Jack', 'zip': '12345'}
   total = 0
   for n in number:
       total += n
   return total


sum_up(1, 2, 3)


sum_up(1, 2, 3, 4, name="Jack", zip="12345")

args = [1, 2, 3, 4]
kwargs = {'name': 'Jack', 'zip': '12345'}

sum_up(*args, **kwargs)

kwargs['name'] = 'Gregg'
sum_up(*args, **kwargs)



class Animal:
   def __init__(self, name):
       self.name = name

   def get_sound(self):
       return "Animal sound"

   def make_sound(self):
       print(f"{self.name} says {self.get_sound()}")


class Dog(Animal):
   def __init__(self, name, breed):
       Animal.__init__(self, name)
       self.breed = breed

   def get_sound(self):
       return "Woof"

   def make_sound(self):
       print(f"{self.name} growls")


miles = Animal("Miles")
miles.make_sound() -> "Miles says Animal sound"

dominic = Dog("Dominic", "Brown Dog")
dominic.make_sound() -> "Dominic growls"

dominic -> type(Dominic) -> Dog

dominic.make_sound()
<->
Dog.make_sound(dominic)

---

DEBUG_MODE = False


def do_debug_logging(func):
   def new_func():
       if DEBUG_MODE:
           print(f"Calling {func}")
       return func()

   return new_func

--------


def login_required(func):
   def new_func():
       if is_logged_in():
           return func()
       else:
           raise NotAllowedException
   return new_func


@login_required
def my_account_view():
   pass


@login_required
def my_billing_view():
   pass
