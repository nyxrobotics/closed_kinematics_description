pegasus_gazebo_plugins  
====
  
pegasus_gazebo_plugins: https://github.com/wojiaojiao/pegasus_gazebo_plugins  
  
#### 概要  
- pegasus_gazebo_pluginsを使って閉じたループの機構を再現する検証を行います   

>  rosrun xacro xacro --inorder -o export/04_pegasus.urdf 04_pegasus.xacro
>  gz sdf --version=1.6 -p export/04_pegasus.urdf > export/04_pegasus.sdf

#### 結論
- pegasus_gazebo_pluginsは使えない → https://github.com/wojiaojiao/pegasus_gazebo_plugins/issues/7
- 代案：https://github.com/2b-t/closed_loop → 完璧だった


