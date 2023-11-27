import numpy as np
import os
import face_recognition  # Fix the typo here
import cv2
import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date


def app():

    run = st.checkbox('Mark Attendance')
    FRAME_WINDOW = st.image([])
    path = 'images'
    images = []
    personName = []
    myList = os.listdir(path)
    # print(myList)

    for cu_img in myList:
        current_img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_img)
        personName.append(os.path.splitext(cu_img)[0])

    # print(personName)

    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):

        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            # print(myDataList)
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                tString = now.strftime('%H:%M:%S')
                today = date.today()
                dtString = today.strftime("%d/%m/%Y")
                f.writelines(f'\n{name},{tString},{dtString}')



    encodeListKnown = faceEncodings(images)
    print("All Encodings Completed!!")

    # If using external Camera then use 1  otherwise if using laptop camera use 0
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while run:
        ret, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personName[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                markAttendance(name)

        FRAME_WINDOW.image(frame)

    else:
        st.write('Stopped')
        # df = pd.read_csv('../Attendance.csv')
        # st.write(df)




