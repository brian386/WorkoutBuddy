from pose_detection import *

def count_bicep_curl(cur_session,detector,lmList):
    rsh_relb_rwr = detector.calc_angle(lmList['right_shoulder'], lmList['right_elbow'], lmList['right_wrist'])
        
    if cur_session['up'] and rsh_relb_rwr < 30:
        cur_session['reps'] += 0.5
        cur_session['up'] = False
    elif not cur_session['up'] and rsh_relb_rwr > 150: 
        cur_session['reps'] += 0.5
        cur_session['up'] = True;
#hi