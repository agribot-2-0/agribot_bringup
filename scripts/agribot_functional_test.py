#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String


def node():
    rospy.init_node('agribot_functional_test')
    task_publisher = rospy.Publisher('/agribot/state_machine/task',
                                     String,
                                     queue_size=1)
    rospy.wait_for_message('/agribot/state_machine/state', String)
    if not rospy.has_param('task_name'):
        ## set tag to "failed"
        return

    ## wait for system is ready

    ## send task
    actual_task_msg = String()
    actual_task_msg.data = rospy.get_param('task_name')
    task_publisher.publish(actual_task_msg)


if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass