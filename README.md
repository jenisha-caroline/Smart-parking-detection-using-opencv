# Smart-parking-detection-using-opencv

SMART PARKING DETECTION USING OPENCV

OVERVIEW:

This project utilizes YOLO (You Only Look Once) and OpenCV to detect and monitor parking spaces in real-time. It helps optimize parking lot management by identifying vacant and occupied spots with high accuracy.

FEATURES:

Real-time Parking Detection* using YOLOv4/YOLOv8
OpenCV for Image Processing*
Bounding Boxes & Object Detection* for parked cars
Customizable Parking Zone Mapping*
Supports Live Camera Feeds & Video Input*

INSTALLATION:

Clone the Repository
git clone https://github.com/prajesdas/Smart-Parking-Space-Detector-using-YOLO-and-OpenCV.git
cd Smart-Parking-Space-Detector-using-YOLO-and-OpenCV
2.Install Dependencies

pip install -r requirements.txt
3.Download YOLO Weights

Download YOLOv4 weights from official YOLO website or use a pre-trained YOLOv8 model.
Place the weights in the models/ directory.
4.Run the Detection Script

python detect_parking.py --source video.mp4
or for live webcam feed:

python detect_parking.py --source 0
PROJECT STRUCTURE

 SMART PARKING DETECTOR:
 ┣  models/              # YOLO model weights  
 ┣  data/                # Parking lot images/videos  
 ┣  utils/               # Helper functions  
 ┣  detect_parking.py    # Main script for detection  
 ┣  requirements.txt     # Dependencies  
 ┣  README.md            # Project documentation  
FUTURE ENHANCEMENTS Integration with a mobile app for user-friendly access Adding a cloud database to store parking statistics
Implementing number plate recognition for security

CONTRIBUTING:

Pull requests are welcome! If you'd like to contribute, please open an issue first to discuss your ideas.

LICENCE:

This project is MIT Licensed. Feel free to use and modify it.
