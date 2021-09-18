import cv2
import mediapipe as mp
import numpy as np
import math
class pose_detector():

    def __init__(self):

        self.drawing_module = mp.solutions.drawing_utils
        self.mp_pose= mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.lm_names = ['nose', 'left_eye_inner', 'left_eye', 'left_eye_outer', 'right_eye_inner','right_eye', 'right_eye_outer', 'left_ear', 'right_ear', 'mouth_left', 'mouth_right', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky', 'left_index', 'right_index', 'left_thumb', 'right_thumb', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_heel', 'right_heel', 'left_foot_index', 'right_foot_index']
    def find_pose(self, img, draw_points = True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        #print(self.results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw_points:
                self.drawing_module.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        
        return img

    def find_position(self,img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        landmarks_list = {}
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                landmarks_list[self.lm_names[id]] = (lm.x,lm.y) 
                cv2.circle(img, (cx,cy),10, (0,0,255), cv2.FILLED)
        
        return landmarks_list

    def calc_angle(self,a,b,c):
        v1 = [a[0]-b[0],a[1]-b[1]]
        v2 = [c[0]-b[0],c[1]-b[1]]
        v1_dot_v2 = v1[0]*v2[0]+v1[1]*v2[1]
        mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
        mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
        cos_abc = v1_dot_v2/(mag_v1*mag_v2)
        return math.acos(cos_abc) * 180 / math.pi