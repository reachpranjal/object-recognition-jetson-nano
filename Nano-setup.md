1. To install Jetson Inference, Follow [This GitHub Link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

2. If there is `Segmentation Fault` Error which occurs due to inappropriate power management,<br />
Then Execeute `$ sudo ldconfig' after '$ sudo install make` command

3. To handle `ImportError: /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block`; <br />
Execute `$ export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1`

> If Micro-USB is used- Enter into 5W mode <br />
> `sudo nvpmodel -m 1`

## OpenCV Error
`CMake Error at CMakeLists.txt:66 (find_package): \
Could not find a configuration file for package "OpenCV" that is compatible \
with requested version "3.0.0". \
The following configuration files were considered but not accepted: \
/usr/local/lib/cmake/opencv4/OpenCVConfig.cmake, version: 4.0.0 \
-- Configuring incomplete, errors occurred! \
See also "/home/nano/jetson-inference/build/CMakeFiles/CMakeOutput.log". \
See also "/home/nano/jetson-inference/build/CMakeFiles/CMakeError.log".`

This is a build problem and hence needs manual change in CMaeLists.txt <br />
`$ cd jetson-inference &nbsp;
$ sudo nano tools/trt-console/CMakeLists.txt` <br />
Change OpenCV version from `3.0.0` to `4.0.0`
