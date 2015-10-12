#!/usr/bin/env python
import tf.transformations

#angles = [-1.798, 1.117, -3.142] #link_hand to link_finger_1
angles = [-1.516, 1.146, 0.240] #link_hand to link_finger_2
#angles = [-1.622, 1.117, -0.236] #link_hand to link_finger_3

M_PI = 3.14159265358979
matrix = tf.transformations.euler_matrix(angles[0], angles[1], angles[2], axes='sxyz')
rxyz_angles = tf.transformations.euler_from_matrix(matrix, axes='rxyz')
print '<rotation> ', rxyz_angles[0]*180/M_PI , 'x </rotation>'
print '<rotation> ', rxyz_angles[1]*180/M_PI , 'y </rotation>'
print '<rotation> ', rxyz_angles[2]*180/M_PI , 'z </rotation>'


