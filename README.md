closed_kinematics_description  
====
  
Gazeboでループの閉じたリンクを再現する手順を記載します  
  
## 概要  
  
#### 用語  
あくまでここでの表記で、一般的なものではない可能性があります。学会・論文誌等で定義されているものがあれば指摘して頂けるとありがたいです。  
- __基準ジョイント__:mimicジョイントが参照しているジョイント  
- __従属ジョイント__:mimicタグを持つジョイント  
- __閉ループリンク機構__:4節リンク・パラレルリンク機構などの、ループ形状を含む関節配置のリンク機構。英語でclosed kinematic chainsと表記されているみたいなので、こう表記している。feedback制御と紛らわしいので表現を変えたい。  
  
#### 手準  
  
- (1) rviz用に、閉ループのないxacroファイルを作成する  
- (2) gazebo用に、後の作業でループを閉じるための書式に合わせてxacroファイルを作成する  
- (3) (2)で作成したファイルをsdfに変換する  
- (4) sdfファイルを編集し、ループを閉じる  
  
#### 原因・背景
これら作業が必要になる原因が以下  

- xacro, urdfはループを閉じることができない  
    - rosのurdf→sdfパーサの挙動として、urdfからモデルを読み込む際に「親リンク→ジョイント→子リンク」の順で解決していく仕組みになっており、ループを閉じる構造があると無限ループに入ってしまう  
    - ジョイントのspring成分は本来sdfで設定できるが、urdf→sdfパーサにその機能がなく、関節のバネ成分は問答無用で0にされてしまう  
- gazeboの物理シミュレータはsdfを使用する  
    - 内部で必ずsdfに変換してから読み込んでいる  
    - リンクの質量・慣性モーメント・粘性・弾性・摩擦、ジョイントの粘性・弾性・摩擦はsdfから読み込まれる  
    - ただしモータやセンサなど、gazeboのプラグインとして機能が実装されている部分は物理演算と独立した機能として作られている  
    - 内部の物理シミュレーションはignitionのAPIを使用しており、gazeboでアクチュエータを再現するプラグインはignitionのAPIを介して関節にトルクを発生させる  
- libroboticsgroup_gazebo_mimic_joint_pluginを使うとロボットが地面に対して滑るようになる  
    - ignitionのAPIでは関節の位置を直接上書きして強引に位置を拘束する機能があるが、これを使うと無限の力を発生して反力を一切受けないリンクが生じてしまうため使用しないことを強く推奨
    - libroboticsgroup_gazebo_mimic_joint_pluginでhasPIDオプションを使用しない場合、上記の関節位置を上書きする機能を叩いているため無限に力を発生する+エネルギー保存則が崩壊し、ロボットが空間に対して静止できない(変な方向に滑りだす)
    - ibroboticsgroup_gazebo_mimic_joint_pluginでhasPIDオプションを使用すると、従属ジョイントは基準ジョイントの目標位置に追従するように独立してPID制御で動く。ロボットが空間に対して静止できるようにはなる。力学的に正しくない(従属リンクは基準リンクと独立して力を出せる)。
## よく使うコマンド  
- xacro→urdf変換:  
> rosrun xacro xacro --inorder -o robot.urdf robot.xacro  
- urdf→sdf変換:  
> gz sdf -p robot.urdf > robot.sdf  
  
## 例
> rosrun xacro xacro --inorder -o export/01_open_chain.urdf 01_open_chain.xacro　　
> gz sdf -p export/01_open_chain.urdf export/test.sdf --version=1.6  
  