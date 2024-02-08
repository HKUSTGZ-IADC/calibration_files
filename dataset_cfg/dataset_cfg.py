dataset_folder_release = '/Titan/dataset/FusionPortable_dataset/sensor_data'
dataset_folder_develop = '/Titan/dataset/FusionPortable_dataset_develop/sensor_data'

# sensor name
sensor_list = ['ouster00/point/data',
               'frame_cam00/image/data',
               'frame_cam01/image/data',
               'event_cam00/image/data',
               'event_cam01/image/data',
               'body_imu',
               'gps00',
               'gt']

# format: platform, sequence_name, date
plat_data_pair_list = [
    # handheld
    # ['handheld', 'garden_night', '20220215', 1.0],
    # ['handheld', 'canteen_night', '20220215', 1.0],
    # ['handheld', 'garden_day', '20220216', 1.0],
    # ['handheld', 'canteen_day', '20220216', 1.0],
    # ['handheld', 'corridor_day', '20220216', 1.0],
    # ['handheld', 'escalator_day', '20220216', 1.0],
    # ['handheld', 'building_day', '20220225', 1.0],
    # ['handheld', 'stair_day', '20220225', 1.0],
    # ['handheld', 'MCR_calibration', '20220216', 0.2],
    # ['handheld', 'MCR_slow', '20220216', 0.2],
    # ['handheld', 'MCR_normal', '20220216', 0.2],
    # ['handheld', 'MCR_fast', '20220216', 0.2],
    # ['handheld', 'lab_calibration', '20220424', 0.5],
    # ['handheld', 'lab_one_loop', '20220424', 0.5],
    # ['handheld', 'lab_two_loops', '20220424', 0.5],
    # quadrupedal_robot
    # ['quadrupedal_robot', 'MCR_slow_00', '20220219', 0.5],
    # ['quadrupedal_robot', 'MCR_slow_01', '20220219', 0.5],
    # ['quadrupedal_robot', 'MCR_normal_00', '20220219', 0.5],
    # ['quadrupedal_robot', 'MCR_normal_01', '20220219', 0.5],
    # ['quadrupedal_robot', 'MCR_fast_00', '20220219', 0.5],
    # ['quadrupedal_robot', 'MCR_fast_01', '20220219', 0.5],
    # ['quadrupedal_robot', 'lab_test', '20220718', 0.5],
    # apollo
    # ['apollo', 'campus_road_day', '20220226', 3.0],
    # sample data
    # ['handheld', 'canteen_day_sample', '20220216', 1.0],
    # ['quadrupedal_robot', 'MCR_slow_00_sample', '20220219', 0.2],
    # ['apollo', 'campus_road_day_sample', '20220226', 3.0]
    # mini_hercules
    # ['mini_hercules', 'hkustgz_calibration', '20221202', 1.0],
    # ['mini_hercules', 'hkustgz_campus_day', '20221202', 3.0]
    # ['mini_hercules', 'hkustgz_campus_road_day', '20230309', 3.0]
    # ['mini_hercules', 'hkustgz_campus_road_day_sequence00', '20230322', 3.0],
    # ['mini_hercules', 'hkustgz_campus_road_day_sequence01', '20230322', 3.0],
    # ['mini_hercules', 'hkustgz_campus_road_day_sequence02', '20230322', 3.0],
    # ['mini_hercules', 'hkustgz_campus_road_day_sequence03', '20230322', 3.0],
    # ['mini_hercules', 'hkustgz_campus_road_day_sequence04', '20230322', 3.0]
    ['mini_hercules', 'hkustgz_campus_road_day_sequence00', '20230403', 3.0],
    ['mini_hercules', 'hkustgz_campus_road_day_sequence01', '20230403', 3.0],
    ['mini_hercules', 'hkustgz_campus_road_day_sequence02', '20230403', 3.0],
    ['mini_hercules', 'hkustgz_campus_road_day_sequence03', '20230403', 3.0],
    ['mini_hercules', 'hkustgz_campus_road_day_sequence04', '20230403', 3.0],
    ['mini_hercules', 'hkustgz_campus_road_day_sequence05', '20230403', 3.0]
]

handheld_topic_list = [
    '/mocap_path',
    '/mocap_pose',
    '/fix',
    '/vel',
    '/time_reference',
    '/os_cloud_node/imu/data_raw',
    '/os_cloud_node/points',
    '/os_image_node/nearir_image',
    '/os_image_node/range_image',
    '/os_image_node/reflec_image',
    '/os_image_node/signal_image',
    '/stim300/imu/data_raw',
    '/stereo/frame_left/image_raw/compressed',
    '/stereo/frame_right/image_raw/compressed',
    '/stereo/frame_left/camera_info',
    '/stereo/frame_right/camera_info',
    '/stereo/vehicle_frame_left/camera_info',
    '/stereo/vehicle_frame_right/camera_info',
    '/stereo/davis_left/events',
    '/stereo/davis_left/image_raw/compressed',
    '/stereo/davis_left/imu/data_raw',
    '/stereo/davis_right/events',
    '/stereo/davis_right/image_raw/compressed',
    '/stereo/davis_right/imu/data_raw'
]

