#==========================kirana========================
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller import *
from datetime import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class StudyLogApp:
    def __init__(self, root):  
        self.root = root
        self.root.title("StudyLog")
        self.root.geometry("1000x700")
        self.root.minsize(900, 650)
        init_csv_files()
        self.absen_stack = []
        self.create_welcome_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_welcome_page(self):
        self.clear_frame()
        left = ctk.CTkFrame(self.root, fg_color='white', width=500, corner_radius=0)
        right = ctk.CTkFrame(self.root, fg_color='#0b355d', width=500, corner_radius=0)
        left.pack(side='left', fill='both', expand=True)
        right.pack(side='right', fill='both', expand=True)

        logo_img = Image.open("asset/STUDY LOG.png").resize((260, 260))
        logo_img = ImageTk.PhotoImage(logo_img)
        logo = ctk.CTkLabel(left, image=logo_img, text="", bg_color='white')
        logo.image = logo_img
        logo.place(relx=0.5, rely=0.30, anchor='center')

        ctk.CTkLabel(left, text="Welcome to", font=ctk.CTkFont(size=26, weight="bold"), text_color="#0b355d").place(relx=0.5, rely=0.52, anchor='center')
        ctk.CTkLabel(left, text="StudyLog", font=ctk.CTkFont(size=48, weight="bold", slant="italic"), text_color="#0b355d").place(relx=0.5, rely=0.60, anchor='center')

        ctk.CTkButton(
            right, text="Start", width=300, height=60, corner_radius=30,
            command=self.create_login_page, fg_color="#b5d0e6", text_color="#0b355d",
            font=ctk.CTkFont(size=20, weight="bold")
        ).place(relx=0.5, rely=0.4, anchor='center')
        ctk.CTkButton(
            right, text="Our Team", width=300, height=60, corner_radius=30,
            command=self.create_team_page, fg_color="#b5d0e6", text_color="#0b355d",
            font=ctk.CTkFont(size=20, weight="bold")
        ).place(relx=0.5, rely=0.55, anchor='center')

    def create_team_page(self):
        self.clear_frame()
        container = ctk.CTkFrame(self.root, fg_color="white")
        container.pack(fill='both', expand=True)

        header = ctk.CTkFrame(container, fg_color='#0b355d', height=70, corner_radius=0)
        header.pack(fill='x')
        logo_img = Image.open("asset/STUDY LOG.png").resize((65, 65))
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(header, image=logo_img, text="")
        logo_label.image = logo_img
        logo_label.pack(side="left", padx=10, pady=7)
        ctk.CTkLabel(header, text="StudyLog", font=ctk.CTkFont(size=24, weight="bold"), text_color="white").pack(side="left", padx=8)
        ctk.CTkButton(header, text="Back", width=120, height=44, corner_radius=18,
                      command=self.create_welcome_page, fg_color="#b5d0e6", text_color="#0b355d",
                      font=ctk.CTkFont(size=16, weight="bold")).pack(side="right", padx=24)

        ctk.CTkLabel(container, text="Our Team", font=ctk.CTkFont(size=32, weight="bold"), text_color="#0b355d").pack(pady=30)

        grid = ctk.CTkFrame(container, fg_color='white', width=900, height=550)
        grid.pack(expand=True)
        grid.pack_propagate(False)

        team_data = [
            ("Iqlima Juliana", "2417051048", "ima.jpg"),
            ("Maulana Abdillahul F.", "2417051055", "maul.jpg"),
            ("Kirana Aditya M.", "2417051057", "kirana.jpg"),
            ("Rizka Aprilia", "2417051066", "rizka.jpg")
        ]

        card_width, card_height = 340, 220
        for i, (nama, npm, foto) in enumerate(team_data):
            card = ctk.CTkFrame(grid, width=card_width, height=card_height, fg_color="#b5d0e6", corner_radius=40)
            card.place(x=(i % 2) * (card_width + 60) + 60, y=(i // 2) * (card_height + 40) + 20)
            card.pack_propagate(False)
            try:
                img = Image.open(f"asset/{foto}").resize((200, 170))
                photo = ImageTk.PhotoImage(img)
                img_label = ctk.CTkLabel(card, image=photo, text="")
                img_label.image = photo
                img_label.pack(pady=0)
            except:
                ctk.CTkLabel(card, text="(Foto)", text_color="#0b355d", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=20)

            ctk.CTkLabel(card, text=nama, font=ctk.CTkFont(size=18, weight="bold"), text_color="#0b355d").pack(pady=(12, 0))
            ctk.CTkLabel(card, text=npm, font=ctk.CTkFont(size=16), text_color="#0b355d").pack()

#==========================rizka==========================
        
#========================================================================iqlima===================================================================================

#================================================================maul=========================================================================================
