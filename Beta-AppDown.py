import yt_dlp
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("290x500+380+100")

# لغة التطبيق
longe = ['en', 'fr', 'ar']

texts = {
    'en': {
        'language': 'Language',
        'welcome': 'Welcome to the Ghost Test Project',
        'enter_link': 'Enter the Video link',
        'enter_link2': 'Entrez le lien music ',
        'download_music': 'Download Music',
        'download_video': 'Download Video',
        'start': 'Start'
    },
    'fr': {
        'language': 'Langue',
        'welcome': 'Bienvenue dans le projet Ghost Test',
        'enter_link': 'Entrez le lien vidéo ',
        'enter_link2': 'Entrez le lien music ',
        'download_music': 'Télécharger la musique',
        'download_video': 'Télécharger la vidéo',
        'start': 'Démarrer'
    },
    'ar': {
        'language': 'اللغة',
        'welcome': 'مرحبًا بك في مشروع الشبح التجريبي',
        'enter_link': 'أدخل رابط الفيديو ',
        'enter_link2': 'أدخل رابط الاغنية ',
        'download_music': 'تحميل موسيقى',
        'download_video': 'تحميل فيديو',
        'start': 'ابدأ'
    },
}

# لغة تلقائية
selected = 'en'

# نصوص إرشادية
lbl0 = Label(win, text=texts['en']['welcome'])
lbl0.place(x=60, y=1)
lbel1 = Label(win, text=texts['en']['enter_link'])
lbel1.place(x=72, y=170)
lbel3 = Label(win, text=texts['en']['language'])
lbel3.place(x=218, y=370)

# دالة تغيير اللغة
def choix_langue(event):
    global selected
    selected = combo.get()
    if selected in texts:
        lbl0.config(text=texts[selected]['welcome'])
        lbel1.config(text=texts[selected]['enter_link'])
        lbel3.config(text=texts[selected]['language'])
        botn1.config(text=texts[selected]['download_music'])
        botn2.config(text=texts[selected]['download_video'])
    else:
        print('Language not supported')

combo = ttk.Combobox(win, values=longe, width=5)
combo.place(x=220, y=392)
combo.bind("<<ComboboxSelected>>", choix_langue)

# دالة اختيار الفيديو
def vidou():

    win2 = Tk()
    win2.geometry('500x500+380+100')
    win2.title("Welcome")
    lbel1 = Label(win2, text=texts[selected]['enter_link'], bg="#d7bde2")
    lbel1.pack()
    win2.configure(bg="#9b59b6")
    frame = Frame(win2, bg="#d7bde2", width=450, height=450)
    frame.pack(pady=25)
    url_entry1 = Entry(win2, width=50)
    url_entry1.place(x=100, y=200)

    # شريط التقدم
    progress = ttk.Progressbar(win2, orient="horizontal", length=300, mode='determinate')
    percent_label = Label(win2, text="0%", bg="#d7bde2")

    # دالة التحديث من yt_dlp
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', 1)  # لا نجعلها صفر لتفادي القسمة على صفر

            percent = int(downloaded * 100 / total)
            progress['value'] = percent  # تحديث شريط التقدم
            percent_label.config(text=f"{percent}%")  # تحديث النص
            win2.update_idletasks()

        elif d['status'] == 'finished':
            progress['value'] = 100
            percent_label.config(text="100%")
            win2.update_idletasks()
            print("Download finished!")

    # دالة التحميل
    def test():
        # إظهار شريط التقدم والنص
        progress.place(x=100, y=300)
        percent_label.place(x=410, y=300)

        url1 = url_entry1.get()
        ydl_option = {
            'format': 'best',
            'outtmpl': 'C:/Users/Ghost/Downloads/vidou/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook] 
        }

        with yt_dlp.YoutubeDL(ydl_option) as var:
            var.download([url1])

    # زر بدء تحميل
    butn1 = Button(win2, text='Start', width=10, command=test)
    butn1.place(x=210, y=230)

    win2.mainloop()
def music():
    #الواجهة الثانية
    win3 = Tk()
    win3.geometry('500x500+380+100')
    win3.title("Welcome")
    lbel1 = Label(win3, text=texts[selected]['enter_link2'], bg="#edbb99")
    lbel1.pack()
    win3.configure(bg="#edbb99")
    frame = Frame(win3, bg="#f7dc6f", width=450, height=450)
    frame.pack(pady=25)
    url_entry1 = Entry(win3, width=50)
    url_entry1.place(x=100, y=200)
    # شريط التقدم
    progress = ttk.Progressbar(win3, orient="horizontal", length=300, mode='determinate')
    percent_label = Label(win3, text="0%", bg="#d7bde2")
    # دالة التحديث من yt_dlp
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', 1)  # لا نجعلها صفر لتفادي القسمة على صفر

            percent = int(downloaded * 100 / total)
            progress['value'] = percent  # تحديث شريط التقدم
            percent_label.config(text=f"{percent}%")  # تحديث النص
            win3.update_idletasks()

        elif d['status'] == 'finished':
            progress['value'] = 100
            percent_label.config(text="100%")
            win3.update_idletasks()
            print("Download finished!")
    #win3.mainloop() <==== error stop fonction worning
    # دالة التحميل الموسيقة
    def test1():
        # إظهار شريط التقدم والنص
        progress.place(x=100, y=300)
        percent_label.place(x=410, y=300)

        url2 = url_entry1.get()
        ydl_option = {
        'format': 'bestaudio',
        'outtmpl': 'C:/Users/Ghost/Downloads/music/%(title)s.%(ext)s',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        },
}
        with yt_dlp.YoutubeDL(ydl_option) as var:
            var.download([url2])
        print ('finish')
    # زر بدء تحميل
    butn2 = Button(win3, text=texts[selected]['start'], width=10, command=test1)
    butn2.place(x=210, y=230)
    win3.mainloop()




# ازرار الاختيار
botn1 = ttk.Button(win, text=texts[selected]['download_music'], width=20,command=music)
botn1.place(x=77, y=210)

botn2 = ttk.Button(win, text=texts[selected]['download_video'], width=20, command=vidou)
botn2.place(x=77, y=250)

# نافذة التطبيق الرئيسية
win.mainloop()
