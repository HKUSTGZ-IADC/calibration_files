# Calibration Pipeline of 20230618\_calib

## Handheld Device
### Camera Intrinsic Calibration
1. [x] Intrinsics of frame_cam00: MATLAB monocular camera calibration toolbox
2. [x] Intrinsics of frame_cam01: MATLAB monocular camera calibration toolbox
3. [x] Intrinsics of event_cam00: MATLAB monocular camera calibration toolbox
4. [x] Intrinsics of event_cam01: MATLAB monocular camera calibration toolbox

### Camera-LiDAR Extrinsic Calibration
1. [ ] Extrinsics from ouster00 to frame_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)
2. [ ] Extrinsics from ouster00 to event_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)
3. [ ] Extrinsics from ouster00 to vehicle_frame_cam00: [LCECalib](https://github.com/HKUSTGZ-IADC/LCECalib)

### Others
1. [ ] Extrinsics from frame_cam00 to vehicle_frame_cam00

## NOTE:
1. The projection matrix is equal to the camera matrix for each camera since we provide the raw distorted images. For whom want to compute the correct **projection matrix** and **rectification matrix** with rectificed images, you can try ```stereoRectify(K1, D1, K2, D2, Size(width, height), R, T_vec, R1, R2, P1, P2, Q)```








