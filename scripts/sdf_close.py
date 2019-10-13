#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import string
import re

in_file  = codecs.open('./../xacro/export/02_open_chain_and_dummy_link.sdf', 'r', 'utf-8')
out_file = codecs.open('./../xacro/export/03_closed_chain.sdf', 'w', 'utf-8')

all_text = in_file.read()
out_text = re.sub(r"""
    <link name='dummy(.)_connection_(.+)'>
      <pose frame=''>(.+)</pose>
      <inertial>
        <pose frame=''>(.+)</pose>
        <mass(.+)</mass>
        <inertia>
          <ixx>(.+)</ixx>
          <ixy>(.+)</ixy>
          <ixz>(.+)</ixz>
          <iyy>(.+)</iyy>
          <iyz>(.+)</iyz>
          <izz>(.+)</izz>
        </inertia>
      </inertial>
    </link>
    <joint name='(.+)' type='revolute'>
      <child>dummy(.)_connection_(.+)</child>
      <parent>(.+)</parent>
      <axis>
        <xyz>(.+)</xyz>
        <limit>
          <lower>(.+)</lower>
          <upper>(.+)</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
        <use_parent_model_frame>1</use_parent_model_frame>
      </axis>
    </joint>
    <link name='dummy(.)_origin_(.+)'>
      <pose frame=''>(.+)</pose>
      <inertial>
        <pose frame=''>(.+)</pose>
        <mass>(.+)</mass>
        <inertia>
          <ixx>(.+)</ixx>
          <ixy>(.+)</ixy>
          <ixz>(.+)</ixz>
          <iyy>(.+)</iyy>
          <iyz>(.+)</iyz>
          <izz>(.+)</izz>
        </inertia>
      </inertial>
    </link>
    <joint name='(.+)' type='revolute'>
      <child>dummy(.)_origin_(.+)</child>
      <parent>dummy(.)_connection_(.+)</parent>
      <axis>
        <xyz>(.+)</xyz>
        <limit>
          <lower>(.+)</lower>
          <upper>(.+)</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
        <use_parent_model_frame>1</use_parent_model_frame>
      </axis>
    </joint>
""",r"""
    <joint name='\12' type='revolute'>
      <pose>\3</pose>
      <child>\14</child>
      <parent>\15</parent>
      <axis>
        <xyz>\16</xyz>
        <limit>
          <lower>\17</lower>
          <upper>\18</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
        <use_parent_model_frame>1</use_parent_model_frame>
      </axis>
    </joint>
""", all_text)
out_file.write(out_text)
in_file.close()
out_file.close()