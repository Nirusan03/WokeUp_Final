from flask import Flask, render_template, Response, request, url_for, redirect
from pymongo import *
from itertools import groupby
from datetime import date, timedelta
import datetime
import cv2
import smtplib

from cvzone.PoseModule import PoseDetector

app = Flask(__name__)

cluster = MongoClient("mongodb://localhost:27017")

user_db = cluster["Users"]
user_account = user_db["Account"]
user_name = ""


# The function to detect the motions and frames
def generate_frames():
    # Object to detect the poses in each frames
    detector = PoseDetector()

    # Capturing the video frames from the camera
    cap = cv2.VideoCapture(0)

    # Detect the falls count
    count = 0

    # Endless loop to detect the human
    while True:

        # Reading each frames of the detected person
        success, img = cap.read()

        # Drawing the landmark on the frames
        img = detector.findPose(img)

        # Detecting the human and drawing the criteria on human
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=True)

        # Check if the user is standing
        if lmList:
            # Get the coordinates of specific body parts
            shoulder = lmList[12]  # Left shoulder
            hip = lmList[11]  # Left hip
            head = lmList[15]  # Top of the head

            # Calculate the vertical distance between shoulder and hip
            vertical_distance = abs(shoulder[1] - hip[1])

            # # Check if the user is standing
            # if vertical_distance > 0.3 * abs(shoulder[1] - head[1]):
            #     print("")

            # Check if the user is laying vertically on a surface
            if vertical_distance < 0.05 * abs(shoulder[1] - head[1]):
                count += 1
                print("User is laying vertically ", count)
                if count >= 150:
                    import smtplib

                    # SMTP server configuration
                    smtp_server = 'smtp.gmail.com'
                    smtp_port = 587

                    # Sender's credentials
                    sender_email = 'nirusan3.hariharan@gmail.com'
                    sender_password = 'IIT#123#123'

                    # Recipient's email
                    recipient_email = 'nirusan.hariharan350@gmail.com'

                    # Email content
                    subject = 'Patient Felt'
                    message = 'Hello, the patient has reported feeling unwell.'

                    try:
                        # Create an SMTP object
                        server = smtplib.SMTP(smtp_server, smtp_port)

                        # Establish a secure connection
                        server.starttls()

                        # Login to the sender's email account
                        server.login(sender_email, sender_password)

                        # Send the email
                        server.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{message}')

                        print('Email sent successfully!')

                    except smtplib.SMTPAuthenticationError:
                        print('Authentication error. Please check your username and password.')

                    except smtplib.SMTPException as e:
                        print(f'An error occurred while sending the email: {str(e)}')

                    finally:
                        # Close the connection to the SMTP server
                        server.quit()

        # Processing the image frames as encoded JPEG
        ret, buffer = cv2.imencode('.jpg', img)

        # Converting JPEG images into bytes
        frame = buffer.tobytes()

        # Yielding to stream the video on web page
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


@app.route('/')
def signup1():
    return render_template('signup1.html')


@app.route('/signup2')
def signup2():
    return render_template('signup2.html')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/admin_home')
def admin_home():
    return render_template('admin.html')


# Creating collection
@app.route('/create_collection', methods=['POST'])
def create_collection():
    global user_name, user_account

    # Get the form data
    user_name = request.form['user_name']
    contact_no = request.form['contact_no']
    address = request.form['address']
    email = request.form['email']
    password = request.form['password']

    # collection creating
    for i in range(1):
        collection_name = f"{user_name}"

        # Calling the create_cluster_vendor method
        user_collection_create(collection_name, contact_no, address,
                               email, password)

    # Returning signup_vendor2 method
    return redirect(url_for('signup2'))


def user_collection_create(collection_name, contact_no, address, email, password):
    global user_name, user_account, user_db

    # Create the new collection
    user_db.create_collection(collection_name)
    temp_collection = user_db[collection_name]

    post = {
        "Name": collection_name,
        "Address": address,
        "Contact_No": contact_no,
        "Email": email,
        "Password": password,
    }
    user_account.insert_one(post)


@app.route('/signup2_insert', methods=['POST'])
def signup2_insert():
    global user_account, user_name, user_db

    # Get the form data
    user_name = request.form['user_name']
    gender = request.form['gender']
    age = request.form['age']
    address = request.form['address']
    bloody_type = request.form['bloody_type']
    allergies = request.form['allergies']
    issues = request.form['issues']

    # Storing the data inside the dictionary
    post = {
        "Parent_name": user_name,
        "Gender": gender,
        "Age": age,
        "Address": address,
        "Bloody_type": bloody_type,
        "Allergies": allergies,
        "Issues": issues
    }

    user_account.update_one({"Name": user_name}, {"$set": post}, upsert=True)

    return redirect(url_for('home'))


@app.route('/signup3_insert', methods=['POST'])
def signup3_insert():
    global user_account, user_name, user_db

    # Get the form data
    ver_number = request.form['ver_number']

    # # Storing the data inside the dictionary
    # post = {
    #     "Parent_name": user_name,
    #     "Gender": gender,
    #     "Age": age,
    #     "Address": address,
    #     "Bloody_type": bloody_type,
    #     "Allergies": allergies,
    #     "Issues": issues
    # }

    # user_account.update_one({"Name": user_name}, {"$set": post}, upsert=True)

    return redirect(url_for('home'))


@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/stream')
def stream():
    return render_template('stream.html')


@app.route('/login', methods=['POST'])
def login_vendor():
    global user_name, user_db

    # Get the vendor_name and password from the form
    name = request.form['name']

    # Check if the collection is available in the database
    if name in user_db.list_collection_names():
        user_name = user_name
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_page'))


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
