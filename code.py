# --------------
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 



# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter
with open(path) as f:
        line=csv.reader(f,delimiter=',')
        line=list(line)
header=line[0]
line.remove(header)
data=np.asarray(line)
#print(data)
#print(type(line))
#print(len(line))
#print(line[0])
camp_dict= Counter(data[:,1])
print(len(camp_dict.keys()))
print(camp_dict)
age_groups_targeted=Counter(data[:,3])
age_groups_targeted.keys()

avg_amount=np.mean(data[:,-3].astype(float))
min_amount=np.min(data[:,-3].astype(float))
max_amount=np.max(data[:,-3].astype(float))

print(avg_amount)
print(min_amount)
print(max_amount)
max_clicks=np.max(data[:,-4].astype(int))
max_clicks_adv_id=data[:,0][data[:,-4].astype(int)==max_clicks]
max_clicks_adv_id
most_clicks_purchase=int(data[:,-1][data[:,0]==max_clicks_adv_id])
most_clicks_purchase
max_conversion=np.max(data[:,-1].astype(int))
max_conversion
if most_clicks_purchase >= max_conversion:
    print('Yes') 
else:
        print('No')
ctr=np.array(data[:,-1].astype(float)/data[:,-2].astype(float))
print(ctr)
ctr=ctr.reshape(-1,1)
ctr.shape
data=np.concatenate((data,ctr),axis=1)
print(data.shape)
cpm=data[:,8].astype(float)/data[:,6].astype(float)*1000
cpm=cpm.reshape(-1,1)

data=np.concatenate((data,cpm),axis=1) 

# What are the age groups that were targeted through these ad campaigns?

# What was the average, minimum and maximum amount spent on the ads?

# What is the id of the ad having the maximum number of clicks ?

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
 
# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 



# Create a new column that represents Cost Per Mille (CPM) 


