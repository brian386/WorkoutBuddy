import cv2
import mediapipe as mp
import math
from pose_detection import *
from exercises import *
def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = pose_detector()
    cur_session = {'reps': 0, 'up': True}
    while True:
        ret, img = cap.read()
        lmList = detector.find_position(img)
        
        if len(lmList) != 0:
            #print(lmList['right_pinky'], lmList['right_wrist'], lmList['right_thumb'])
            count_hip_thrust(cur_session, detector,lmList)
            
            print(math.floor(cur_session['reps']))
        cv2.imshow("vid",detector.find_pose(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

if __name__ == "__main__":
    main()

cv2.destroyAllWindows()