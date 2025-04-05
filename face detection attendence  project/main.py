import cv2
import numpy as np
import face_recognition
import os
import datetime

IMAGES_PATH = "students_images"
images,names =[],[]
def load_known_faces():
    
    for file in os.listdir(IMAGES_PATH):
        img=cv2.imread(f"{IMAGES_PATH}/{file}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #we need to convert to rgb for face_recognition
        encoded_image=face_recognition.face_encodings(img)
        if len(encoded_image)==0:
            print("no face was detected ") 
        else:                                # If a face is found in the image
            images.append(encoded_image[0])
            names.append(os.path.splitext(file)[0])
    return images ,names
 


import cv2
def capture_student_face():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("cannot open camera please try again")
        return None
    captured_frame = None
    while True:
        ret ,frame=cap.read()
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF==  ord('q'):  #if q is clicked exit the camera window 
           captured_frame=frame    #returns the last fram captured before pressing q
           break
    cap.release()
    cv2.destroyAllWindows()
    return captured_frame





def register_new_students(frame):
    name=input("type your  name  :").strip()
    if not name:
        print("invalid name enter it again")
    new_file_path=f'{IMAGES_PATH}/{name}.jpg'
    cv2.imwrite(new_file_path,frame)
    new_img=face_recognition.load_image_file(new_file_path)
    new_encoded_image=face_recognition.face_encodings(new_img)[0]
    if len(new_encoded_image)==0:
        print("no face detected ")
    else:   
        images.append(new_encoded_image[0])
        names.append(name)
        print(f' {name}have been added to the system succesfully')
    return images , names  # Return the lists containing face encodings and names

    
def comparing_faces(captured_frame,images ,names):   #compare existing faces with the camera capture 
    frame_rgb = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB)
    captured_encoding = face_recognition.face_encodings(frame_rgb)
    if not captured_encoding:
        print(" No face detected. Try again.")
        return None
    captured_encoding = captured_encoding[0] 
    matchedfaces=face_recognition.compare_faces(images,captured_encoding)
    #face distance is a list of distances calculated in the face ex:[0.45, 0.32, 0.67]
    face_distances = face_recognition.face_distance(images, captured_encoding)#Getting Similarity Scores Between Faces
    if True in matchedfaces:   #matches=False, True, False, True]
       best_match_index = np.argmin(face_distances)  # Get the closest match
       recognized_name = names[best_match_index]
       print(f" Student recognized: {recognized_name}")
       return recognized_name
    else:
        print("please register first !!")

        return None
    if recognized_name:
        mark_attendance(recognized_name)

def mark_attendance(student_name):
    with open("attendance.csv", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{student_name},{timestamp}\n")
    print(f" Attendance marked for {student_name} at {timestamp}")

def process_student(captured_frame):
    recognized_name = comparing_faces(captured_frame, images, names)
    if recognized_name:
        mark_attendance(recognized_name)
    else:
        print(" Student not found. Do you want to register? (yes/no)")
        choice = input().strip().lower()
        if choice == "yes":
            register_new_students(captured_frame)

def main():
    print("\nloading student list .....")
    images,names=load_known_faces()
    print("\ncapturing image of the student ...")
    captured_frame=capture_student_face()
    if captured_frame is None:
        print("no image is captured ")
        return 
    print("\nProcessing student...")
    recognized_name=comparing_faces(captured_frame, images, names)
    if recognized_name:
        mark_attendance(recognized_name)
    else:
        print("student not found .do you wanna register ?")
        choice=input().strip().lower()
        if choice =="yes" :
            images,names=register_new_students(captured_frame)
        else:
            print("exiting without registation.")


if __name__ =="__main__":
    main()