lidar_body_imu_topic_list = [
    '/mocap_path',
    '/mocap_pose',
    '/fix',
    '/vel',
    '/time_reference',
    '/os_cloud_node/imu/data_raw',
    '/os_cloud_node/points',
    '/os_image_node/nearir_image',
    '/os_image_node/range_image',
    '/os_image_node/reflec_image',
    '/os_image_node/signal_image',
    '/stim300/imu/data_raw'
]

stereoframe_body_imu_topic_list = [
    '/mocap_path',
    '/mocap_pose',
    '/fix',
    '/vel',
    '/time_reference',
    '/stereo/frame_left/image_raw',
    '/stereo/frame_right/image_raw',
    '/stim300/imu/data_raw'
]

stereoevent_body_imu_topic_list = [
    '/mocap_path',
    '/mocap_pose',
    '/fix',
    '/vel',
    '/time_reference',
    '/stereo/davis_left/events',
    '/stereo/davis_left/image_raw',
    '/stereo/davis_left/imu/data_raw',
    '/stereo/davis_right/events',
    '/stereo/davis_right/image_raw',
    '/stereo/davis_right/imu/data_raw',
    '/stim300/imu/data_raw'
]

prcv2022_topic_list = [
    '/fix',
    '/vel',
    '/time_reference',
    '/stereo/davis_left/events',
    '/stereo/davis_left/image_raw',
    '/stereo/davis_left/imu/data_raw',
    '/stereo/davis_right/events',
    '/stereo/davis_right/image_raw',
    '/stereo/davis_right/imu/data_raw',
    '/stereo/frame_left/image_raw',
    '/stereo/frame_right/image_raw',
    '/stim300/imu/data_raw'
]

_3dm_topic_list = [
    '/3dm_ins/gnss_left/aiding_status',
    '/3dm_ins/gnss_left/fix',
    '/3dm_ins/gnss_left/fix_info',
    '/3dm_ins/gnss_left/odom',
    '/3dm_ins/gnss_left/time_ref',
    '/3dm_ins/gnss_right/aiding_status',
    '/3dm_ins/gnss_right/fix',
    '/3dm_ins/gnss_right/fix_info',
    '/3dm_ins/gnss_right/odom',
    '/3dm_ins/gnss_right/time_ref',
    '/3dm_ins/gps_corr',
    '/3dm_ins/imu/data_raw',
    '/3dm_ins/mag/data_raw',
    '/3dm_ins/nav/aiding_summary',
    '/3dm_ins/nav/dual_antenna_status',
    '/3dm_ins/nav/filtered_imu/data',
    '/3dm_ins/nav/heading',
    '/3dm_ins/nav/odom',
    '/3dm_ins/nav/status'
]

mini_hercules_topic_list = [
    '/can_port/bcm_feedback',
    '/can_port/bms_feedback',
    '/can_port/brake_feedback',
    '/can_port/bumper_feedback',
    '/can_port/epb_feedback',
    '/can_port/joy_feedback',
    '/can_port/motor_feedback',
    '/can_port/odometer_feedback',
    '/can_port/sonar_feedback',
    '/can_port/steer_feedback',
    '/can_port/tire_status_feedback',
    '/can_port/unified_error_codes',
    '/can_port/vcu_feedback',
    '/lower_control/vehicle_control',
    '/top/rslidar_points',
    '/left/rslidar_points',
    '/livox/lidar',
    '/right/rslidar_points',
    '/rion/yaw_data',
    '/mini_hercules/encoder_left',
    '/mini_hercules/encoder_right'
]

unitree_topic_list = [
    '/unitree/imu/data_raw', 
    '/unitree/odom', 
    '/unitree/joint_state'
]

