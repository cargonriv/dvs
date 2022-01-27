#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/src/geneus"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/install/lib/python3.9/site-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/install/lib/python3.9/site-packages:/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build/lib/python3.9/site-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build" \
    "/Users/gonz495/miniconda3/envs/ROSDVS/bin/python" \
    "/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/src/geneus/setup.py" \
    egg_info --egg-base /Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build/geneus \
    build --build-base "/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/build/geneus" \
    install \
    --root="${DESTDIR-/}" \
     --prefix="/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/install" --install-scripts="/Users/gonz495/Downloads/Interns/luigi/dvs/ros_catkin_ws/install/bin"
