import airsim 
import numpy as np
import os
import cv2

# Connect to AirSim Client 
client = airsim.MultirotorClient()

# get type of image
response_normal = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.SurfaceNormals,False,False)])
response_scene = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene,False,False)])
response_depth = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.DepthVis,False,False)])



response_normal = response_normal[0]
response_scene = response_scene[0]
response_depth = response_depth[0]


# get numpy array
img_normal = np.fromstring(response_normal.image_data_uint8, dtype=np.uint8) 
img_scene = np.fromstring(response_scene.image_data_uint8, dtype=np.uint8) 
img_depth = np.fromstring(response_depth.image_data_uint8, dtype=np.uint8) 


# reshape array to 4 channel image array H X W X 4
img_normal = img_normal.reshape(response_normal.height, response_normal.width, 3)#Surface map
img_scene = img_scene.reshape(response_scene.height, response_scene.width, 3) #RGB Image
img_depth = img_depth.reshape(response_depth.height, response_depth.width, 3)
mask = cv2.bitwise_not(img_depth) #Mask Image



# write to png 
airsim.write_png(os.path.normpath('normal' + '.png'), img_normal) 
airsim.write_png(os.path.normpath('scene' + '.png'), img_scene)
airsim.write_png(os.path.normpath('mask' + '.png'), mask) 
