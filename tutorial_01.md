tutorial_01  
====
  
tutorial_01:通常の開いた3節のリンクを作成します  
  
 #### 注意事項  
##### - linkについて  
- link関連のパラメータ:http://wiki.ros.org/urdf/XML/link  
- linkのinertialタグ内が空だとgazeboで消える  
    - urdf->sdfパーサは、inertialが空のリンクを無視する  
    - 無視されたリンクから先のjoint、linkはすべて無視される  
- linkのinertialタグ内の数値は、物理的に整合性の取れない値を入れるとモデルが崩壊する  
    - 適当な値で試したい時は、質量0.5kg程度の立方体で入力しています。(例)  
```xml
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0.5 0 -0.05" rpy="0 0 0"/>
      <inertia
        ixx="0.0001"
        ixy="0.0000" iyy="0.0001"
        ixz="0.0000" iyz="0.0000" izz="0.0001"/>
    </inertial>
```
- linkのinertialタグについて、質量5gを下回る部品は計算が不安定になる  
    - 質量が5g程度になるように質量・慣性行列を定数倍する  
    - ロボワンの場合はロボット全体の重量に対して十分小さいとみなし、厳密性を諦めた。  

##### - jointについて  
- joint関連のパラメータ:http://wiki.ros.org/urdf/XML/joint  
- 機構的な可動範囲のリミットはできるだけjointのlimitで制限する
    - リンク同士の接触判定は計算が重い
    - 特異点付近は不安定になりやすい。できるだけjointでリミットをかけておくことで物理演算の崩壊が防げる
- jointのdynamicsタグ内の数値(damping,friction)は、基本的に効かない。大きい数字を入れると爆発する  
- jointにmimicタグが設定されている場合について  
    - jointにmimicタグが設定されている場合でもsdfではmimicタグを無視して通常関節と同じように振る舞う  
    - gazeboプラグイン(joint_state_controllerなど、これらはsdfを使用できずurdfを読み込む)では関節として認識されず、mimic jointにアクチュエータなどを配置することができない
    - robot_state_publisherを使用した場合、rviz上では基準関節に対して勝手に従属に動く。この時使用するjointstatesには基準関節の角度が含まれていればよく、mimic jointの関節角は不要。仮にmimic jointの関節角が含まれていても無視される  
    
    


