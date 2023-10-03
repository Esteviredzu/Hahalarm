import tkinter as tk
import time
import threading
import pygame as pg

class Alarm:
    """Класс для управления будильником."""

    def __init__(self, root):
        """Инициализация объекта Alarm."""
        self.root = root
        root.geometry('400x200')
        self.root.title("Hahalarm")
        self.root.iconphoto(False, tk.PhotoImage(file='hahicon.png'))

        # Поле ввода часов
        self.hour_entry = tk.Entry(self.root)
        self.hour_entry.pack()

        # Поле ввода минут
        self.minute_entry = tk.Entry(self.root)
        self.minute_entry.pack()

        # Кнопка
        self.button = tk.Button(self.root, text='Ввести время', command=self.create_alarm)
        self.button.pack()

        self.indicator_label = tk.Label(self.root, text="Будильник не установлен", fg="red")
        self.indicator_label.pack()

        # Тут храним часы и минуты
        self.hour = tk.StringVar()
        self.minute = tk.StringVar()

        self.alarm_enabled = False

        # Поток
        self.alarm_thread = None

        # Добавляем кнопку для создания нового окна
        self.create_button = tk.Button(root, text="Создать новое окно", command=self.create_new_window)
        self.create_button.pack()

   
    def create_new_window(self):
        """Создает новое окно с экземпляром Alarm."""
        new_window = tk.Toplevel(self.root)
        new_app = Alarm(new_window)

    def create_alarm(self):
        """Создает и запускает будильник."""
        entered_hour = self.hour_entry.get()
        entered_minute = self.minute_entry.get()

        try:
            alarm_hour = int(entered_hour)
            alarm_minute = int(entered_minute)
            self.alarm_enabled = True

            # Запускаем поток
            self.alarm_thread = threading.Thread(target=self.check_time, args=(alarm_hour, alarm_minute))
            self.alarm_thread.daemon = True
            self.alarm_thread.start()

            message = f"Будильник установлен на {alarm_hour:02d}:{alarm_minute:02d}"
            self.update_indicator(message, "green")

        except ValueError:
            self.hour.set("Ошибка")
            self.minute.set("Ошибка")
            self.update_indicator("Ошибка: Некорректные данные для будильника", "red")

    def check_time(self, alarm_hour, alarm_minute):
        """Проверяет время и срабатывает будильник, если время совпадает."""
        while self.alarm_enabled:
            current_time = time.localtime()
            if current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute:
                self.update_indicator("Будильник сработал, и теперь по прежнему не установлен", "red")
                print('Будильник прозвенел!!!')

                music_window = tk.Tk()
                music_window.title("ВОРНИНГ!!!")
                music_window.geometry('400x200')
                music_window.configure(bg="red")

                label = tk.Label(
                    music_window,
                    text='БУДИЛЬНИК СРАБОТАЛ!!! ПОДЪЁЁЁМ!!!!!',
                    fg='white',
                    bg='red'
                )
                label.pack(pady=40)

                pg.init()
                pg.mixer.music.load('ALARM/sonng.mp3')
                pg.mixer.music.play()

                music_window.mainloop()

                pg.mixer.music.stop()

                self.alarm_enabled = False

   
    def update_indicator(self, text, color):
        """Обновляет текст индикатора и его цвет."""
        self.indicator_label.config(text=text, fg=color)

    def run(self):
        """Запускает главный цикл tkinter."""
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Alarm(root)
    app.run()
