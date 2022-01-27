execute_process(COMMAND "/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build/gennodejs/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build/gennodejs/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
