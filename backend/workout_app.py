import cv2
import mediapipe as mp
from pose_detection import *

def main():
    cap = cv2.VideoCapture(0)
    detector = pose_detector()
    while True:
        ret, img = cap.read()
        lmList = detector.find_position(img)
        
        if len(lmList) != 0:
            #print(lmList['right_pinky'], lmList['right_wrist'], lmList['right_thumb'])
            print(detector.calc_angle(lmList['right_shoulder'], lmList['right_elbow'], lmList['right_wrist']))
            #print(detector.calc_cos_angle([1,0,0],[0,0,0],[0,1,0]))
        
        cv2.imshow("hello",detector.find_pose(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

if __name__ == "__main__":
    main()