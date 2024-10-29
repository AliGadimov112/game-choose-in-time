import random
import datetime
import time
import keyboard
print('добро пожаловать в игру "Время на размышления"!')
start_time = datetime.datetime.now()
print(f'время начала:{start_time.strftime("%H:%M:%S")}')
print("нажмите enter для начала...")

endGame_time = datetime.datetime.now()
print(f'время окончания игры:{endGame_time.strftime("%H:%M:%S")}')
total_time = endGame_time - start_time
print(f'общее время игры: {total_time.total_seconds():.2f}секунд')
num_rounds = random.randint (1,4)
reaction_times = []
print(f"Вам предстоит {num_rounds} раундов.")
keys = ['enter', 'space', 'tab', 'backspace', 'esc', 'delete', 'end', 'page up', 'page down', 'up', 'down', 'right', 'left', 'shift', 'ctrl', 'alt']
for round_num in range(1, num_rounds + 1):

  print(f"\nРаунд {round_num}")
  wait_time = random.randint(1, 3)
  print("Ждите сигнала...")
  time.sleep(wait_time)
  random_key = random.choice(keys)
  print(f'нажмите клавишу{random_key}!')
  start_time_input = time.time()
  while True:
    if keyboard.is_pressed(random_key):
      break
    end_time = time.time()
    reaction_time = end_time - start_time_input
    reaction_times.append(reaction_time)
    print(f'время реакции:{reaction_time:.3f}секунд')
    break
end_game_time = time.time()
total_time = sum(reaction_times)
average_time = total_time / num_rounds
game_duration = end_game_time - start_time
print("\n--- Результаты игры ---")
print(f"Общее время реакции: {total_time:.3f} секунд")
print(f"Среднее время реакции: {average_time:.3f} секунд")
print(f"Время окончания игры: {time.strftime('%H:%M:%S', time.localtime(end_game_time))}")
print(f"Общее время игры: {game_duration:.3f} секунд")





