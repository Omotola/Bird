
# Import classes
from Bird import Bird
from BirdRide import BirdRide
from User import User

# open file
file = open("../events.txt","r")

# Initialize structures
birds = {}
users = {}

# Read information from file
for line in file:
    timestamp, bird_id, event_type, x, y, user_id = line.strip().split(",")

    if event_type == "DROP":
        birds[bird_id] = Bird(bird_id,x,y,timestamp)
    elif event_type == "START_RIDE":

        # Create New User
        if user_id not in users:
            users[user_id] = User(user_id)

        user = users[user_id]
        # Create New Ride
        bird = birds[bird_id]
        tmpRide = BirdRide()
        tmpRide.StartRide(x,y,bird,user,timestamp)

        # Add Ride to the bird
        bird.NewRide(tmpRide,timestamp)

        #Add Ride to the User
        user.AddRide(tmpRide)


    elif event_type == "END_RIDE":
        # Complete Ride
        bird = birds[bird_id]
        bird.CompleteRide(timestamp,x,y)


# Question 1: Total Number of Bird Vehicles
print("1. There are ",len(birds.keys())," birds total in simulation \n")

# Question 2: Bird with Max Distance From DropPoint
print("2. The Bird with the furthest distance from its drop point and the corresponding distance in km is")
print(max([(bird.GetID(),bird.GetDistanceFromDropPoint()) for bird in birds.values()],key=lambda x:float(x[1])),"\n")

# Question 3: Bird with Max Total Distance
print("3. The Bird that traveled furthest overall and its corresponding distance in km is")
print(max([(bird.GetID(),bird.GetTotalDistanceTraveled()) for bird in birds.values()],key=lambda x:float(x[1])),"\n")

# Question 4: User who spent most
print("4. The User that spent the most and the corresponding amount spent is")
print(max([(user.GetID(),user.CalculateAmountSpent()) for user in users.values()],key=lambda x:float(x[1])),"\n")

# Question 5: Bird with Max WaitTime
print("5. The Bird with the maximum wait times between rides and the corresponding wait time in seconds is")
print(max([(bird.GetID(),bird.GetMaxWaitTime()) for bird in birds.values()],key=lambda x:float(x[1])),"\n")

# Question 6: What is the average speed travelled across all rides? -> Total Distance/ Total Duration for all rides
print("6. The average speed for all rides in km/s is")
print((sum(list([bird.GetTotalDistanceTraveled() for bird in birds.values()])))/(sum(list([bird.GetTotalDuration() for bird in birds.values()]))))