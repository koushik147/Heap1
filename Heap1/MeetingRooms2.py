def minMeetingRooms(self,intervals):
    rooms = [] # creating an empty rooms array
    intervals.sort(key = lambda x:x[0]) # defining the custom sort function with lambda function
    heappush(rooms,intervals[0][1]) # push the intervals[0][1] into heap
    
    for incoming in intervals[1:]: # run until intervals and rooms is lesser than incoming 
        if rooms[0]<=incoming[0]:
            heappop(rooms) # then pop from the heap
        heappush(rooms,incoming[1]) # push the incoming[1] into the heap
    return len(rooms) # returning the length of rooms