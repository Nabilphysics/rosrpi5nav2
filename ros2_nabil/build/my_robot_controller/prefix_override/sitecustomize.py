import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/srhnabilacademy/ros2_nabil/install/my_robot_controller'
