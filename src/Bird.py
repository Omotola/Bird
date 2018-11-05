import math


class Bird:
    """
       This class represents a Bird
       ...

       Attributes
       ----------
       id : str
           The Id of the bird
       idleTime : int
           The "End" timestamp of the last ride for the bird
       waitTimes : array of ints
           array of waitTimes i.e  idle time between each ride
       rides : array of Ride objects
            the rides associated with the bird
       dropx,dropy : float
           the location of the drop position for the bird
        currRide : Ride object
           the active ride the bird is on
       totalDistance : float
            Overall distance covered by bird on all rides
       totalDuration : int
           the total duration for all rides by bird
       distanceFromDropPoint : float
           distance from the end location of the last ride to the bird's drop point
           """

    def __init__(self,id,dropx,dropy,droptime):
        self.id =id
        self.idleTime = int(droptime)
        self.waitTimes = []
        self.rides = []
        self.currRide = None
        self.dropX = dropx
        self.dropY = dropy
        self.totalDistance = 0
        self.totalDuration = 0
        self.distanceFromDropPoint=0


    def NewRide(self, ride, startTime):
        """Handles a new ride for the bird.

             Parameters
             ----------
             ride : Ride Object
                 The sound the animal makes (default is None)
             startime: int
                 timestamp for the start of the ride"""

        self.currRide = ride
        self.waitTimes.append(int(startTime) - int(self.idleTime))

    def CompleteRide(self,endTime,endX,endY):
        """Completes the bird's active ride.

             Parameters
             ----------
             endTime : Ride Object
                 Timestamp for the end of the ride
             endY, endX: float
                 End location for the ride"""

        ride = self.currRide
        ride.EndRide(endX,endY,endTime)
        self.totalDistance+=ride.GetDistance()
        self.totalDuration+=ride.GetDuration()
        self.rides.append(ride)
        self.currRide = None
        self.idleTime = endTime
        self.CalculateDistanceFromDropPoint(endX,endY)


    def CalculateDistanceFromDropPoint(self,endPosX,endPosY):
        """Calculate the bird's distance from the drop point

             Parameters
             ----------
             endPosY, endPosX: float
                 End location coordinates"""


        R = 6371.0

        startLat = math.radians(float(self.dropX))
        startLong = math.radians(float(self.dropY))

        endLat = math.radians(float(endPosX))
        endLong = math.radians(float(endPosY))

        longDist = endLong - startLong
        latDist = endLat - startLat

        a = math.sin(latDist / 2) ** 2 + math.cos(startLat) * math.cos(endLat) * math.sin(longDist / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.distanceFromDropPoint = R * c


    def GetTotalDistanceTraveled(self):
        """Getter for overall distance

             Return
             ----------
             totalDistance: float
                 Overall Distance the bird has traveled"""
        return self.totalDistance


    def GetDistanceFromDropPoint(self):
        """Getter for distance from drop point

             Return
             ----------
             distanceFromDropPoint: float
                 Distance from the drop point"""
        return self.distanceFromDropPoint

    def GetMaxWaitTime(self):
        """Getter for maximum wait time

             Return
             ----------
             maxwaitTime: int
                 maximum wait time between rides"""
        return max(self.waitTimes)



    def GetTotalDuration(self):
        """Getter for total Duration

             Return
             ----------
             totalDuration: int
                 total duration over all rides for the bird"""
        return self.totalDuration



    def GetID(self):
        """Getter for id

             Return
             ----------
             id: str
                 Id for the bird """
        return self.id

