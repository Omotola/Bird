

## Bird Events:

The input to your program is a text file containing a list of Bird events from a completed simulation. Bird events are events which happen in our system, e.g. when a ride is started or ended. A drop event is when a Bird is initially put into the simulation. The format of the events is:

| Data        | Type           | Description  |
| ------------- |-------------| -----|
| timestamp       | Integer        | The time in seconds since the start of the simulation |
| bird_id       | String        | The id of the associated Bird vehicle, e.g. JK5T |
| event_type       | String        | The type of the event is one of START_RIDE, END_RIDE, DROP |
| x       | Double        | The x coordinate of the location of where the event happened in the simulation |
| y       | Double        | The y coordinate of the location of where the event happened in the simulation |
| user_id       | Integer        | The id of the associated user or NULL if the event does not have an associated user |
   

