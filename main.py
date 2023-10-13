#Module tim kiem
from search import search           

#Giao dien
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo

#khoi tao nhung thu co ban
window = Tk()
window.config(bg="#283655")
window.title("MOVIE SEARCH ENGINE")
window.geometry('{}x{}'.format(
    window.winfo_screenwidth(), window.winfo_screenheight()))
Label(window,
      text="welcome",
      font=("Times New Roman", 15),
      background='green',
      foreground="white").grid(column=0,
                               row=0)

#label trong cua so 
lb_1 = Label(window, text="Key word", font=("cambria", 12))
lb_1.place(x=20, y=40)

lb_2 = Label(window, text="Genres", font=("cambria", 12))
lb_2.place(x=20, y=80)

lb_2 = Label(window, text="Language", font=("cambria", 12))
lb_2.place(x=20, y=120)

lb_2 = Label(window, text="OVERVIEWS", font=("cambria", 15))
lb_2.place(x=220, y=200)


#3 button de show ra so phim nguoi dung mong doi
rv = IntVar()
rv.set(1)
rdo1 = Radiobutton(window, text="Top10", variable=rv, value=1)
rdo2 = Radiobutton(window, text="Top 5", variable=rv, value=2)
rdo3 = Radiobutton(window, text="All", variable=rv, value=3)

rdo1.place(x=20   , y=150)
rdo2.place(x=120  , y=150)
rdo3.place(x=220 , y=150)

#textbox 
title_tb = Entry(window, width=20, border=3)
title_tb.place(x=120, y=40)



#tao combobox luu the loai+ngon ngu
genres = ('--', 'Action', 'Animation', 'Adventure', 'Crime', 'Comedy', 'Documentary', 'Drama', 'Family', 'Foreign', 'Fantasy',
          'History', 'Horror', 'Music', 'Mystery',
           'Romance',  'Science Fiction', 'Thriller', 'TV Movie', 'Western', 'War')
genres_cbx = Combobox(window, values=genres)
genres_cbx.place(x=120, y=80)

lang = ("--", "en (English)", "es (Spanish)", "fr (French)", "zh (Chinese)", "ar (Arabic)", "ru (Russian)", "pt (Portuguese)", "de (German)", "ja (Japanese)", "it (Italian)", "tr (Turkish)", "vi (Vietnamese)", "pl (Polish)", "ko (Korean)", "nl (Dutch)", "sv (Swedish)", "nb (Norwegian Bokmal)", "da (Danish)", "fa (Persian)", "th (Thai)", "ca (Catalan)", "ro (Romanian)", "cs (Czech)",
        "sk (Slovak)", "fi (Finnish)", "hu (Hungarian)", "el (Greek)", "he (Hebrew)", "eo (Esperanto)", "bn (Bengali)", "xx (Unknown language)", "hi (Hindi)", "is (Icelandic)", "sh (Serbo-Croatian)", "ka (Georgian)", "bs (Bosnian)", "cy (Welsh)", "ps (Pashto)", "mn (Mongolian)", "mk (Macedonian)", "sr (Serbian)", "bm (Bambara)", "ab (Abkhazian)", "wo (Wolof)", "cn (Cantonese)", "bo (Tibetan)")
lang_cbx = Combobox(window, values=lang)
lang_cbx.place(x=120, y=120)


#tao listbox de luu phim+diem
title_listbox = Listbox(window, width=100, height=40,
                          bg="#4d648d", fg="white", font="calbiri",
                          )
title_listbox.place(x=660, y=0)


#tao scrollertext de show overviews
scrtxt = ScrolledText(window, width=58, height=80) 
scrtxt.place(x=0,y=250)
scrtxt.config(bg="#4d648d",fg="white",font="Helvetica 14")


#khi nut search duoc click thi moi thu bat dau
def cmd_yes():
    #thao tac tren cua so
    name = title_tb.get()
    chose_genres = genres_cbx.get()
    how_many = rv.get()
    chose_lang = lang_cbx.get()[:2]
    
    res = search(name, chose_genres, chose_lang,how_many)
    
    #xoa list box tim kiem cu
    title_listbox.delete(0, END)
    scrtxt.delete('1.0', END)

    #show các phim va diem trung binh
    if len(res) == 0 :  #khong co phim
        showinfo("Notification","There are no movies that match your criteria")
    for x in res:
        title_listbox.insert(END, f"{x[1]} | {x[0]}")


    #khi user click vao mot phim o trong list box
    def on_click(event):
        #lay vi tri cua hang duoc click
        index = event.widget.curselection()[0]
        #xoa overviews cu de show ra overview moi
        scrtxt.delete('1.0', END)
        scrtxt.insert(INSERT,res[index][0].upper())
        scrtxt.insert(INSERT,'\n\n'+res[index][2])
    title_listbox.bind("<<ListboxSelect>>", on_click)


#tạo nut bam search
cmbt1 = Button(window, text="Search", font=("consolas", 15),
               bg="#d0e1f9", fg="red", command=cmd_yes)
cmbt1.place(x=450, y=60)   
    

#vong lap chuong trinh
window.mainloop()
