## Calibration Pipeline of 20230309\_calib

### Calibration data 1
1. [x] Intrinsics of frame_cam00: MATLAB monocular camera calibration toolbox
2. [x] Intrinsics of frame_cam01: MATLAB monocular camera calibration toolbox
3. [x] Extrinsics from ouster00 to frame_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)
4. [x] Extrinsics from ouster00 to frame_cam01: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)
5. [x] Extrinsics from frame_cam00 to frame_cam01
* NOTE: we cannot use the MATLAB stereo camera calibration toolbox since they do not have an overlapping FOV
* NOTE: we get T^framecam01_framecam00 = T^framecam01_lidar * T^lidar_framecam00

### Calibration data 2
5. [x] Extrinsics from body_imu to frame_cam00: [Kalibr](https://github.com/ethz-asl/kalibr)
6. [x] Extrinsics from body_imu to osimu: [Kalibr](https://github.com/ethz-asl/kalibr)

### Calibration data 3
6. [x] Extrinsics from body_imu to frame_cam01: [Kalibr](https://github.com/ethz-asl/kalibr)
* NOTE: we only record the calibrated timeshift and discard the calibrated but wrong transformation
* NOTE: we get T^Framecam01_body_imu = T^framecam01_framecam00 * T^framecam00_body_imu
