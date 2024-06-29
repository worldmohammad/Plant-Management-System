import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# اتصال به دیتابیس SQLite
conn = sqlite3.connect('plants.db')
c = conn.cursor()

# ایجاد جدول برای نگهداری اطلاعات گیاهان در صورت عدم وجود
c.execute('''
          CREATE TABLE IF NOT EXISTS plants
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          scientific_name TEXT,
          local_name TEXT,
          family TEXT,
          water_need TEXT,
          light_need TEXT,
          soil_type TEXT,
          irrigation_frequency TEXT,
          water_amount TEXT,
          irrigation_method TEXT,
          ph_level TEXT,
          fertilizer_type TEXT,
          fertilizer_amount TEXT,
          light_exposure_duration TEXT)
          ''')

# تابع افزودن گیاه جدید
def add_plant():
    scientific_name = entry_scientific_name.get()
    local_name = entry_local_name.get()
    family = entry_family.get()
    water_need = entry_water_need.get()
    light_need = entry_light_need.get()
    soil_type = entry_soil_type.get()
    irrigation_frequency = entry_irrigation_frequency.get()
    water_amount = entry_water_amount.get()
    irrigation_method = entry_irrigation_method.get()
    ph_level = entry_ph_level.get()
    fertilizer_type = entry_fertilizer_type.get()
    fertilizer_amount = entry_fertilizer_amount.get()
    light_exposure_duration = entry_light_exposure_duration.get()

    c.execute('''
              INSERT INTO plants (scientific_name, local_name, family, water_need, light_need, soil_type,
                                  irrigation_frequency, water_amount, irrigation_method, ph_level,
                                  fertilizer_type, fertilizer_amount, light_exposure_duration)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''',
              (scientific_name, local_name, family, water_need, light_need, soil_type,
               irrigation_frequency, water_amount, irrigation_method, ph_level,
               fertilizer_type, fertilizer_amount, light_exposure_duration))
    conn.commit()
    messagebox.showinfo("افزودن گیاه", "گیاه با موفقیت افزوده شد.")
    show_plants_in_treeview()
    add_window.destroy()

