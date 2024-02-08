# Calibration Pipeline of 20230425\_calib

## Handheld Device
### Multi-IMU Calibration
1. [x] Intrinsics of Ouster IMU: Allen deviation
2. [x] Intrinsics of Davis left IMU: Allen deviation
3. [x] Intrinsics of Davis right IMU: Allen deviation
4. [x] Intrinsics of STIM300 IMU: Allen deviation
5. [x] Intrinsics of 3DM IMU: Allen deviation
6. [x] Extrinsics of STIM300 IMU - 3DM IMU, Davis left IMU, Davis right IMU, Ouster IMU: Kalibr

### Camera Intrinsic Calibration
1. [x] Intrinsics of frame_cam00: MATLAB monocular camera calibration toolbox
2. [x] Intrinsics of frame_cam01: MATLAB monocular camera calibration toolbox
3. [x] Intrinsics of event_cam00: MATLAB monocular camera calibration toolbox
4. [x] Intrinsics of event_cam01: MATLAB monocular camera calibration toolbox

### IMU-Camera Extrinsic Calibration
1. [x] Extrinsics from body_imu to frame_cam00: [Kalibr](https://github.com/ethz-asl/kalibr)
2. [x] Extrinsics from body_imu to event_cam00: [Kalibr](https://github.com/ethz-asl/kalibr)
3. [x] Extrinsics from event_cam00_imu to event_cam00: [Kalibr](https://github.com/ethz-asl/kalibr)
4. [x] Extrinsics from event_cam01_imu to event_cam01: [Kalibr](https://github.com/ethz-asl/kalibr)
5. [x] Extrinsics from 3dm_imu to frame_cam00: [Kalibr](https://github.com/ethz-asl/kalibr)

### Camera-LiDAR Extrinsic Calibration
1. [x] Extrinsics from ouster00 to frame_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)
2. [x] Extrinsics from ouster00 to event_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)

## Leica MS60
### IMU-Leica Marker Extrinsic Calibration
1. [x] Extrinsics from body_imu to leica_marker: Hand-eye calibration

## Unitree
### IMU-Unitree IMU Extrinsic Calibration
1. [ ] Extrinsics from body_imu to unitree_body_imu: [Kalibr](https://github.com/ethz-asl/kalibr)

## Mini-Hercules
### IMU-Mini Hercules Wheel Extrinsic Calibration
1. [ ] Extrinsics from body_imu to mini_hercules_wheel: Manually measure

## Vehicle
### IMU-Vehicle Camera Extrinsic Calibration
1. [ ] Intrinsics of vehicle_frame_cam00:
2. [ ] Intrinsics of vehicle_frame_cam01:
3. [ ] Extrinsics of body_imu to frame_cam00: ICP

## NOTE:
1. The projection matrix is equal to the camera matrix for each camera since we provide the raw distorted images. For whom want to compute the correct **projection matrix** and **rectification matrix** with rectificed images, you can try ```stereoRectify(K1, D1, K2, D2, Size(width, height), R, T_vec, R1, R2, P1, P2, Q)```








