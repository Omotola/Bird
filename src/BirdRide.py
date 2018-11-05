import math
class BirdRide:
    """
          This class represents a Ride
          ...

          Attributes
          ----------
          associatedBird : Bird Object
              The bird associated with this ride
          associatedUser : User Object
              The user associated with this ride
          distance : float
              The distance covered by this ride
          cost : float
               The amount this ride costs
          startPosX,startPosY : float
              the location of the start position for the ride
          endPosX,endPosY : float
              the location of the end position for the ride
          startTime : int
               The timestamp for the start of the ride
          endTime : int
               The timestamp for the end of the ride
          duration : int
              The duration of the ride
              """
    def __init__(self):
        self.associatedBird = None
        self.associatedUser = None
        self.distance = 0
        self.cost = 0.0
        self.startPosX = 0
        self.startPosY = 0
        self.endPosX = 0
        self.endPosY = 0
        self.startTime = 0
        self.endTime = 0
        self.duration = 0
    def StartRide(self,startX,startY,bird,user,time):
        """Handles the start of a ride.

             Parameters
             ----------
             startX,startY : float
                 The start location of the ride
             user: User object
                 The user associated with the ride
            time: int
                 The time the ride started
                 """
        self.associatedBird = bird
        self.associatedUser = user
        self.startPosX = float(startX)
        self.startPosY = float(startY)
        self.startTime = time

    def EndRide(self,endX,endY,time):
        """Handles the end of a ride.

             Parameters
             ----------
             endX,endY : float
                 The end location of the ride
            time: int
                 The time the ride ended
                 """
        self.endPosX = float(endX)
        self.endPosY = float(endY)
        self.endTime=time

        self.CalculateDistance()
        self.CalculateCost()


    def CalculateCost(self):
        """Calculates the total cost for the ride.
                ...

                 """
        self.duration = float(self.endTime) - float(self.startTime)
        tempDuration = self.duration
        if tempDuration < 60:
            self.cost = 0.0
        else:

            self.cost = 1.0
            while tempDuration > 0:
                self.cost+=0.15
                tempDuration-=60
        self.cost = round(self.cost,2)




    def CalculateDistance(self):
        """Calculates the distance covered by the ride.
                ...

                 """



        R = 6371.0 #radius of earth in km

        startLat = math.radians(self.startPosX)
        startLong = math.radians(self.startPosY)
        endLat = math.radians(self.endPosX)
        endLong = math.radians(self.endPosY)

        longDist = endLong - startLong
        latDist = endLat - startLat

        a = math.sin(latDist / 2) ** 2 + math.cos(startLat) * math.cos(endLat) * math.sin(longDist / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.distance = R * c

    def GetDistance(self):
        """Getter for Distance

             Return
             ----------
             distance: float
                 The distance of the ride """

        return self.distance


    def GetCost(self):
        """Getter for Cost

             Return
             ----------
             cost: float
                 The cost for the ride """

        return self.cost


    def GetDuration(self):
        """Getter for duration

             Return
             ----------
             duration: int
                 Duration for the ride """

        return self.duration