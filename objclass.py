#Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        #Count number of greetings
        self.greeting_count = 0
        #Bonus challenge
        self.unique_people_greeted = []

    def greet(self, other_person):
        if other_person not in self.unique_people_greeted: #bonus
            print ('Hello %s, I am %s!' % (other_person.name, self.name))
            self.unique_people_greeted.append(other_person) #bonus
        self.greeting_count += 1

    def num_unique_people_greeted(self):
        print(len(self.unique_people_greeted))

    #Add a Method 2
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    #Add a add_friend method
    def add_friend(self, other_person):
        self.friends.append(other_person)

    # Add a num_friend method
    def num_friends(self):
        print(len(self.friends))

    # __repr__
    def __repr__(self):
        return f"{self.name}, {self.email}, {self.phone}"


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(f"Sonny's email is {sonny.email} and her phone number is {sonny.phone}.")

print(f"Jordan's email is {jordan.email} and his phone number is {jordan.phone}.")

#Add a Method 2
sonny.print_contact_info()

#Add a add_friend method
jordan.add_friend(sonny)
print(jordan.friends)

# Add a num_friend method
jordan.num_friends()

sonny.num_unique_people_greeted()

# Make your own class
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

#Add a method
    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle("Acura", "TSX", "2011")

print(car.make, car.model, car.year)


car.print_info()
