import face_recognition
import cv2
import numpy as np
import os
from .models import Presence
from datetime import datetime
from personnels.models import Personnel
import pyautogui
import win32com.client as comclt

from test7.settings import MEDIA_ROOT




def prepare_path(base,url_inv):
    ch=''
    for i in url_inv:
        if(i=='/'):
            ch=ch+'\\'
        else:
            ch=ch+i
    ch1=os.path.join(base,ch)
    return ch1

def f_recognition(personnels):
    known_face_encodings=[]
    known_face_names = []
    known_face_cins =[]
    for c in personnels:
        ch1=prepare_path(MEDIA_ROOT,str(c.img))
        image = face_recognition.load_image_file(ch1)
        image_face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings = known_face_encodings +[image_face_encoding]
        known_face_names = known_face_names +[c.nom]
        known_face_cins =known_face_cins +[c.cin]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    cin = known_face_cins[best_match_index]
                    date_entree=datetime.now().strftime('%Y-%m-%d')
                    heure_entree=datetime.now().strftime('%H:%M-%S')
                    nb_heures=20-int(datetime.now().strftime('%H'))
                    
                    #ajout presence ..
                    try:
                        presence =Presence()
                        presence.cin=Personnel(cin)
                        presence.date_entree=date_entree
                        presence.heure_entree=heure_entree
                        presence.nb_heures=nb_heures
                        try:
                            presence.save()
                            print('ajout presence terminee..')
                        except:
                            print("presence existe..")
                    except:
                        print(personnel.cin)
                        print("probleme d'ajout presence!!")
                face_names.append(name)        
                print(name)
                
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()



def f_recognitionOff():
   print('test\n')
