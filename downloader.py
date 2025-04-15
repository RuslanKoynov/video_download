import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = entry.get()
    if not url:
        messagebox.showwarning("Ошибка", "Введите ссылку на видео.")
        return
    
    try:
        ydl_opts = {
            'outtmpl': 'videos/%(title)s.%(ext)s',
            'format': format_var.get()
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Готово", "Видео успешно загружено.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при загрузке: {e}")

# Создание GUI
root = tk.Tk()
root.title("Видео Загрузчик")
root.geometry("400x200")

tk.Label(root, text="Ссылка на видео:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Label(root, text="Формат загрузки:").pack(pady=5)
format_var = tk.StringVar(value='best')
tk.Radiobutton(root, text="Лучшее качество", variable=format_var, value='best').pack()
tk.Radiobutton(root, text="Только аудио", variable=format_var, value='bestaudio').pack()

tk.Button(root, text="Скачать", command=download_video).pack(pady=10)

root.mainloop()
