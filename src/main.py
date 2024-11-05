# Imports
import mediapipe as mp
import time
import cv2

# Start the camera and give it a second to set up
camera = cv2.VideoCapture(0)
time.sleep(1)

if not camera.isOpened():
	raise Exception("Could not open video device")

def draw_pose(image, landmarks):
	# Copy the image
	landmark_image = image.copy()
	
	# Get the dimensions of the image
	height, width, _ = image.shape

	# Draw all landmark circles
	for landmark in landmarks.landmark:
		x_coord = int(landmark.x * width)
		y_coord = int(landmark.y * height)
		cv2.circle(
			landmark_image,
			(x_coord, y_coord),
			radius=6,
			color=(128, 0, 128),  # Purple color
			thickness=-1  # Fill the circle
		)

	# Map constant landmark connections
	connect_components = [
		# Upper Face
		[1, 4],
		[0, 2],
		[1, 3],
		[2, 7],
		[0, 5],
		[4, 6],
		[5, 8],
		[3],
		[6],

		# Mouth
		[10],
		[9],

		# Body
		[12, 13, 23],
		[11, 14, 24],
		[11, 15],
		[12, 16],
		[13, 17, 19, 21],
		[14, 18, 20, 22],
		[15, 19],
		[16, 20],
		[15, 17],
		[16, 18],
		[15],
		[16],
		[11, 24, 25],
		[12, 23, 26],
		[23, 27],
		[24, 28],
		[25, 31],
		[26, 32],
		[27, 31],
		[28, 32],
		[27, 29],
		[28, 30]
	]
	NODE_AMOUNT: int = len(connect_components)

	def dfs(node_num: int, visited: list[bool]):
		visited[node_num] = True

		x_start = int(landmarks.landmark[node_num].x * width)
		y_start = int(landmarks.landmark[node_num].y * height)
		for next_node in connect_components[node_num]:
			x_end = int(landmarks.landmark[next_node].x * width)
			y_end = int(landmarks.landmark[next_node].y * height)

			# Draw the line between current node and connected node
			cv2.line(
				landmark_image,
				(x_start, y_start),
				(x_end, y_end),
				color=(255, 255, 0),  # Cyan color
				thickness=2
			)

			if not visited[next_node]:
				dfs(next_node, visited)

	# Draw the connections between the landmarks using dfs/flood fill
	for node_number in [0, 9, 11]:
		dfs(node_number, [False] * NODE_AMOUNT)

	'''
	# Draw lines connecting the landmarks using POSE_CONNECTIONS
	connections = mp.solutions.pose.POSE_CONNECTIONS
	for start_idx, end_idx in connections:
		start_landmark = landmarks.landmark[start_idx]
		end_landmark = landmarks.landmark[end_idx]

		x_start = int(start_landmark.x * width)
		y_start = int(start_landmark.y * height)

		x_end = int(end_landmark.x * width)
		y_end = int(end_landmark.y * height)

		cv2.line(
			landmark_image,
			(x_start, y_start),
			(x_end, y_end),
			color=(255, 255, 0),  # Cyan color
			thickness=2
		)
	'''

	return landmark_image

def main():
	''' 
	TODO Task 2
		modify this fucntion to take a photo uses the pi camera instead 
		of loading an image

	TODO Task 3
		modify this function further to loop and show a video
	'''

	# Create a pose estimation model 
	mp_pose = mp.solutions.pose
	
	# start detecting the poses
	with mp_pose.Pose(
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as pose:

		# load test image
		image = cv2.imread("person.png")	

		# To improve performance, optionally mark the image as not 
		# writeable to pass by reference.
		image.flags.writeable = False
		
		# get the landmarks
		results = pose.process(image)
		
		if results.pose_landmarks != None:
			result_image = draw_pose(image, results.pose_landmarks)
			cv2.imwrite('output.png', result_image)
			print(results.pose_landmarks)
		else:
			print('No Pose Detected')

if __name__ == "__main__":
	main()
	print('done')
