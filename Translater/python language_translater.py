from tkinter import*
import tkinter as tk
from tkinter import ttk
from googletrans import Translator #pip install googletrans==3.1.0a0
from tkinter import messagebox


root=tk.Tk()
root.title('LANGUAGE TRANSLATOR')
root.geometry('590x370')

def translate():
    lang_1=text_entry1.get("0.1","end-1c")
    cl=choose_language.get()

    if lang_1=='':
        messagebox.showerror('Language Translator','Enter the text to translate!')
    else:
        text_entry2.delete(1.0,'end')
        translator=Translator()
        output=translator.translate(lang_1,dest=cl)
        text_entry2.insert('end',output.text)
def clear():
    text_entry1.delete(1.0,'end')
    text_entry2.delete(1.0,'end')

a=tk.StringVar()

frame1=Frame(root,width=590,height=370,relief=RIDGE,borderwidth=5,bg='#F7DC6F')
Label(root,text="Language Translator",font=("Helventica 20 bold"),fg='#F7DC6F').pack(pady=10)

auto_select=ttk.Combobox(frame1,width=27,textvariable=a,state='randomly',font=('verdana',12,'bold'))

auto_select['values']=(
                           'Auto Select',   
                      )

auto_select.place(x=15,y=60)
auto_select.current(0)

l=tk.StringVar()
choose_language=ttk.Combobox(frame1,width=27,textvariable=a,state='randomly',font=('verdana',12,'bold'))

choose_language['values']=(
                            'Afrikaans',
'Albanian',
'Amharic',
'Arabic (Egyptian Spoken)',
'Arabic (Levantine)',
'Arabic (Modern Standard)',
'Arabic (Moroccan Spoken)',
'Arabic (Overview)',
'Aramaic',
'Armenian',
'Assamese',
'Aymara',
'Azerbaijani',
'Balochi',
'Bamanankan',
'Bashkort (Bashkir)',
'Basque',
'Belarusan',
'Bengali',
'Bhojpuri',
'Bislama',
'Bosnian',
'Brahui',
'Bulgarian',
'Burmese',
'Cantonese',
'Catalan',
'Cebuano',
'Chechen',
'Cherokee',
'Croatian',
'Czech',
'Dakota',
'Danish',
'Dari',
'Dholuo',
'Dutch',
'English',
'Esperanto',
'Estonian',
'Éwé',
'Finnish',
'French',
'Georgian',
'German',
'Gikuyu',
'Greek',
'Guarani',
'Gujarati',
'Haitian Creole',
'Hausa',
'Hawaiian',
'Hawaiian Creole',
'Hebrew',
'Hiligaynon',
'Hindi',
'Hungarian',
'Icelandic',
'Igbo',
'Ilocano',
'Indonesian (Bahasa Indonesia)',
'Inuit/Inupiaq',
'Irish Gaelic',
'Italian',
'Japanese',
'Jarai',
'Javanese',
'K’iche’',
'Kabyle',
'Kannada',
'Kashmiri',
'Kazakh',
'Khmer',
'Khoekhoe',
'Korean',
'Kurdish',
'Kyrgyz',
'Lao',
'Latin',
'Latvian',
'Lingala',
'Lithuanian',
'Macedonian',
'Maithili',
'Malagasy',
'Malay (Bahasa Melayu)',
'Malayalam',
'Mandarin (Chinese)',
'Marathi',
'Mende',
'Mongolian',
'Nahuatl',
'Navajo',
'Nepali',
'Norwegian',
'Ojibwa',
'Oriya',
'Oromo',
'Pashto',
'Persian',
'Polish',
'Portuguese',
'Punjabi',
'Quechua',
'Romani',
'Romanian',
'Russian',
'Rwanda',
'Samoan',
'Sanskrit',
'Serbian',
'Shona',
'Sindhi',
'Sinhala',
'Slovak',
'Slovene',
'Somali',
'Spanish',
'Swahili',
'Swedish',
'Tachelhit',
'Tagalog',
'Tajiki',
'Tamil',
'Tatar',
'Telugu',
'Thai',
'Tibetic Languages',
'Tigrigna',
'Tok Pisin',
'Turkish',
'Turkmen',
'Ukrainian',
'Urdu',
'Uyghur',
'Uzbek',
'Vietnamese',
'Warlpiri',
'Welsh',
'Wolof',
'Xhosa',
'Yakut',
'Yiddish',
'Yoruba',
'Yucatec',
'Zapotec',
'Zulu',
)

choose_language.place(x=3)
choose_language.current(0)

text_entry1=Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
text_entry1.place(x=10,y=100)

text_entry2=Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
text_entry2.place(x=10,y=100)

btn1=Button(frame1,command=translate,text="Translate",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",cursor="hand2")  
btn1.place(x=185,y=300)  

btn2=Button(frame1,command=clear,text="Clear",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",cursor="hand2")  
btn2.place(x=300,y=300) 

root.mainloop()


























































































































































































