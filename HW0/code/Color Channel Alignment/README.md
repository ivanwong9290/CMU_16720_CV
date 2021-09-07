# Description
This code takes in a picture that was separated by its RGB channels and attempts to stitch the channel images back together using a horizontal and vertical shift dictated by a cost function of Sum of Squared Differences (SSD). <br/>
<br/>
## Contents
- script1.py contains the main loop for the work sequence <br/>
- alignChannels.py mainly contains a nested for-loop to try all combinations of neighborhood (up to 30 pixels away) to search for shifts with minimum SSD, it returns the rectified image based on the optimal horizontal/vertical shifts
## Results
Before <br/>
![Capture1](https://user-images.githubusercontent.com/71652695/132289868-fdd42110-5081-4738-bf27-04a48f0027b2.PNG) <br/>
After <br/>
![Capture](https://user-images.githubusercontent.com/71652695/132289883-84ab9255-6180-4237-b136-fb3ef6ee1958.PNG)


