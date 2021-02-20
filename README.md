## Object detection 

- To run object detection in jetson nano:
```bash
$ git clone https://github.com/reachpranjal/object-recognition-jetson-nano
$ cd object-recognition-jetson-nano
$ python3 object_detection.py
```
## Object Recognition

- To run object recognition in jetson nano:
```bash
$ python3 object_recognition.py
```

## Install Object detection prebuilt models

To install Jetson Inference, Follow [This GitHub Link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

## Fix to possible errors

1. If there is `Segmentation Fault` Error which occurs due to inappropriate power management, \
```bash
$ sudo install make
$ sudo ldconfig
```

2. To handle `ImportError: /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block`; \
```bash
$ export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
```

3. OpenCV Error
```bash
CMake Error at CMakeLists.txt:66 (find_package): 
Could not find a configuration file for package "OpenCV" that is compatible
with requested version "3.0.0". `<br />
The following configuration files were considered but not accepted:  
/usr/local/lib/cmake/opencv4/OpenCVConfig.cmake, version: 4.0.0  
-- Configuring incomplete, errors occurred! 
See also "/home/nano/jetson-inference/build/CMakeFiles/CMakeOutput.log"  
See also "/home/nano/jetson-inference/build/CMakeFiles/CMakeError.log"
```
-This is a build problem and hence needs manual change in `CMaeLists.txt`
```bash
$ cd jetson-inference
$ sudo nano tools/trt-console/CMakeLists.txt
```
Search for OpenCV version and change from `3.0.0` to `4.0.0`
