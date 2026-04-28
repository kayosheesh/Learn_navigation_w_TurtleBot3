# Learn Navigation with TurtleBot3 (ROS 2 Humble)

Проект по реализации автономной навигации робота TurtleBot3 в симуляторе Gazebo.

## 1. Установка необходимых пакетов
Выполните команды в терминале Ubuntu 22.04 для установки ROS 2 и инструментов TurtleBot3:

```bash
sudo apt update
sudo apt install ros-humble-turtlebot3-gazebo \
                 ros-humble-turtlebot3-simulations \
                 ros-humble-turtlebot3-navigation2 \
                 ros-humble-nav2-bringup \
                 ros-humble-nav2-simple-commander -y

echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

2. Настройка рабочего пространства
Создание папок и клонирование репозитория:

```bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/src
git clone https://github.com/Parf1x/Learn_navigation_w_TurtleBot3.git
cd ~/turtlebot3_ws
colcon build
source install/setup.bash
```

3. Инструкция по запуску
Для запуска автономного патрулирования откройте 3 отдельных терминала.
Терминал 1: Запуск симулятора:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Терминал 2: Запуск системы навигации:

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
     use_sim_time:=True \
     map:=$HOME/turtlebot3_ws/src/Learn_navigation_w_TurtleBot3/map.yaml
```

Примечание: После открытия RViz необходимо нажать кнопку 2D Pose Estimate и указать на карте текущее положение робота.

Терминал 3: Запуск автономного скрипта:

```bash
cd ~/turtlebot3_ws/src/Learn_navigation_w_TurtleBot3/
python3 patrol.py
```

📂 Описание файлов проекта
map.yaml — Конфигурационный файл карты (масштаб, пороги занятости).

map.pgm — Изображение карты лабиринта, построенное с помощью SLAM.

patrol.py — Скрипт на Python, использующий nav2_simple_commander для циклического патрулирования заданных точек.

plan_uchebnogo_kursa.md — Теоретический план и дорожная карта проекта.

ustanovka_i_nastroika_sredy.md — Дополнительная справка по настройке окружения.

⚠️ Решение частых проблем (WSL 2)
Черный экран или вылет Gazebo:
Перед запуском введите: export LIBGL_ALWAYS_SOFTWARE=1

Ошибка "Spawn service failed":
Закройте Gazebo и запустите Терминал 1 снова. Обычно со второго раза робот появляется успешно.

Робот не едет в скрипте:
Убедитесь, что вы выполнили локализацию (2D Pose Estimate) в RViz, иначе навигация не сможет построить путь.

Ссылка на видеоотчет готового проекта:

https://youtu.be/iP7PXnv_raI



Автор: Даниил Парфенюк, Владислав Мисюрко
