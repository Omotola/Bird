class User:
    """
             This class represents a User
             ...

             Attributes
             ----------
             userId : str
                 The user Id of the User
             rides : Array of ride Objects
                 The rides associated with this user

                 """
    def __init__(self,user_id):
        self.userId = user_id
        self.rides = []

    def AddRide(self,ride):
        """Adds ride to the User.

                     Parameters
                     ----------
                    ride: Ride Object
                         The ride to be added to the user
                         """
        self.rides.append(ride)


    def CalculateAmountSpent(self):
        """Handles the start of a ride.

                     Return
                     ----------
                     totalAmount: float
                            The total amount spent on all rides
                         """
        totalAmount = 0
        for ride in self.rides:
            totalAmount+=ride.GetCost()
        return round(totalAmount,2)


    def GetID(self):
        """Getter for id

             Return
             ----------
             id: str
                 Id for the User """
        return self.userId