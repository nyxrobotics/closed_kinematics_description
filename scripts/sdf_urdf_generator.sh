# Generate .urdf from .xacro
echo "generate urdf to ./../xacro/export/"
rosrun xacro xacro --inorder -o ./../xacro/export/02_open_chain_and_dummy_link.urdf "./../xacro/02_open_chain_and_dummy_link.xacro" 
echo "generate sdf to ./../xacro/export/"
gz sdf -p ./../xacro/export/02_open_chain_and_dummy_link.urdf > ./../xacro/export/02_open_chain_and_dummy_link.sdf
echo "close sdf to ./../xacro/export/"
python sdf_close.py