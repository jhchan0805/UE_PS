import setup_path
import airsim
import random
import time
from airsim.types import Vector3r, Pose, Quaternionr
import numpy as np
import os
import cv2

client = airsim.VehicleClient()
client.confirmConnection()
client.reset()

# List of Asset 
assets = client.simListAssets()
print(f"Assets: {assets}")


###############################################################################################
# get type of image
response_scene = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene,False,False)])
response_scene = response_scene[0]

# get numpy array
img_scene = np.fromstring(response_scene.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_scene = img_scene.reshape(response_scene.height, response_scene.width, 3) #RGB Image

# write to png 
airsim.write_png(os.path.normpath('before' + '.png'), img_scene)
###############################################################################################



scale = airsim.Vector3r(1.0, 1.0, 1.0) # Lighting Scale
asset_name = 'PointLightBP'
desired_name = "New_Lighting"


lights = client.simListSceneObjects("PointLight.*")
pose = client.simGetObjectPose(lights[0])
print(pose)

x = pose.position.x_val #+ np.random.uniform(-1,1)
#y = pose.position.y_val + np.random.uniform(-1,1)
#z = pose.position.z_val + np.random.uniform(-1,1)
print("x",x)
#print("y",y)
#print("z",z)
#client.simDestroyObject(lights[0])
#time.sleep(4.0)

pose = airsim.Pose(position_val=airsim.Vector3r(-10,-10,-10))

#obj_name = client.simSpawnObject(desired_name, asset_name, pose, scale, True)
print("Object is moving")

obj_name = client.simSetObjectPose("PointLightJH",pose,teleport=True)
print(pose)


###############################################################################################
# get type of image
response_scene = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene,False,False)])
response_scene = response_scene[0]

# get numpy array
img_scene = np.fromstring(response_scene.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_scene = img_scene.reshape(response_scene.height, response_scene.width, 3) #RGB Image

# write to png 
airsim.write_png(os.path.normpath('after' + '.png'), img_scene)
###############################################################################################



time.sleep(10.0)
client.reset()
"""
print(f"Created object {obj_name} from asset {asset_name} "
      f"at pose {pose}, scale {scale}")

all_objects = client.simListSceneObjects()
if obj_name not in all_objects:
    print(f"Object {obj_name} not present!")

time.sleep(10.0)

print(f"Destroying {obj_name}")
#client.simDestroyObject(obj_name)

"""

