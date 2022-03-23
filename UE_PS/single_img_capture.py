import airsim 
import numpy as np
import os
import cv2

# Connect to AirSim Client 
client = airsim.MultirotorClient()



###############################################################################################
# get type of image
response_scene = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene,False,False)])
response_scene = response_scene[0]

# get numpy array
img_scene = np.fromstring(response_scene.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_scene = img_scene.reshape(response_scene.height, response_scene.width, 3) #RGB Image

# write to png 
airsim.write_png(os.path.normpath('scene_single' + '.png'), img_scene)
###############################################################################################



