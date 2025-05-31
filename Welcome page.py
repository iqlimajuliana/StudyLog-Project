#==========================kirana========================
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
#==========================rizka==========================

#==========================iqlima=========================

#================================================================maul=========================================================================================
spacer = ctk.CTkFrame(container, fg_color="transparent")
        spacer.pack(expand=True)

        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(pady=(0, 30))

        ctk.CTkButton(btn_frame, text="Start Now", width=120, corner_radius=20).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="See Our Team", width=120, corner_radius=20,
                      command=lambda: self.show_frame("team")).grid(row=0, column=1, padx=10)

    def create_team(self):
        frame = ctk.CTkFrame(self, fg_color="#eef3fc")
        self.frames["team"] = frame

        ctk.CTkLabel(frame, text="OUR TEAM", font=ctk.CTkFont(size=20, weight="bold"), text_color="#6b72c9").pack(pady=(30, 20))

        for member in self.members:
            member_card = ctk.CTkFrame(frame, width=300, height=60, corner_radius=10)
            member_card.pack(pady=5)

            img = Image.open(member.photo_path).resize((35, 35))
            member.icon = ImageTk.PhotoImage(img)
            tk.Label(member_card, image=member.icon, bg="#E1E6F9").pack(side="left", padx=10)

            text = f"{member.name}\n{member.npm}"
            ctk.CTkButton(member_card, text=text, anchor="w", fg_color="#6b72c9",
                          command=lambda m=member.name: self.show_frame(m),
                          width=200, height=50, corner_radius=10).pack(side="left", padx=5)

        ctk.CTkButton(frame, text="Back to Home", width=200, height=40, corner_radius=20,
                      command=lambda: self.show_frame("home")).pack(pady=30)

    def create_member_pages(self):
        for member in self.members:
            self.frames[member.name] = MemberPage(self, member, back_callback=lambda: self.show_frame("team"))


if __name__ == "__main__":
    app = StudyLogApp()
    app.mainloop()
