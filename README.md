# Zuri_cdt 
A module  to help in calculating the best way to avoid hitting impenetrable rocks under the earth. The following parameters are the requirements:

1. Your module works with 2 paramets, which are location a and location b. 
2. Your module looks at point a to b to determine if there are any obstructions and if the obstructions are impenetrable 
3. If there are no obstructions, your module returns false, if there are obstructions your module returns true
4. An obstruction would typically be determined by how long it will take to go from a to b
5. An obstruction is considered impenetrable determine time exceeds expected by 60 mins.

Assumptions:

The following assumptions are true:

1. Another member of the team already developed a module to calculation time taken from one distance to another, you can simulate the result from this module (You don't need to develop this module, just simulate the results from the module in minutes).
2. Your module knows the following: 1. the speed of the machine 2. the distance between a - b (in miles), and 3. the expected time it will take to get from a - b (calculate expected time by using speed and distance). 
3. the above speed, distance and time taken cannot be hardcoded into your module because point a and b are never fixed
