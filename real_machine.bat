chcp 65001
cd C:\Users\terak\Documents\プログラミング\GitHub\Chiba_university\ロボット工学\ロボットアーム\

for /l %%i in (41, 1, 50) do (
    python real_machine.py %%i
)
python real_machine.py 46_1