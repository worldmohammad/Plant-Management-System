import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect('plants.db')
c = conn.cursor()

# ایجاد جدول گیاهان در پایگاه داده
c.execute('''CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY,
                scientific_name TEXT,
                local_name TEXT,
                family TEXT,
                water_need TEXT,
                light_need TEXT,
                soil_type TEXT,
                irrigation_frequency TEXT,
                water_amount REAL,
                irrigation_method TEXT,
                ph_level REAL,
                fertilizer_type TEXT,
                fertilizer_amount REAL,
                light_exposure_duration TEXT
            )''')
conn.commit()

# تابع برای افزودن گیاه جدید
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

    messagebox.showinfo("افزودن گیاه", "گیاه با موفقیت اضافه شد.")
    clear_entries()
    show_plants_in_treeview()

# تابع برای پاک کردن مقادیر ورودی‌ها
def clear_entries():
    entry_scientific_name.delete(0, tk.END)
    entry_local_name.delete(0, tk.END)
    entry_family.delete(0, tk.END)
    entry_water_need.delete(0, tk.END)
    entry_light_need.delete(0, tk.END)
    entry_soil_type.delete(0, tk.END)
    entry_irrigation_frequency.delete(0, tk.END)
    entry_water_amount.delete(0, tk.END)
    entry_irrigation_method.delete(0, tk.END)
    entry_ph_level.delete(0, tk.END)
    entry_fertilizer_type.delete(0, tk.END)
    entry_fertilizer_amount.delete(0, tk.END)
    entry_light_exposure_duration.delete(0, tk.END)

# تابع برای نمایش گیاهان در Treeview
def show_plants_in_treeview(search_text=""):
    # پاک کردن تمام آیتم‌های قبلی در Treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # دریافت تمام گیاهان از پایگاه داده
    c.execute("SELECT * FROM plants")
    rows = c.fetchall()

    # قرار دادن گیاهان در Treeview
    for row in rows:
        if search_text.lower() in " ".join(map(str, row)).lower():
            treeview.insert("", tk.END, values=row)

# تابع برای جستجو
def search_plants(event):
    search_text = entry_search.get()
    show_plants_in_treeview(search_text)

# تابع برای نمایش پنجره افزودن گیاه
def show_add_plant_window():
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

    global entry_scientific_name, entry_local_name, entry_family, entry_water_need
    global entry_light_need, entry_soil_type, entry_irrigation_frequency
    global entry_water_amount, entry_irrigation_method, entry_ph_level
    global entry_fertilizer_type, entry_fertilizer_amount, entry_light_exposure_duration

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

    # دکمه برای افزودن گیاه
    btn_add = tk.Button(add_window, text="افزودن گیاه", command=add_plant)
    btn_add.grid(row=13, column=0, columnspan=2, pady=10)

