import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Инициализация pygame для работы с аудио
pygame.mixer.init()

# Функция для выбора файла
def open_file():
    file_path = filedialog.askopenfilename(
        title="Выберите аудиофайл",
        filetypes=(("Аудиофайлы", "*.mp3 *.wav"), ("Все файлы", "*.*"))
    )
    if file_path:
        pygame.mixer.music.load(file_path)
        file_name.set(os.path.basename(file_path))

# Функция для воспроизведения аудио
def play():
    pygame.mixer.music.play()

# Функция для паузы
def pause():
    pygame.mixer.music.pause()

# Функция для остановки
def stop():
    pygame.mixer.music.stop()

# Функция для продолжения воспроизведения
def unpause():
    pygame.mixer.music.unpause()

# Создание основного окна
root = tk.Tk()
root.title("Аудиоплеер")
root.geometry("400x150")

# Переменная для отображения имени файла
file_name = tk.StringVar()
file_name.set("Файл не выбран")

# Элементы интерфейса
label = tk.Label(root, textvariable=file_name, font=("Arial", 12))
label.pack(pady=10)

open_button = tk.Button(root, text="Выбрать файл", command=open_file)
open_button.pack(pady=5)

play_button = tk.Button(root, text="Воспроизвести", command=play)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Пауза", command=pause)
pause_button.pack(pady=5)

unpause_button = tk.Button(root, text="Продолжить", command=unpause)
unpause_button.pack(pady=5)

stop_button = tk.Button(root, text="Стоп", command=stop)
stop_button.pack(pady=5)

# Запуск основного цикла
root.mainloop()