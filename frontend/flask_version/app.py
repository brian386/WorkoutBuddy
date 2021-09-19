from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import math
import os
from pose_detection import *
from exercises import *


app=Flask(__name__)

if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def generate_frames():
    detector = pose_detector()
    cur_session = {'reps': 0, 'up': True}
    while True:

        success, frame_0 = camera.read()
        if success == True:
            frame_0 = detector.find_pose(frame_0)


            lmList = detector.find_position(frame_0)
            if len(lmList) != 0:
                # print(lmList['right_pinky'], lmList['right_wrist'], lmList['right_thumb'])
                count_bicep_curl(cur_session, detector, lmList)

                print(math.floor(cur_session['reps']))
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame_0, (0,375),(150,500), (0,0,0), -1)
            cv2.putText(frame_0, '{}'.format(math.floor(cur_session['reps'])), (10, 450), font, 3, (255, 255, 255), 2, cv2.LINE_AA)
            success,buffer = cv2.imencode('.jpg', frame_0)
            frame = buffer.tobytes()
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




        else:
            print("didn't work")
            break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(debug=True)
    print("Donezo")
    camera.release()
    print("washington")
    cv2.destroyAllWindows()