import airsim 
import numpy as np
import os
import cv2

#https://blog.actorsfit.com/a?ID=00850-7ce2aad1-b508-43ed-8c05-04c7540105b8
#.mat & .npy tutorial

# Connect to AirSim Client 
client = airsim.MultirotorClient()


lights = client.simListSceneObjects("PointLight.*")
pose = client.simGetObjectPose(lights[0])
print("Position of Light:",pose)

###############################################################################################
# get type of image
response_scene = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.SurfaceNormals,False,False)])

response_scene = response_scene[0]

# get numpy array

img_scene = np.fromstring(response_scene.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_scene = img_scene.reshape(response_scene.height, response_scene.width, 3) #RGB Image
img_scene = np.flipud(img_scene)

#To get Normalize map
data_normal = ((img_scene/255)*2) -1



# write to png 
print("Writing image....")
airsim.write_png(os.path.normpath('scene_single' + '.png'), img_scene)
np.save('normal.npy',data_normal)



###############################################################################################



