import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped
import time

def create_pose(nav, x, y, w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.orientation.w = w
    return pose

def main():
    rclpy.init()
    nav = BasicNavigator()

    # Ждем, пока Nav2 проснется
    nav.waitUntilNav2Active()

    # Точки патрулирования (X, Y, Поворот)
    patrol_points = [
        create_pose(nav, 1.5, 0.5, 1.0),
        create_pose(nav, 1.5, -1.5, 1.0),
        create_pose(nav, -1.5, -1.5, 1.0)
    ]

    print("--- ПАТРУЛИРОВАНИЕ ЗАПУЩЕНО ---")

    try:
        while True:
            for i, point in enumerate(patrol_points):
                print(f"Цель №{i+1}: еду...")
                nav.goToPose(point)

                while not nav.isTaskComplete():
                    # Тут можно добавить логику, если нужно
                    pass

                result = nav.getResult()
                if result == TaskResult.SUCCEEDED:
                    print(f"Точка №{i+1} взята! Отдых 3 сек.")
                    time.sleep(3)
                else:
                    print(f"Проблема с точкой №{i+1}. Еду к следующей.")

    except KeyboardInterrupt:
        print("Остановка патруля...")
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
