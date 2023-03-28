class Bird: #superclass
    def intro(self):
        print("There are many types of birds.")
	
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird): #subclass (inheritance)
    #override flight() method
    def flight(self):
        print("Sparrows can fly.")
	
class ostrich(Bird): #subclass (inheritance)
    #override flight() method
    def flight(self):
        print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro() #There are many types of birds.
obj_bird.flight() #Most of the birds can fly but some cannot.

obj_spr.intro() #There are many types of birds.
obj_spr.flight() #Sparrows can fly.

obj_ost.intro() #There are many types of birds.
obj_ost.flight() #Ostriches cannot fly.
