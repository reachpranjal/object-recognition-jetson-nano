* To install Jetson Inference, Follow [This GitHub Link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

* If there is `Segmentation Fault` Error which occurs due to inappropriate power management,
Then Execeute `$ sudo ldconfig' after '$ sudo install make` command

* To handle `ImportError: /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block`; 
Execute `$ export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1`

If Micro-USB is used- Enter into 5W mode
`sudo nvpmodel -m 1`
