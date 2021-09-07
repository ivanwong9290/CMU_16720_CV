# Description
This code takes in a picture that was separated by its RGB channels and attempts to stitch the channel images back together using a horizontal and vertical shift dictated by a cost function of Sum of Squared Differences (SSD). <br/>
<br/>
## Contents
- script1.py contains the main loop for the work sequence <br/>
- alignChannels.py mainly contains a nested for-loop to try all combinations of neighborhood (up to 30 pixels away) to search for shifts with minimum SSD, it returns the rectified image based on the optimal horizontal/vertical shifts
