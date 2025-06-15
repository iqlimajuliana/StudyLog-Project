import csv
import os
from datetime import datetime

MATA_KULIAH = [
    "Pengantar Organisasi Komputer",
    "Struktur Data dan Algoritma",
    "Pemrograman Terstruktur",
    "Sistem Operasi",
    "Pendidikan Kewarga Negaraan",
    "Bahasa Indonesia",
    "Pengantar Sistem Informasi",
    "Matematika Diskrit"
]

JADWAL_MATKUL = {
    "Senin": [
        "Pengantar Organisasi Komputer",
        "Pemrograman Terstruktur",
        "Matematika Diskrit"
    ],
    "Selasa": [
        "Pendidikan Kewarga Negaraan"
    ],
    "Rabu": [
        "Struktur Data dan Algoritma"
    ],
    "Kamis": [
        "Pengantar Sistem Informasi",
        "Sistem Operasi"
    ],
    "Jumat": [
        "Bahasa Indonesia"
    ]
}

absensi_file = 'absensi.csv'
user_file = 'user.csv'

def init_csv_files():
    if not os.path.exists(absensi_file):
        with open(absensi_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nama", "NPM", "Mata Kuliah", "Hari", "Jam", "Tanggal", "Status"])

    if not os.path.exists(user_file):
        with open(user_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nama", "NPM", "Password"])

def verify_or_register_user(nama, npm, password):
    with open(user_file, 'a+', newline='') as f:
        f.seek(0)
        reader = csv.reader(f)
        for row in reader:
            if row == [nama, npm, password]:
                return True
        writer = csv.writer(f)
        writer.writerow([nama, npm, password])
        return True

def save_absen(nama, npm, matkul, hari, jam, tanggal, status):
    try:
        tgl_obj = datetime.strptime(tanggal, "%d/%m/%Y")
        tanggal = tgl_obj.strftime("%d/%m/%Y")
    except ValueError:
        pass  
    with open(absensi_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nama, npm, matkul, hari, jam, tanggal, status])
    sort_absensi_csv()

def get_absen_summary(nama, npm):
    count = {mk: 0 for mk in MATA_KULIAH}
    total = {mk: 16 for mk in MATA_KULIAH}

    with open(absensi_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Nama'] == nama and row['NPM'] == npm and row['Status'] == "Hadir":
                count[row['Mata Kuliah']] += 1

    return count, total

def is_already_absent(nama, npm, matkul, tanggal):
    with open(absensi_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (
                row['Nama'] == nama and
                row['NPM'] == npm and
                row['Mata Kuliah'] == matkul and
                row['Tanggal'] == tanggal
            ):
                return True
    return False

def get_hari_from_tanggal(tanggal):
    try:
        tgl_obj = datetime.strptime(tanggal, "%d/%m/%Y")
        hari_map = {
            "Monday": "Senin",
            "Tuesday": "Selasa",
            "Wednesday": "Rabu",
            "Thursday": "Kamis",
            "Friday": "Jumat",
            "Saturday": "Sabtu",
            "Sunday": "Minggu"
        }
        hari_inggris = tgl_obj.strftime("%A")
        return hari_map.get(hari_inggris, "")
    except Exception:
        return ""

def get_matkul_from_hari(hari):
   
    return JADWAL_MATKUL.get(hari, [])

def sort_absensi_csv():
    with open(absensi_file, 'r', newline='') as f:
        reader = list(csv.DictReader(f))
        sorted_rows = sorted(
            reader,
            key=lambda x: (
                datetime.strptime(x['Tanggal'], "%d/%m/%Y"),
                x['Mata Kuliah']
            )
        )

    
    with open(absensi_file, 'w', newline='') as f:
        fieldnames = ["Nama", "NPM", "Mata Kuliah", "Hari", "Jam", "Tanggal", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)
