import cv2
import mediapipe as mp

class pose_detector():

    def __init__(self):

        self.drawing_module = mp.solutions.drawing_utils
        self.mp_pose= mp.solutions.pose
        self.pose = self.mp_pose.Pose()

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
        landmarks_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                landmarks_list.append([id,lm.x,lm.y,lm.z])
                cv2.circle(img, (cx,cy),10, (0,0,255), cv2.FILLED)
        
        return landmarks_list

def main():
    cap = cv2.VideoCapture(0)
    detector = pose_detector()
    while True:
        ret, img = cap.read()
        lmList = detector.find_position(img)
        cv2.imshow("hello",detector.find_pose(img))
        print(lmList)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

if __name__ == "__main__":
    main()