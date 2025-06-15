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
            
    def create_login_page(self):
        self.clear_frame()
        left = ctk.CTkFrame(self.root, fg_color='white', width=500, corner_radius=0)
        right = ctk.CTkFrame(self.root, fg_color='#0b355d', width=500, corner_radius=0)
        left.pack(side='left', fill='both', expand=True)
        right.pack(side='right', fill='both', expand=True)

        logo_img = Image.open("asset/STUDY LOG.png").resize((300, 300))
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(left, image=logo_img, text="")
        logo_label.image = logo_img
        logo_label.place(relx=0.5, rely=0.25, anchor='center')

        ctk.CTkLabel(left, text="StudyLog", font=ctk.CTkFont(size=36, weight="bold", slant="italic"), text_color="#0b355d").place(relx=0.5, rely=0.48, anchor='center')
        ctk.CTkLabel(left, text="Attendance Tracker", text_color="#0b355d", font=ctk.CTkFont(size=24, weight="bold")).place(relx=0.5, rely=0.56, anchor='center')
        ctk.CTkLabel(
            left,
            text="Aplikasi absensi digital yang mencatat kehadiran\nsecara otomatis dan efisien.\nSetiap kali hadir, skor keaktifan akan bertambah.\nAplikasi ini sederhana, efisien, dan mudah digunakan.",
            text_color="#0b355d", font=ctk.CTkFont(size=13), justify="center"
        ).place(relx=0.5, rely=0.65, anchor='center')

        form = ctk.CTkFrame(right, fg_color="white", corner_radius=18)
        form.place(relx=0.5, rely=0.5, anchor='center')
        form.pack_propagate(False)
        form.configure(width=340, height=340)

        self.nama_entry = self.styled_entry(form, "Nama")
        self.npm_entry = self.styled_entry(form, "NPM")
        self.pass_entry = self.styled_entry(form, "Password", show='*')

        ctk.CTkButton(
            form, text="Login", command=self.login_user, corner_radius=14, width=240,
            fg_color="#b5d0e6", text_color="#0b355d", font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(22, 6))

        ctk.CTkLabel(
            form, text="forgot password?", font=ctk.CTkFont(size=11), text_color='#0b355d'
        ).pack(pady=(0, 10))

    def styled_entry(self, parent, label, show=None):
        ctk.CTkLabel(parent, text=label, text_color='#0b355d', anchor='w', font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=12, pady=(10,0))
        entry = ctk.CTkEntry(parent, show=show, corner_radius=7, width=250, font=ctk.CTkFont(size=14))
        entry.pack(padx=12, pady=7)
        return entry

    def labeled_entry(self, parent, label):
        ctk.CTkLabel(parent, text=label, text_color='#0b355d', font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=12, pady=(10,0))
        entry = ctk.CTkEntry(parent, corner_radius=7, width=250, font=ctk.CTkFont(size=14))
        entry.pack(padx=12, pady=7)
        return entry

    def labeled_combobox(self, parent, label, values):
        ctk.CTkLabel(parent, text=label, text_color="#0b355d", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=24)
        combo = ctk.CTkComboBox(parent, values=values, corner_radius=7, width=270, font=ctk.CTkFont(size=14))
        combo.pack(pady=10)
        return combo

    def login_user(self):
        nama = self.nama_entry.get()
        npm = self.npm_entry.get()
        password = self.pass_entry.get()

        if not all([nama, npm, password]):
            messagebox.showerror("Error", "Semua field harus diisi")
            return

        if verify_or_register_user(nama, npm, password):
            self.current_user = (nama, npm)
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {nama}!")
            self.create_absen_page()
        else:
            messagebox.showerror("Login Gagal", "Nama, NPM, atau Password salah.")
    def create_absen_page(self):
        self.clear_frame()
        header = ctk.CTkFrame(self.root, fg_color='#0b355d', height=60, corner_radius=0)
        header.pack(fill='x')

        logo_img = Image.open("asset/STUDY LOG.png").resize((50, 50))
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(header, image=logo_img, text="")
        logo_label.image = logo_img
        logo_label.pack(side="left", padx=16, pady=7)

        ctk.CTkLabel(header, text="StudyLog", font=ctk.CTkFont(size=22, weight="bold"), text_color="white").pack(side="left")
        ctk.CTkButton(
            header, text="Log Out", width=120, height=40, corner_radius=14,
            command=self.show_scoreboard,
            fg_color="#b5d0e6", text_color="#0b355d",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(side="right", padx=26)

        left = ctk.CTkFrame(self.root, fg_color='white', width=340, corner_radius=0)
        right = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
        left.pack(side='left', fill='y')
        right.pack(side='right', fill='both', expand=True)

        form = ctk.CTkFrame(left, fg_color="#e1ecf4", corner_radius=18)
        form.pack(pady=18, padx=12)
        form.pack_propagate(False)
        form.configure(width=310, height=520)

        ctk.CTkLabel(form, text="StudyLog", font=ctk.CTkFont(size=22, weight="bold"), text_color="#0b355d").pack(pady=(12, 6))

        ctk.CTkLabel(form, text="Mata Kuliah", text_color="#0b355d", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=10, pady=(6,0))
        self.combo_matkul = ctk.CTkComboBox(form, values=MATA_KULIAH, corner_radius=7, width=250, font=ctk.CTkFont(size=14))
        self.combo_matkul.pack(padx=10, pady=4)

        ctk.CTkLabel(form, text="Hari", text_color="#0b355d", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=10, pady=(6,0))
        self.combo_hari = ctk.CTkComboBox(form, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"], corner_radius=7, width=250, font=ctk.CTkFont(size=14))
        self.combo_hari.pack(padx=10, pady=4)

        ctk.CTkLabel(form, text="Tanggal", text_color="#0b355d", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor='w', padx=10, pady=(6,0))
        self.entry_tanggal = ctk.CTkEntry(form, placeholder_text="dd/mm/2025", width=250, font=ctk.CTkFont(size=14))
        self.entry_tanggal.pack(padx=10, pady=4)
        self.entry_tanggal.bind("<FocusOut>", self.update_hari_dan_matkul)
        self.entry_tanggal.bind("<Return>", self.update_hari_dan_matkul)

        self.entry_jam = self.labeled_entry(form, "Jam")

        btn_frame = ctk.CTkFrame(form, fg_color='#e1ecf4')
        btn_frame.pack(pady=18, fill="x", expand=True)

        for i in range(2):
            btn_frame.grid_rowconfigure(i, weight=1)
            btn_frame.grid_columnconfigure(i, weight=1)

        for i, status in enumerate(["Hadir", "Alpha", "Sakit", "Izin"]):
            ctk.CTkButton(
                btn_frame, text=status, width=120, height=60, corner_radius=18,
                fg_color="#0b355d", text_color='white',
                font=ctk.CTkFont(size=16, weight="bold"),
                command=lambda s=status: self.submit_absen(s)
            ).grid(row=i//2, column=i%2, padx=16, pady=16, sticky="nsew")

        self.summary_frame = right
        self.update_absen_summary()

    def submit_absen(self, status):
        matkul = self.combo_matkul.get()
        hari = self.combo_hari.get()
        jam = self.entry_jam.get()
        tanggal = self.entry_tanggal.get()
        nama, npm = self.current_user

        if not all([matkul, hari, jam, tanggal]):
            messagebox.showerror("Error", "Semua field harus diisi")
            return

        try:
            tgl_obj = datetime.strptime(tanggal, "%d/%m/%Y")
            if tgl_obj.year != 2025:
                messagebox.showerror("Tahun Salah", "Tahun harus 2025")
                return
        except ValueError:
            messagebox.showerror("Format Salah", "Format tanggal harus dd/mm/2025")
            return

        try:
            jam_obj = datetime.strptime(jam, "%H:%M")
        except ValueError:
            messagebox.showerror("Format Salah", "Format jam harus jj:jj (24 jam, contoh 08:30)")
            return

        if matkul in self.absen_stack:
            messagebox.showwarning(
                "Sudah Absen",
                "Anda sudah absen di mata kuliah ini."
            )
            return

        if is_already_absent(nama, npm, matkul, tanggal):
            messagebox.showwarning(
                "Absensi Ganda",
                f"Anda sudah melakukan absensi untuk mata kuliah '{matkul}' pada tanggal {tanggal}."
            )
            return

        save_absen(nama, npm, matkul, hari, jam, tanggal, status)
        self.absen_stack.append(matkul)
        messagebox.showinfo("Absensi Berhasil", f"Absensi untuk mata kuliah '{matkul}' pada tanggal {tanggal} berhasil disimpan.")
        self.update_absen_summary()

    def update_absen_summary(self):
        for widget in self.summary_frame.winfo_children():
            widget.destroy()

        nama, npm = self.current_user
        count, total = get_absen_summary(nama, npm)

        grid = ctk.CTkFrame(self.summary_frame, fg_color='white', width=400)
        grid.pack(padx=18, pady=36, anchor='n')
        grid.pack_propagate(False)

        card_width, card_height = 370, 64
        for i, mk in enumerate(MATA_KULIAH):
            row, col = i // 2, i % 2
            card = ctk.CTkFrame(grid, width=card_width, height=card_height, fg_color="#b5d0e6", corner_radius=18)
            card.grid(row=row, column=col, padx=18, pady=14)
            card.pack_propagate(False)

            absen_box = ctk.CTkFrame(card, width=70, height=36, fg_color='white', corner_radius=18)
            absen_box.place(relx=1.0, rely=0.5, x=-22, anchor='e')
            absen_box.pack_propagate(False)
            ctk.CTkLabel(absen_box, text=f"{count[mk]}/{total[mk]}", text_color="#0b355d", font=ctk.CTkFont(size=16, weight="bold")).pack(expand=True)

            ctk.CTkLabel(card, text=mk, font=ctk.CTkFont(size=15, weight="bold"), text_color="#0b355d", anchor='w').place(x=22, rely=0.5, anchor='w')

    def update_hari_dan_matkul(self, event=None):
        tanggal = self.entry_tanggal.get()
        hari = get_hari_from_tanggal(tanggal)
        self.combo_hari.set(hari)
        matkul_list = get_matkul_from_hari(hari)
        self.combo_matkul.configure(values=matkul_list)
        if matkul_list:
            self.combo_matkul.set(matkul_list[0])
        else:
            self.combo_matkul.set("")

class ScoreboardApp(ctk.CTkFrame):
    def __init__(self, master, controller=None):
        super().__init__(master)
        self.controller = controller
        self.time_left = 10
        self.timer_running = False
        self.ao_score = 0
        self.aka_score = 0

        self.theme = {
            "bg": "#121212",
            "fg": "#00ffcc",
            "ao_bg": "#004080",
            "aka_bg": "#800000",
            "timer_bg": "#000000",
            "timer_fg": "#32cd32",
            "btn_bg": "#00ffcc",
            "btn_fg": "#121212",
            "btn_active_bg": "#00cca3",
            "font": ("Poppins", 14, "bold"),
        }

        self.configure(fg_color=self.theme["bg"])
        self.pack(fill="both", expand=True)

        self.outer_frame = ctk.CTkFrame(self, fg_color=self.theme["bg"])
        self.outer_frame.pack(expand=True, fill="both", padx=20, pady=20)

        ctk.CTkLabel(
            self.outer_frame, text="Scoreboard",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=self.theme["fg"], fg_color=self.theme["bg"]
        ).grid(row=0, column=0, columnspan=5, pady=(0, 20))

        ctk.CTkLabel(
            self.outer_frame, text="Team AO:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme["fg"], fg_color=self.theme["bg"]
        ).grid(row=1, column=0, sticky="e", padx=10)
        self.ao_name = ctk.CTkEntry(self.outer_frame, font=ctk.CTkFont(size=14))
        self.ao_name.grid(row=1, column=1, padx=10, sticky="ew")
        self.ao_name.insert(0, "Kisodori Shiho")

        ctk.CTkLabel(
            self.outer_frame, text="Team AKA:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme["fg"], fg_color=self.theme["bg"]
        ).grid(row=1, column=3, sticky="e", padx=10)
        self.aka_name = ctk.CTkEntry(self.outer_frame, font=ctk.CTkFont(size=14))
        self.aka_name.grid(row=1, column=4, padx=10, sticky="ew")
        self.aka_name.insert(0, "Keneth")

        self.outer_frame.grid_columnconfigure(1, weight=1)
        self.outer_frame.grid_columnconfigure(4, weight=1)
        self.outer_frame.grid_rowconfigure(2, weight=1)

        self.ao_frame = ctk.CTkFrame(self.outer_frame, fg_color=self.theme["ao_bg"], corner_radius=12)
        self.ao_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")
        self.ao_score_label = ctk.CTkLabel(
            self.ao_frame, text="0", font=ctk.CTkFont(size=48, weight="bold"),
            text_color="white", fg_color=self.theme["ao_bg"]
        )
        self.ao_score_label.pack(pady=(0, 15), fill="x")
        btn_ao_frame = ctk.CTkFrame(self.ao_frame, fg_color=self.theme["ao_bg"])
        btn_ao_frame.pack()
        ctk.CTkButton(btn_ao_frame, text="+1", width=60, height=40, font=ctk.CTkFont(size=18, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.add_ao).pack(side="left", padx=8)
        ctk.CTkButton(btn_ao_frame, text="-1", width=60, height=40, font=ctk.CTkFont(size=18, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.sub_ao).pack(side="left", padx=8)

        self.aka_frame = ctk.CTkFrame(self.outer_frame, fg_color=self.theme["aka_bg"], corner_radius=12)
        self.aka_frame.grid(row=2, column=3, columnspan=2, pady=10, sticky="nsew")
        self.aka_score_label = ctk.CTkLabel(
            self.aka_frame, text="0", font=ctk.CTkFont(size=48, weight="bold"),
            text_color="white", fg_color=self.theme["aka_bg"]
        )
        self.aka_score_label.pack(pady=(0, 15), fill="x")
        btn_aka_frame = ctk.CTkFrame(self.aka_frame, fg_color=self.theme["aka_bg"])
        btn_aka_frame.pack()
        ctk.CTkButton(btn_aka_frame, text="+1", width=60, height=40, font=ctk.CTkFont(size=18, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.add_aka).pack(side="left", padx=8)
        ctk.CTkButton(btn_aka_frame, text="-1", width=60, height=40, font=ctk.CTkFont(size=18, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.sub_aka).pack(side="left", padx=8)

        self.timer_label = ctk.CTkLabel(
            self.outer_frame, text="0:10", font=ctk.CTkFont(size=36, weight="bold"),
            fg_color=self.theme["timer_bg"], text_color=self.theme["timer_fg"], corner_radius=8, width=220, height=60
        )
        self.timer_label.grid(row=3, column=0, columnspan=5, pady=20, sticky="ew")

        btn_frame = ctk.CTkFrame(self.outer_frame, fg_color=self.theme["bg"])
        btn_frame.grid(row=4, column=0, columnspan=5, pady=(0, 10))
        ctk.CTkButton(btn_frame, text="Start", width=80, height=36, font=ctk.CTkFont(size=14, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.start_timer).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Stop", width=80, height=36, font=ctk.CTkFont(size=14, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.stop_timer).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Reset", width=80, height=36, font=ctk.CTkFont(size=14, weight="bold"),
                      fg_color=self.theme["btn_bg"], text_color=self.theme["btn_fg"], hover_color=self.theme["btn_active_bg"],
                      command=self.reset_timer).pack(side="left", padx=10)

        nav_frame = ctk.CTkFrame(self.outer_frame, fg_color=self.theme["bg"])
        nav_frame.grid(row=5, column=0, columnspan=5, pady=10)
        ctk.CTkButton(nav_frame, text="Back", width=120, height=40, font=ctk.CTkFont(size=16, weight="bold"),
                      fg_color="#b5d0e6", text_color="#0b355d", command=self.back_to_studylog).pack(side="left", padx=10)
        ctk.CTkButton(nav_frame, text="Quit", width=120, height=40, font=ctk.CTkFont(size=16, weight="bold"),
                      fg_color="#d9534f", text_color="white", command=self.quit_app).pack(side="left", padx=10)

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.configure(text=f"{minutes}:{seconds:02d}")
            self.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_running = False
            messagebox.showinfo("Timer", "Time's up!")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.stop_timer()
        self.time_left = 10
        self.timer_label.configure(text="0:10")

    def add_ao(self):
        self.ao_score += 1
        self.ao_score_label.configure(text=str(self.ao_score))

    def sub_ao(self):
        self.ao_score = max(0, self.ao_score - 1)
        self.ao_score_label.configure(text=str(self.ao_score))

    def add_aka(self):
        self.aka_score += 1
        self.aka_score_label.configure(text=str(self.aka_score))

    def sub_aka(self):
        self.aka_score = max(0, self.aka_score - 1)
        self.aka_score_label.configure(text=str(self.aka_score))

    def back_to_studylog(self):
        self.pack_forget()
        if self.controller:
            self.controller.create_welcome_page()

    def quit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ScoreboardApp(root)
    app.mainloop()
