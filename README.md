# RAMLAB_DATASET

> This package is used to store information of various datasets. Folders are arranged like this:
>
> ${Dataset_Name}
>
> |----calib (intrinsics and extrinsics)
>
> |--------cam00.yaml
>
> |--------cam01.yaml
>
> |--------...
>
> |--------camN.yaml
>
> |--------extrinsics.yaml
>
> |----cfg (config files for programs)
>
> |--------${Program_Name}.yaml
>
> |----figure (figure of the multi-sensor device, better contains the coordinate definition)

## Usage

1. CameraSystem.cpp: a camera system object to load camera intrinsics

   - ramlab/util_utils_sensor/src

   ```  c++
   #include "ramlab_sensor/CameraSystem.hpp"
   
   std::string calib_info_dir_ = "ramlab/ramlab_parameter/${Dataset_Name}/calib"
   int N_CAM_ = 2; // number of cameras 
   CameraSystem::Ptr cam_sys_ptr_;
   cam_sys_ptr_.reset(new CameraSystem(calib_info_dir_, N_CAM_, true));
   ```

2. SensorSystem.cpp: a sensor system object to load sensor extrinsics

   - ramlab/util_utils_sensor/src

   ```  c++
   #include "ramlab_sensor/SensorSystem.hpp"
   
   std::string calib_info_dir_ = "ramlab/ramlab_parameter/${Dataset_Name}/calib"
   int N_SENSOR_ = 4; // number of cameras + number of other sensors
   SensorSystem::Ptr sensor_sys_ptr_;
   sensor_sys_ptr_.reset(new SensorSystem(calib_info_dir_, N_SENSOR_, true));
   ```





