🚀 Mark-Me – Smart Attendance Portal
📌 Overview

Mark-Me is a modern attendance management application built using React Native for cross-platform mobile experience and HTML/CSS for web interface components.

The application helps teachers and institutions manage attendance digitally while allowing students to track their attendance records in real-time.

🎯 Objective

Traditional attendance systems are:

Manual and time-consuming

Error-prone

Hard to maintain

Mark-Me digitizes attendance tracking, improving efficiency, transparency, and accessibility.






# Run the container
docker run -p 3000:3000 my-app
The containerized application can be deployed to any platform that supports Docker, including:

AWS ECS
Google Cloud Run
Azure Container Apps
Digital Ocean App Platform
Fly.io
Railway
DIY Deployment
If you're familiar with deploying Node applications, the built-in app server is production-ready.

Make sure to deploy the output of npm run build

├── package.json
├── package-lock.json (or pnpm-lock.yaml, or bun.lockb)
├── build/
│   ├── client/    # Static assets
│   └── server/    # Server-side code
Styling
This template comes with Tailwind CSS already configured for a simple default starting experience. You can use whatever CSS framework you prefer.





Available Scripts
In the project directory, you can run:


npm test
Launches the test runner in the interactive watch mode.
See the section about running tests for more information.

npm run build
Builds the app for production to the build folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.
Your app is ready to be deployed!

See the section about deployment for more information.

npm run eject
Note: this is a one-way operation. Once you eject, you can't go back!

If you aren't satisfied with the build tool and configuration choices, you can eject at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except eject will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use eject. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

Learn More
You can learn more in the Create React App documentation.

To learn React, check out the React documentation.

Code Splitting
This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

Analyzing the Bundle Size
This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

Making a Progressive Web App
This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

Advanced Configuration
This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

Deployment
This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

npm run build fails to minify
This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify


Features
Real-time camera feed using PiCamera2.
Flask backend serving the stream.
Browser access at /video_feed.
Adjustable resolution and format.
Lightweight, ~0ms latency on local network.
Requirements
Raspberry Pi (with 64-bit OS recommended).

Raspberry Pi Camera Module enabled (raspi-config).

Python 3.9+

Dependencies:

pip install flask opencv-python picamera2
Usage
Clone the repository:

git clone https://github.com/yourusername/pi-camera-stream.git
cd pi-camera-stream
Run the app:

python app.py
Open browser and visit:

http://<raspberry-pi-ip>:5000
Project Structure
pi-camera-stream/
│── app.py          # Flask server with PiCamera2 video stream
│── templates/
│     └── index.html  # Basic UI to display the video feed
│── README.md
Endpoints
/ → Webpage with video feed
/video_feed → Raw MJPEG stream
Configuration
Default resolution: 640x480

Format: RGB888

To change resolution, edit in app.py:

config = picam2.create_video_configuration(main={"format": "RGB888", "size": (1280, 720)})
Notes
Use wired LAN or local WiFi for lowest latency.
Works best in Chrome/Edge/Firefox.
Add ngrok / reverse proxy if you want to view feed remotely.
Future Enhancements
Add motion detection (OpenCV).
Record and save stream to file.
Add authentication for /video_feed.
Python Script Description
The script does the following:

Initializes PiCamera2 and configures resolution/format.
Starts the camera and continuously captures frames.
Encodes each frame as JPEG.
Streams frames over Flask using multipart/x-mixed-replace.
Provides / endpoint for the UI and /video_feed endpoint for direct MJPEG stream.

