import tkinter as tk
from tkinter import ttk, messagebox

# اتصال به پایگاه داده SQLite
import sqlite3

conn = sqlite3.connect('plants.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS plants (
          id INTEGER PRIMARY KEY,
          scientific_name TEXT,
          local_name TEXT,
          family TEXT,
          temperature_need TEXT,
          light_need TEXT,
          soil_type TEXT,
          irrigation_frequency TEXT,
          water_amount TEXT,
          irrigation_method TEXT,
          ph_level TEXT,
          fertilizer_type TEXT,
          fertilizer_amount TEXT,
          light_exposure_duration TEXT,
          humidity TEXT,
          solution_composition TEXT,
          light_type TEXT)
          ''')
conn.commit()

# تابع افزودن گیاه جدید
def add_plant():
    scientific_name = entry_scientific_name.get()
    local_name = entry_local_name.get()
    family = entry_family.get()
    temperature_need = entry_temperature_need.get()
    light_need = entry_light_need.get()
    soil_type = entry_soil_type.get()
    irrigation_frequency = entry_irrigation_frequency.get()
    water_amount = entry_water_amount.get()
    irrigation_method = entry_irrigation_method.get()
    ph_level = entry_ph_level.get()
    fertilizer_type = entry_fertilizer_type.get()
    fertilizer_amount = entry_fertilizer_amount.get()
    light_exposure_duration = entry_light_exposure_duration.get()
    humidity = entry_humidity.get()
    solution_composition = entry_solution_composition.get()
    light_type = entry_light_type.get()

    c.execute('''
              INSERT INTO plants (scientific_name, local_name, family, temperature_need, light_need, soil_type,
                                  irrigation_frequency, water_amount, irrigation_method, ph_level, fertilizer_type,
                                  fertilizer_amount, light_exposure_duration, humidity, solution_composition, light_type)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''',
              (scientific_name, local_name, family, temperature_need, light_need, soil_type, irrigation_frequency,
               water_amount, irrigation_method, ph_level, fertilizer_type, fertilizer_amount,
               light_exposure_duration, humidity, solution_composition, light_type))
    conn.commit()
    messagebox.showinfo("افزودن گیاه", "گیاه با موفقیت اضافه شد.")
    show_plants_in_treeview()
    add_window.destroy()

# تابع نمایش فرم افزودن گیاه جدید
def show_add_plant_window():
    global add_window, entry_scientific_name, entry_local_name, entry_family, entry_temperature_need, entry_light_need
    global entry_soil_type, entry_irrigation_frequency, entry_water_amount, entry_irrigation_method, entry_ph_level
    global entry_fertilizer_type, entry_fertilizer_amount, entry_light_exposure_duration, entry_humidity
    global entry_solution_composition, entry_light_type, entry_disease_type, entry_prevention_method, entry_treatment_method

    add_window = tk.Toplevel(root)
    add_window.title("افزودن گیاه جدید")

    tk.Label(add_window, text="نام علمی:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نام محلی:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="خانواده:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="دمای مورد نیاز:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نیاز نوری:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع خاک:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(add_window, text="فرکانس آبیاری:").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مقدار آب مورد نیاز به لیتر:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نحوه آبیاری:").grid(row=8, column=0, padx=10, pady=5)
    tk.Label(add_window, text="میزان pH خاک:").grid(row=9, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع کود:").grid(row=10, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مقدار کود:").grid(row=11, column=0, padx=10, pady=5)
    tk.Label(add_window, text="مدت زمان تابش نور:").grid(row=12, column=0, padx=10, pady=5)
    tk.Label(add_window, text="میزان رطوبت:").grid(row=13, column=0, padx=10, pady=5)
    tk.Label(add_window, text="ترکیب محلول غذایی:").grid(row=14, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع تابش نور:").grid(row=15, column=0, padx=10, pady=5)
    tk.Label(add_window, text="نوع بیماری:").grid(row=16, column=0, padx=10, pady=5)
    tk.Label(add_window, text="روش پیشگیری:").grid(row=17, column=0, padx=10, pady=5)
    tk.Label(add_window, text="روش درمان:").grid(row=18, column=0, padx=10, pady=5)

    entry_scientific_name = tk.Entry(add_window, width=30)
    entry_scientific_name.grid(row=0, column=1, padx=10, pady=5)
    entry_local_name = tk.Entry(add_window, width=30)
    entry_local_name.grid(row=1, column=1, padx=10, pady=5)
    entry_family = tk.Entry(add_window, width=30)
    entry_family.grid(row=2, column=1, padx=10, pady=5)
    entry_temperature_need = tk.Entry(add_window, width=30)
    entry_temperature_need.grid(row=3, column=1, padx=10, pady=5)
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
    entry_humidity = tk.Entry(add_window, width=30)
    entry_humidity.grid(row=13, column=1, padx=10, pady=5)
    entry_solution_composition = tk.Entry(add_window, width=30)
    entry_solution_composition.grid(row=14, column=1, padx=10, pady=5)
    entry_light_type = ttk.Combobox(add_window, values=["مستقیم", "غیرمستقیم"], width=28)
    entry_light_type.grid(row=15, column=1, padx=10, pady=5)
    entry_disease_type = tk.Entry(add_window, width=30)
    entry_disease_type.grid(row=16, column=1, padx=10, pady=5)
    entry_prevention_method = tk.Entry(add_window, width=30)
    entry_prevention_method.grid(row=17, column=1, padx=10, pady=5)
    entry_treatment_method = tk.Entry(add_window, width=30)
    entry_treatment_method.grid(row=18, column=1, padx=10, pady=5)

    btn_save = tk.Button(add_window, text="ذخیره", command=add_plant)
    btn_save.grid(row=19, column=0, columnspan=2, pady=10)

    # اضافه کردن منوی راست کلیک برای کپی، کات و پیست
    def add_context_menu(entry_widget):
        def copy_text():
            entry_widget.event_generate("<<Copy>>")

        def cut_text():
            entry_widget.event_generate("<<Cut>>")

        def paste_text():
            entry_widget.event_generate("<<Paste>>")

        context_menu = tk.Menu(entry_widget, tearoff=0)
        context_menu.add_command(label="کپی", command=copy_text)
        context_menu.add_command(label="برش", command=cut_text)
        context_menu.add_command(label="چسباندن", command=paste_text)

        def show_context_menu(event):
            context_menu.post(event.x_root, event.y_root)

        entry_widget.bind("<Button-3>", show_context_menu)

    for widget in [entry_scientific_name, entry_local_name, entry_family, entry_temperature_need, entry_light_need,
                   entry_soil_type, entry_irrigation_frequency, entry_water_amount, entry_irrigation_method,
                   entry_ph_level, entry_fertilizer_type, entry_fertilizer_amount, entry_light_exposure_duration,
                   entry_humidity, entry_solution_composition, entry_light_type, entry_disease_type,
                   entry_prevention_method, entry_treatment_method]:
        add_context_menu(widget)
        
# تابع نمایش گیاهان در Treeview
def show_plants_in_treeview():
    for i in tree.get_children():
        tree.delete(i)
    c.execute("SELECT * FROM plants")
    for row in c.fetchall():
        tree.insert("", "end", values=row)

# تابع ویرایش گیاه
def edit_plant():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("ویرایش گیاه", "لطفاً یک گیاه را برای ویرایش انتخاب کنید.")
        return
    item = tree.item(selected_item)
    plant_id = item['values'][0]

    def save_edited_plant():
        scientific_name = entry_scientific_name.get()
        local_name = entry_local_name.get()
        family = entry_family.get()
        temperature_need = entry_temperature_need.get()
        light_need = entry_light_need.get()
        soil_type = entry_soil_type.get()
        irrigation_frequency = entry_irrigation_frequency.get()
        water_amount = entry_water_amount.get()
        irrigation_method = entry_irrigation_method.get()
        ph_level = entry_ph_level.get()
        fertilizer_type = entry_fertilizer_type.get()
        fertilizer_amount = entry_fertilizer_amount.get()
        light_exposure_duration = entry_light_exposure_duration.get()
        humidity = entry_humidity.get()
        solution_composition = entry_solution_composition.get()
        light_type = entry_light_type.get()

        c.execute('''
                  UPDATE plants SET scientific_name=?, local_name=?, family=?, temperature_need=?, light_need=?,
                                   soil_type=?, irrigation_frequency=?, water_amount=?, irrigation_method=?,
                                   ph_level=?, fertilizer_type=?, fertilizer_amount=?, light_exposure_duration=?,
                                   humidity=?, solution_composition=?, light_type=? WHERE id=?
                  ''',
                  (scientific_name, local_name, family, temperature_need, light_need, soil_type, irrigation_frequency,
                   water_amount, irrigation_method, ph_level, fertilizer_type, fertilizer_amount,
                   light_exposure_duration, humidity, solution_composition, light_type, plant_id))
        conn.commit()
        messagebox.showinfo("ویرایش گیاه", "گیاه با موفقیت ویرایش شد.")
        show_plants_in_treeview()
        edit_window.destroy()

    edit_window = tk.Toplevel(root)
    edit_window.title("ویرایش گیاه")

    tk.Label(edit_window, text="نام علمی:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نام محلی:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="خانواده:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="دمای مورد نیاز:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نیاز نوری:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نوع خاک:").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="فرکانس آبیاری:").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مقدار آب مورد نیاز به لیتر:").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نحوه آبیاری:").grid(row=8, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="میزان pH خاک:").grid(row=9, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نوع کود:").grid(row=10, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مقدار کود:").grid(row=11, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="مدت زمان تابش نور:").grid(row=12, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="میزان رطوبت:").grid(row=13, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="ترکیب محلول غذایی:").grid(row=14, column=0, padx=10, pady=5)
    tk.Label(edit_window, text="نوع تابش نور:").grid(row=15, column=0, padx=10, pady=5)

    entry_scientific_name = tk.Entry(edit_window, width=30)
    entry_scientific_name.grid(row=0, column=1, padx=10, pady=5)
    entry_scientific_name.insert(0, item['values'][1])
    entry_local_name = tk.Entry(edit_window, width=30)
    entry_local_name.grid(row=1, column=1, padx=10, pady=5)
    entry_local_name.insert(0, item['values'][2])
    entry_family = tk.Entry(edit_window, width=30)
    entry_family.grid(row=2, column=1, padx=10, pady=5)
    entry_family.insert(0, item['values'][3])
    entry_temperature_need = tk.Entry(edit_window, width=30)
    entry_temperature_need.grid(row=3, column=1, padx=10, pady=5)
    entry_temperature_need.insert(0, item['values'][4])
    entry_light_need = tk.Entry(edit_window, width=30)
    entry_light_need.grid(row=4, column=1, padx=10, pady=5)
    entry_light_need.insert(0, item['values'][5])
    entry_soil_type = tk.Entry(edit_window, width=30)
    entry_soil_type.grid(row=5, column=1, padx=10, pady=5)
    entry_soil_type.insert(0, item['values'][6])
    entry_irrigation_frequency = tk.Entry(edit_window, width=30)
    entry_irrigation_frequency.grid(row=6, column=1, padx=10, pady=5)
    entry_irrigation_frequency.insert(0, item['values'][7])
    entry_water_amount = tk.Entry(edit_window, width=30)
    entry_water_amount.grid(row=7, column=1, padx=10, pady=5)
    entry_water_amount.insert(0, item['values'][8])
    entry_irrigation_method = tk.Entry(edit_window, width=30)
    entry_irrigation_method.grid(row=8, column=1, padx=10, pady=5)
    entry_irrigation_method.insert(0, item['values'][9])
    entry_ph_level = tk.Entry(edit_window, width=30)
    entry_ph_level.grid(row=9, column=1, padx=10, pady=5)
    entry_ph_level.insert(0, item['values'][10])
    entry_fertilizer_type = tk.Entry(edit_window, width=30)
    entry_fertilizer_type.grid(row=10, column=1, padx=10, pady=5)
    entry_fertilizer_type.insert(0, item['values'][11])
    entry_fertilizer_amount = tk.Entry(edit_window, width=30)
    entry_fertilizer_amount.grid(row=11, column=1, padx=10, pady=5)
    entry_fertilizer_amount.insert(0, item['values'][12])
    entry_light_exposure_duration = tk.Entry(edit_window, width=30)
    entry_light_exposure_duration.grid(row=12, column=1, padx=10, pady=5)
    entry_light_exposure_duration.insert(0, item['values'][13])
    entry_humidity = tk.Entry(edit_window, width=30)
    entry_humidity.grid(row=13, column=1, padx=10, pady=5)
    entry_humidity.insert(0, item['values'][14])
    entry_solution_composition = tk.Entry(edit_window, width=30)
    entry_solution_composition.grid(row=14, column=1, padx=10, pady=5)
    entry_solution_composition.insert(0, item['values'][15])
    entry_light_type = ttk.Combobox(edit_window, values=["مستقیم", "غیرمستقیم"], width=28)
    entry_light_type.grid(row=15, column=1, padx=10, pady=5)
    entry_light_type.set(item['values'][16])

    btn_save = tk.Button(edit_window, text="ذخیره", command=save_edited_plant)
    btn_save.grid(row=16, column=0, columnspan=2, pady=10)

    # اضافه کردن منوی راست کلیک برای کپی، کات و پیست
    for widget in [entry_scientific_name, entry_local_name, entry_family, entry_temperature_need, entry_light_need,
                   entry_soil_type, entry_irrigation_frequency, entry_water_amount, entry_irrigation_method,
                   entry_ph_level, entry_fertilizer_type, entry_fertilizer_amount, entry_light_exposure_duration,
                   entry_humidity, entry_solution_composition, entry_light_type]:
        add_context_menu(widget)

# تابع حذف گیاه
def delete_plant():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("حذف گیاه", "لطفاً یک گیاه را برای حذف انتخاب کنید.")
        return
    item = tree.item(selected_item)
    plant_id = item['values'][0]

    c.execute("DELETE FROM plants WHERE id=?", (plant_id,))
    conn.commit()
    messagebox.showinfo("حذف گیاه", "گیاه با موفقیت حذف شد.")
    show_plants_in_treeview()

# تابع جستجو و نمایش نتایج در Treeview
def search_plant(event):
    search_term = entry_search.get()
    for i in tree.get_children():
        tree.delete(i)
    c.execute("SELECT * FROM plants WHERE scientific_name LIKE ? OR local_name LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    for row in c.fetchall():
        tree.insert("", "end", values=row)

# ساخت رابط کاربری اصلی
def main_window():
    global root, tree, entry_search

    root = tk.Tk()
    root.title("سیستم مدیریت گیاهان")
    root.geometry("600x600")

    # ساخت فیلد جستجو
    tk.Label(root, text="جستجو:").pack(pady=5)
    entry_search = tk.Entry(root, width=50)
    entry_search.pack(pady=5)
    entry_search.bind("<KeyRelease>", search_plant)

    # ساخت دکمه افزودن گیاه جدید
    btn_add_plant = tk.Button(root, text="افزودن گیاه جدید", command=show_add_plant_window)
    btn_add_plant.pack(pady=10)

    # ساخت Treeview برای نمایش گیاهان ثبت شده
    columns = ("id", "scientific_name", "local_name", "family", "temperature_need", "light_need", "soil_type",
               "irrigation_frequency", "water_amount", "irrigation_method", "ph_level", "fertilizer_type",
               "fertilizer_amount", "light_exposure_duration", "humidity", "solution_composition", "light_type")

    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
    tree.pack(pady=20, padx=10, fill='both', expand=True)

    # تنظیم نام ستون‌ها
    tree.heading("id", text="شناسه")
    tree.heading("scientific_name", text="نام علمی")
    tree.heading("local_name", text="نام محلی")
    tree.heading("family", text="خانواده")
    tree.heading("temperature_need", text="دمای مورد نیاز")
    tree.heading("light_need", text="نیاز نوری")
    tree.heading("soil_type", text="نوع خاک")
    tree.heading("irrigation_frequency", text="فرکانس آبیاری")
    tree.heading("water_amount", text="مقدار آب مورد نیاز")
    tree.heading("irrigation_method", text="نحوه آبیاری")
    tree.heading("ph_level", text="میزان pH")
    tree.heading("fertilizer_type", text="نوع کود")
    tree.heading("fertilizer_amount", text="مقدار کود")
    tree.heading("light_exposure_duration", text="مدت زمان تابش نور")
    tree.heading("humidity", text="میزان رطوبت")
    tree.heading("solution_composition", text="ترکیب محلول غذایی")
    tree.heading("light_type", text="نوع تابش نور")

    # اضافه کردن اسکرول‌بار به Treeview
    scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=scrollbar_x.set)

    # ساخت دکمه‌های ویرایش و حذف گیاه
    btn_edit_plant = tk.Button(root, text="ویرایش گیاه", command=edit_plant)
    btn_edit_plant.pack(side="left", padx=20, pady=10)

    btn_delete_plant = tk.Button(root, text="حذف گیاه", command=delete_plant)
    btn_delete_plant.pack(side="right", padx=20, pady=10)

    show_plants_in_treeview()
    root.mainloop()

if __name__ == "__main__":
    main_window()