# تابع برای ویرایش گیاه انتخاب شده
def edit_plant():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("ویرایش گیاه", "لطفاً یک گیاه را انتخاب کنید.")
        return
    
    plant = treeview.item(selected_item)["values"]
    plant_id = plant[0]

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
    entry_local_name_edit = tk.Entry(edit_window, width=30)
    entry_local_name_edit.grid(row=1, column=1, padx=10, pady=5)
    entry_family_edit = tk.Entry(edit_window, width=30)
    entry_family_edit.grid(row=2, column=1, padx=10, pady=5)
    entry_water_need_edit = tk.Entry(edit_window, width=30)
    entry_water_need_edit.grid(row=3, column=1, padx=10, pady=5)
    entry_light_need_edit = tk.Entry(edit_window, width=30)
    entry_light_need_edit.grid(row=4, column=1, padx=10, pady=5)
    entry_soil_type_edit = tk.Entry(edit_window, width=30)
    entry_soil_type_edit.grid(row=5, column=1, padx=10, pady=5)
    entry_irrigation_frequency_edit = tk.Entry(edit_window, width=30)
    entry_irrigation_frequency_edit.grid(row=6, column=1, padx=10, pady=5)
    entry_water_amount_edit = tk.Entry(edit_window, width=30)
    entry_water_amount_edit.grid(row=7, column=1, padx=10, pady=5)
    entry_irrigation_method_edit = tk.Entry(edit_window, width=30)
    entry_irrigation_method_edit.grid(row=8, column=1, padx=10, pady=5)
    entry_ph_level_edit = tk.Entry(edit_window, width=30)
    entry_ph_level_edit.grid(row=9, column=1, padx=10, pady=5)
    entry_fertilizer_type_edit = tk.Entry(edit_window, width=30)
    entry_fertilizer_type_edit.grid(row=10, column=1, padx=10, pady=5)
    entry_fertilizer_amount_edit = tk.Entry(edit_window, width=30)
    entry_fertilizer_amount_edit.grid(row=11, column=1, padx=10, pady=5)
    entry_light_exposure_duration_edit = tk.Entry(edit_window, width=30)
    entry_light_exposure_duration_edit.grid(row=12, column=1, padx=10, pady=5)

    entry_scientific_name_edit.insert(0, plant[1])
    entry_local_name_edit.insert(0, plant[2])
    entry_family_edit.insert(0, plant[3])
    entry_water_need_edit.insert(0, plant[4])
    entry_light_need_edit.insert(0, plant[5])
    entry_soil_type_edit.insert(0, plant[6])
    entry_irrigation_frequency_edit.insert(0, plant[7])
    entry_water_amount_edit.insert(0, plant[8])
    entry_irrigation_method_edit.insert(0, plant[9])
    entry_ph_level_edit.insert(0, plant[10])
    entry_fertilizer_type_edit.insert(0, plant[11])
    entry_fertilizer_amount_edit.insert(0, plant[12])
    entry_light_exposure_duration_edit.insert(0, plant[13])

    def update_plant():
        new_scientific_name = entry_scientific_name_edit.get()
        new_local_name = entry_local_name_edit.get()
        new_family = entry_family_edit.get()
        new_water_need = entry_water_need_edit.get()
        new_light_need = entry_light_need_edit.get()
        new_soil_type = entry_soil_type_edit.get()
        new_irrigation_frequency = entry_irrigation_frequency_edit.get()
        new_water_amount = entry_water_amount_edit.get()
        new_irrigation_method = entry_irrigation_method_edit.get()
        new_ph_level = entry_ph_level_edit.get()
        new_fertilizer_type = entry_fertilizer_type_edit.get()
        new_fertilizer_amount = entry_fertilizer_amount_edit.get()
        new_light_exposure_duration = entry_light_exposure_duration_edit.get()

        c.execute('''
                  UPDATE plants
                  SET scientific_name=?, local_name=?, family=?, water_need=?, light_need=?, soil_type=?,
                      irrigation_frequency=?, water_amount=?, irrigation_method=?, ph_level=?,
                      fertilizer_type=?, fertilizer_amount=?, light_exposure_duration=?
                  WHERE id=?
                  ''',
                  (new_scientific_name, new_local_name, new_family, new_water_need, new_light_need, new_soil_type,
                   new_irrigation_frequency, new_water_amount, new_irrigation_method, new_ph_level,
                   new_fertilizer_type, new_fertilizer_amount, new_light_exposure_duration, plant_id))
        conn.commit()

        messagebox.showinfo("ویرایش گیاه", "گیاه با موفقیت به‌روزرسانی شد.")
        show_plants_in_treeview()
        edit_window.destroy()

    btn_update = tk.Button(edit_window, text="به‌روزرسانی گیاه", command=update_plant)
    btn_update.grid(row=13, column=0, columnspan=2, pady=10)

# تابع برای حذف گیاه انتخاب شده
def delete_plant():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("حذف گیاه", "لطفاً یک گیاه را انتخاب کنید.")
        return
    
    plant = treeview.item(selected_item)["values"]
    plant_id = plant[0]

    response = messagebox.askyesno("حذف گیاه", f"آیا مطمئنید که می خواهید گیاه {plant[1]} را حذف کنید؟")
    if response == 1:
        c.execute("DELETE FROM plants WHERE id=?", (plant_id,))
        conn.commit()
        messagebox.showinfo("حذف گیاه", f"گیاه {plant[1]} با موفقیت حذف شد.")
        show_plants_in_treeview()

# تابع برای ایجاد و نمایش پنجره اصلی
def main_window():
    global root, treeview, entry_search

    root = tk.Tk()
    root.title("سیستم مدیریت گیاهان")

    # تنظیم اندازه پنجره اصلی
    root.geometry("600x600")

    # دکمه افزودن گیاه جدید
    btn_add_plant = tk.Button(root, text="افزودن گیاه جدید", command=show_add_plant_window)
    btn_add_plant.pack(pady=10)

    # جستجو
    tk.Label(root, text="جستجو:").pack()
    entry_search = tk.Entry(root, width=30)
    entry_search.pack()
    entry_search.bind("<KeyRelease>", search_plants)

    # ساخت Treeview برای نمایش گیاهان
    columns = ("id", "scientific_name", "local_name", "family", "water_need", "light_need", "soil_type",
               "irrigation_frequency", "water_amount", "irrigation_method", "ph_level",
               "fertilizer_type", "fertilizer_amount", "light_exposure_duration")
    
    treeview = ttk.Treeview(root, columns=columns, show="headings")
    treeview.pack(expand=True, fill="both")

    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=100)

    # اضافه کردن اسکرولبار به Treeview
    scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=treeview.xview)
    treeview.configure(xscrollcommand=scrollbar_x.set)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # دکمه‌های ویرایش و حذف
    btn_edit = tk.Button(root, text="ویرایش گیاه", command=edit_plant)
    btn_edit.pack(side=tk.LEFT, padx=10, pady=10)

    btn_delete = tk.Button(root, text="حذف گیاه", command=delete_plant)
    btn_delete.pack(side=tk.LEFT, padx=10, pady=10)

    show_plants_in_treeview()
    root.mainloop()

if __name__ == "__main__":
    main_window()
