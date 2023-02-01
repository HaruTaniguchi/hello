import rclpy                    # ROS2のPythonモジュールをインポートする
from rclpy.node import Node  # rclpy.nodeモジュールからNodeクラスをインポート

def todo(): # 実行したい処理の関数
   while True:                # 無限ループ
       print("hello world")   # 端末に出力    

def main(): # main関数
    rclpy.init()               # 初期化
    node = Node('hello_node')  # ノードの生成。Nodeクラスのコンストラクタの引数はノード名。
    todo()                     # 実行したい処理
    rclpy.spin(node)           # 終了まで待機
    rclpy.shutdown()           # 終了処理

if __name__ == '__main__':
    main()
