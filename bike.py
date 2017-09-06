class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed, miles):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    # # this is a method we created to help a user login
    def displayInfo(self):
        print "Price is $",self.price
        print "Max speed is: ",self.max_speed
        print "Total miles: ",self.miles
        print "\n"
        return self

    def ride(self):
        self.miles += 10
        print "Riding bike.. Miles increased by 10"
        print "Total miles: ", self.miles
        print "\n"
        return self

    def reverse(self):
        if (self.miles > 5):
            self.miles -= 5
            print "Rolling odometer back by 5"
            print "Total miles now:", self.miles
            print "\n"
        else: print "not enough miles to roll back"

        return self
#now create an instance of the class
new_bike1 = Bike(30,40,100)
new_bike2 = Bike(40,50,10)
new_bike3 = Bike(60,80,10)

# Have the first instance ride three times, reverse once and have it displayInfo().
#  Have the second instance ride twice, reverse twice and have it displayInfo().
#   Have the third instance reverse three times and displayInfo().
#

print "--------- BIKE 1 -----------\n"
new_bike1.displayInfo().ride().reverse()
# new_bike1.ride()
# new_bike1.resverse()
print "--------- BIKE 2 -----------\n"
new_bike2.ride().ride().reverse().reverse().displayInfo()
print "--------- BIKE 3 -----------\n"
new_bike3.reverse().reverse().reverse().displayInfo()
# print "price is $" + new_bike1.price
# print "max speed is: "+new_bike1.max_speed
# print "miles: "+new_bike1.miles