# تابع نمایش پنجره افزودن گیاه جدید
def show_add_plant_window():
    global add_window, entry_scientific_name, entry_local_name, entry_family, entry_water_need, entry_light_need
    global entry_soil_type, entry_irrigation_frequency, entry_water_amount, entry_irrigation_method
    global entry_ph_level, entry_fertilizer_type, entry_fertilizer_amount, entry_light_exposure_duration

    add_window = tk.Toplevel(root)
    add_window.title("افزودن گیاه جدید")

    # Labels and Entries for plant information
    tk.Label(add_window, text="نام علمی:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نام محلی:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="خانواده گیاه:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نیاز به آب:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نیاز به نور:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع خاک:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(add_window, text="فرکانس آبیاری:").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مقدار آب مورد نیاز به لیتر:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نحوه آبیاری:").grid(row=8, column=0, padx=10, pady=5)
    tk.Label(add_window, text="میزان pH خاک:").grid(row=9, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع کود:").grid(row=10, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مقدار کود:").grid(row=11, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مدت زمان تابش نور:").grid(row=12, column=0, padx=10, pady=5)

    entry_scientific_name = tk.Entry(add_window, width=30)
    entry_scientific_name.grid(row=0, column=1, padx=10, pady=5)
    entry_local_name = tk.Entry(add_window, width=30)
    entry_local_name.grid(row=1, column=1, padx=10, pady=5)
    entry_family = tk.Entry(add_window, width=30)
    entry_family.grid(row=2, column=1, padx=10, pady=5)
    entry_water_need = tk.Entry(add_window, width=30)
    entry_water_need.grid(row=3, column=1, padx=10, pady=5)
    entry_light_need = tk.Entry(add_window, width=30)
    entry_light_need.grid(row=4, column=1, padx=10, pady=5)
    entry_soil_type = tk.Entry(add_window, width=30)
    entry_soil_type.grid(row=5, column=1, padx=10, pady=5)
    entry_irrigation_frequency = tk.Entry(add_window, width=30)
    entry_irrigation_frequency.grid(row=6, column=1, padx=10, pady=5)
    entry_water_amount = tk.Entry(add_window, width=30)
    entry_water_amount.grid(row=7, column=1, padx=10, pady=5)
    entry_irrigation_method = tk.Entry(add_window, width=30)
    entry_irrigation_method.grid(row=8, column=1, padx=10, pady=5)
    entry_ph_level = tk.Entry(add_window, width=30)
    entry_ph_level.grid(row=9, column=1, padx=10, pady=5)
    entry_fertilizer_type = tk.Entry(add_window, width=30)
    entry_fertilizer_type.grid(row=10, column=1, padx=10, pady=5)
    entry_fertilizer_amount = tk.Entry(add_window, width=30)
    entry_fertilizer_amount.grid(row=11, column=1, padx=10, pady=5)
    entry_light_exposure_duration = tk.Entry(add_window, width=30)
    entry_light_exposure_duration.grid(row=12, column=1, padx=10, pady=5)

    btn_add = tk.Button(add_window, text="افزودن گیاه", command=add_plant)
    btn_add.grid(row=13, column=0, columnspan=2, pady=10)

# تابع جستجوی گیاهان
def search_plants(event):
    search_term = entry_search.get()
    query = "SELECT * FROM plants WHERE scientific_name LIKE ? OR local_name LIKE ?"
    c.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
    plants = c.fetchall()
    update_treeview(plants)

# تابع به‌روزرسانی Treeview
def update_treeview(plants):
    for item in treeview.get_children():
        treeview.delete(item)
    for plant in plants:
        treeview.insert('', 'end', values=plant)

# تابع نمایش گیاهان در Treeview
def show_plants_in_treeview():
    c.execute("SELECT * FROM plants")
    plants = c.fetchall()
    update_treeview(plants)

# تابع ویرایش گیاه انتخاب شده
def edit_plant():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("ویرایش گیاه", "لطفاً یک گیاه را انتخاب کنید.")
        return
    
    plant = treeview.item(selected_item)["values"]
    plant_id = plant[0]

    global edit_window, entry_scientific_name_edit, entry_local_name_edit, entry_family_edit, entry_water_need_edit
    global entry_light_need_edit, entry_soil_type_edit, entry_irrigation_frequency_edit, entry_water_amount_edit
    global entry_irrigation_method_edit, entry_ph_level_edit, entry_fertilizer_type_edit, entry_fertilizer_amount_edit
    global entry_light_exposure_duration_edit

    edit_window = tk.Toplevel(root)
    edit_window.title("ویرایش گیاه")

    # Labels and Entries for plant information
    tk.Label(edit_window, text="نام علمی:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نام محلی:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="خانواده گیاه:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نیاز به آب:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نیاز به نور:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نوع خاک:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="فرکانس آبیاری:").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مقدار آب مورد نیاز به لیتر:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نحوه آبیاری:").grid(row=8, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="میزان pH خاک:").grid(row=9, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نوع کود:").grid(row=10, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مقدار کود:").grid(row=11, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مدت زمان تابش نور:").grid(row=12, column=0, padx=10, pady=5)

    entry_scientific_name_edit = tk.Entry(edit_window, width=30)
    entry_scientific_name_edit.grid(row=0, column=1, padx=10, pady=5)
    entry_scientific_name_edit.insert(0, plant[1])
    entry_local_name_edit = tk.Entry(edit_window, width=30)
    entry_local_name_edit.grid(row=1, column=1, padx=10, pady=5)
    entry_local_name_edit.insert(0, plant[2])
    entry_family_edit = tk.Entry(edit_window, width=30)
    entry_family_edit.grid(row=2, column=1, padx=10, pady=5)
    entry_family_edit.insert(0, plant[3])
    entry_water_need_edit = tk.Entry(edit_window, width=30)
    entry_water_need_edit.grid(row=3, column=1, padx=10, pady=5)
    entry_water_need_edit.insert(0, plant[4])
    entry_light_need_edit = tk.Entry(edit_window, width=30)
    entry_light_need_edit.grid(row=4, column=1, padx=10, pady=5)
    entry_light_need_edit.insert(0, plant[5])
    entry_soil_type_edit = tk.Entry(edit_window, width=30)
    entry_soil_type_edit.grid(row=5, column=1, padx=10, pady=5)
    entry_soil_type_edit.insert(0, plant[6])
    entry_irrigation_frequency_edit = tk.Entry(edit_window, width=30)
    entry_irrigation_frequency_edit.grid(row=6, column=1, padx=10, pady=5)
    entry_irrigation_frequency_edit.insert(0, plant[7])
    entry_water_amount_edit = tk.Entry(edit_window, width=30)
    entry_water_amount_edit.grid(row=7, column=1, padx=10, pady=5)
    entry_water_amount_edit.insert(0, plant[8])
    entry_irrigation_method_edit = tk.Entry(edit_window, width=30)
    entry_irrigation_method_edit.grid(row=8, column=1, padx=10, pady=5)
    entry_irrigation_method_edit.insert(0, plant[9])
    entry_ph_level_edit = tk.Entry(edit_window, width=30)
    entry_ph_level_edit.grid(row=9, column=1, padx=10, pady=5)
    entry_ph_level_edit.insert(0, plant[10])
    entry_fertilizer_type_edit = tk.Entry(edit_window, width=30)
    entry_fertilizer_type_edit.grid(row=10, column=1, padx=10, pady=5)
    entry_fertilizer_type_edit.insert(0, plant[11])
    entry_fertilizer_amount_edit = tk.Entry(edit_window, width=30)
    entry_fertilizer_amount_edit.grid(row=11, column=1, padx=10, pady=5)
    entry_fertilizer_amount_edit.insert(0, plant[12])
    entry_light_exposure_duration_edit = tk.Entry(edit_window, width=30)
    entry_light_exposure_duration_edit.grid(row=12, column=1, padx=10, pady=5)
    entry_light_exposure_duration_edit.insert(0, plant[13])

    btn_save_edit = tk.Button(edit_window, text="ذخیره تغییرات", command=lambda: save_edit(plant_id))
    btn_save_edit.grid(row=13, column=0, columnspan=2, pady=10)

# تابع ذخیره تغییرات ویرایش
def save_edit(plant_id):
    scientific_name = entry_scientific_name_edit.get()
    local_name = entry_local_name_edit.get()
    family = entry_family_edit.get()
    water_need = entry_water_need_edit.get()
    light_need = entry_light_need_edit.get()
    soil_type = entry_soil_type_edit.get()
    irrigation_frequency = entry_irrigation_frequency_edit.get()
    water_amount = entry_water_amount_edit.get()
    irrigation_method = entry_irrigation_method_edit.get()
    ph_level = entry_ph_level_edit.get()
    fertilizer_type = entry_fertilizer_type_edit.get()
    fertilizer_amount = entry_fertilizer_amount_edit.get()
    light_exposure_duration = entry_light_exposure_duration_edit.get()

    c.execute('''
              UPDATE plants
              SET scientific_name = ?, local_name = ?, family = ?, water_need = ?, light_need = ?, soil_type = ?,
                  irrigation_frequency = ?, water_amount = ?, irrigation_method = ?, ph_level = ?,
                  fertilizer_type = ?, fertilizer_amount = ?, light_exposure_duration = ?
              WHERE id = ?
              ''',
              (scientific_name, local_name, family, water_need, light_need, soil_type,
               irrigation_frequency, water_amount, irrigation_method, ph_level,
               fertilizer_type, fertilizer_amount, light_exposure_duration, plant_id))
    conn.commit()
    messagebox.showinfo("ویرایش گیاه", "تغییرات با موفقیت ذخیره شد.")
    show_plants_in_treeview()
    edit_window.destroy()

# تابع حذف گیاه انتخاب شده
def delete_plant():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("حذف گیاه", "لطفاً یک گیاه را انتخاب کنید.")
        return

    plant = treeview.item(selected_item)["values"]
    plant_id = plant[0]

    c.execute("DELETE FROM plants WHERE id = ?", (plant_id,))
    conn.commit()
    messagebox.showinfo("حذف گیاه", "گیاه با موفقیت حذف شد.")
    show_plants_in_treeview()

# تابع اصلی برای ایجاد رابط کاربری
def main_window():
    global root, treeview, entry_search

    root = tk.Tk()
    root.title("مدیریت و نگهداری گیاهان")
    root.geometry("600x600")

    # کادر جستجو
    tk.Label(root, text="جستجو:").pack(pady=10)
    entry_search = tk.Entry(root, width=50)
    entry_search.pack()
    entry_search.bind("<KeyRelease>", search_plants)

    # Treeview برای نمایش گیاهان
    columns = ("id", "scientific_name", "local_name", "family", "water_need", "light_need", "soil_type",
               "irrigation_frequency", "water_amount", "irrigation_method", "ph_level", "fertilizer_type",
               "fertilizer_amount", "light_exposure_duration")
    treeview = ttk.Treeview(root, columns=columns, show="headings", height=15)

    treeview.heading("id", text="شناسه")
    treeview.heading("scientific_name", text="نام علمی")
    treeview.heading("local_name", text="نام محلی")
    treeview.heading("family", text="خانواده")
    treeview.heading("water_need", text="نیاز آبی")
    treeview.heading("light_need", text="نیاز نوری")
    treeview.heading("soil_type", text="نوع خاک")
    treeview.heading("irrigation_frequency", text="فرکانس آبیاری")
    treeview.heading("water_amount", text="مقدار آب")
    treeview.heading("irrigation_method", text="نحوه آبیاری")
    treeview.heading("ph_level", text="میزان pH")
    treeview.heading("fertilizer_type", text="نوع کود")
    treeview.heading("fertilizer_amount", text="مقدار کود")
    treeview.heading("light_exposure_duration", text="مدت زمان تابش نور")

    # Scrollbars
    scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=treeview.xview)
    treeview.configure(xscrollcommand=scrollbar_x.set)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    treeview.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

    # دکمه‌های ویرایش و حذف
    btn_add_plant = tk.Button(root, text="افزودن گیاه جدید", command=show_add_plant_window)
    btn_add_plant.pack(side=tk.LEFT, padx=10, pady=10)

    btn_edit = tk.Button(root, text="ویرایش گیاه", command=edit_plant)
    btn_edit.pack(side=tk.LEFT, padx=10, pady=10)

    btn_delete = tk.Button(root, text="حذف گیاه", command=delete_plant)
    btn_delete.pack(side=tk.LEFT, padx=10, pady=10)

    show_plants_in_treeview()
    root.mainloop()

if __name__ == "__main__":
    main_window()