# Topics in a Rosbag
#   /mocap_path                         6088 msgs    : nav_msgs/Path
#   /mocap_pose                         6088 msgs    : geometry_msgs/PoseStamped
#   /os_cloud_node/imu/data_raw         30799 msgs    : sensor_msgs/Imu
#   /os_cloud_node/points                3080 msgs    : sensor_msgs/PointCloud2
#   /os_image_node/nearir_image          3081 msgs    : sensor_msgs/Image
#   /os_image_node/range_image           3081 msgs    : sensor_msgs/Image
#   /os_image_node/reflec_image          3081 msgs    : sensor_msgs/Image
#   /os_image_node/signal_image          3081 msgs    : sensor_msgs/Image
#   /stereo/davis_left/events          302865 msgs    : dvs_msgs/EventArray
#   /stereo/davis_left/image_raw         6293 msgs    : sensor_msgs/Image
#   /stereo/davis_left/imu/data_raw    307188 msgs    : sensor_msgs/Imu
#   /stereo/davis_right/events         306416 msgs    : dvs_msgs/EventArray
#   /stereo/davis_right/image_raw        6370 msgs    : sensor_msgs/Image
#   /stereo/davis_right/imu/data_raw   307866 msgs    : sensor_msgs/Imu
#   /stereo/frame_left/image_raw         6160 msgs    : sensor_msgs/Image
#   /stereo/frame_right/image_raw        6160 msgs    : sensor_msgs/Image
#   /stim300/imu/data_raw               61580 msgs    : sensor_msgs/Imu
#   /fix
#   /vel
#   /time_reference                              99473 msgs: sensor_msgs/TimeReference
# 3dm
#   /3dm_ins/gnss1/aiding_status                 68852 msgs: microstrain_inertial_msgs/GNSSAidingStatus
#   /3dm_ins/gnss1/fix                           14364 msgs: sensor_msgs/NavSatFix
#   /3dm_ins/gnss1/fix_info                      14364 msgs: microstrain_inertial_msgs/GNSSFixInfo
#   /3dm_ins/gnss1/odom                          14364 msgs: nav_msgs/Odometry
#   /3dm_ins/gnss1/time_ref                      14364 msgs: sensor_msgs/TimeReference
#   /3dm_ins/gnss2/aiding_status                 68852 msgs: microstrain_inertial_msgs/GNSSAidingStatus
#   /3dm_ins/gnss2/fix                           14363 msgs: sensor_msgs/NavSatFix
#   /3dm_ins/gnss2/fix_info                      14363 msgs: microstrain_inertial_msgs/GNSSFixInfo
#   /3dm_ins/gnss2/odom                          14363 msgs: nav_msgs/Odometry
#   /3dm_ins/gnss2/time_ref                      14363 msgs: sensor_msgs/TimeReference
#   /3dm_ins/gps_corr                          1737493 msgs: microstrain_inertial_msgs/GPSCorrelationTimestampStamped
#   /3dm_ins/imu/data                          1737495 msgs: sensor_msgs/Imu
#   /3dm_ins/mag                               1737495 msgs: sensor_msgs/MagneticField
#   /3dm_ins/nav/aiding_summary                  68828 msgs: microstrain_inertial_msgs/FilterAidingMeasurementSummary
#   /3dm_ins/nav/dual_antenna_status             68850 msgs: microstrain_inertial_msgs/GNSSDualAntennaStatus
#   /3dm_ins/nav/filtered_imu/data               68850 msgs: sensor_msgs/Imu
#   /3dm_ins/nav/heading                         68850 msgs: microstrain_inertial_msgs/FilterHeading
#   /3dm_ins/nav/odom                            78761 msgs: nav_msgs/Odometry
#   /3dm_ins/nav/status                          68846 msgs: microstrain_inertial_msgs/FilterStatus
# mini hercules
#   /can_port/bcm_feedback                      100023 msgs: sei_msgs/BcmFeedback
#   /can_port/bms_feedback                       99955 msgs: sei_msgs/BmsFeedback
#   /can_port/brake_feedback                    498085 msgs: sei_msgs/BrakeFeedback
#   /can_port/bumper_feedback                   498142 msgs: sei_msgs/BumperFeedback
#   /can_port/epb_feedback                      498085 msgs: sei_msgs/EpbFeedback
#   /can_port/joy_feedback                       99989 msgs: sei_msgs/JoyFeedback
#   /can_port/motor_feedback                    497945 msgs: sei_msgs/MotorFeedback
#   /can_port/odometer_feedback                  10006 msgs: sei_msgs/OdometerFeedback
#   /can_port/sonar_feedback                     98938 msgs: sys_eng_msgs/SonarFeedback
#   /can_port/steer_feedback                    498012 msgs: sei_msgs/SteerFeedback
#   /can_port/tire_status_feedback               20012 msgs: sei_msgs/TireStatusFeedback
#   /can_port/unified_error_codes               995498 msgs: sys_eng_msgs/UnifiedErrorCodes
#   /can_port/vcu_feedback                       99988 msgs: sei_msgs/VcuFeedback
#   /lower_control/vehicle_control              995412 msgs: sei_msgs/VehicleControl
#   /top/rslidar_points                          96113 msgs: sensor_msgs/PointCloud2
#   /left/rslidar_points                         27763 msgs: sensor_msgs/PointCloud2
#   /livox/lidar                                 99753 msgs: sensor_msgs/PointCloud2
#   /right/rslidar_points                        23978 msgs: sensor_msgs/PointCloud2
#   /rion/yaw_data                              994039 msgs: sensor_msgs/Imu
