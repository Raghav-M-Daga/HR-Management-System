import tkinter
from datetime import datetime
from tkcalendar import Calendar
import secrets
import string
import functions
from PIL import ImageTk, Image

# used for editing in manager page
global edit_id

# used for employee_id
global employee_id

budgeting_id = 0

# creation of all GUI pages
login = tkinter.Tk()
login.configure(background="white")
login.attributes("-fullscreen", True)

manager = tkinter.Tk()
manager.configure(background="white")
manager.attributes("-fullscreen", True)
manager.withdraw()

employee = tkinter.Tk()
employee.configure(background="white")
employee.attributes("-fullscreen", True)
employee.withdraw()

add = tkinter.Tk()
add.configure(background="white")
add.attributes("-fullscreen", True)
add.withdraw()

values = tkinter.Tk()
values.configure(background="white")
values.attributes("-fullscreen", True)
values.withdraw()

cal_tk = tkinter.Tk()
cal_tk.configure(background="white")
cal_tk.attributes("-fullscreen", True)
cal_tk.withdraw()

edit = tkinter.Tk()
edit.configure(background="white")
edit.attributes("-fullscreen", True)
edit.withdraw()

created_password_page = tkinter.Tk()
created_password_page.configure(background="white")
created_password_page.geometry("300x200")
created_password_page.eval('tk::PlaceWindow . center')
created_password_page.withdraw()

new_password = tkinter.Tk()
new_password.configure(background="white")
new_password.attributes("-fullscreen", True)
new_password.withdraw()

budget = tkinter.Tk()
budget.configure(background="white")
budget.attributes("-fullscreen", True)
budget.withdraw()

add_budget = tkinter.Tk()
add_budget.configure(background="white")
add_budget.attributes("-fullscreen", True)
add_budget.withdraw()

update_budget = tkinter.Tk()
update_budget.configure(background="white")
update_budget.attributes("-fullscreen", True)
update_budget.withdraw()

extra_costs = tkinter.Tk()
extra_costs.configure(background="white")
extra_costs.attributes("-fullscreen", True)
extra_costs.withdraw()

budget_calculations = tkinter.Tk()
budget_calculations.configure(background="white")
budget_calculations.attributes("-fullscreen", True)
budget_calculations.withdraw()

feedback = tkinter.Tk()
feedback.configure(background="white")
feedback.attributes("-fullscreen", True)
feedback.withdraw()

feedback_display = tkinter.Tk()
feedback_display.configure(background="white")
feedback_display.attributes("-fullscreen", True)
feedback_display.withdraw()

search = tkinter.Tk()
search.configure(background="white")
width = search.winfo_screenwidth()
search.geometry("%dx130+0+150" % width)
search.withdraw()


# function to end GUI
def del_gui():
    functions.end()
    add.destroy()
    values.destroy()
    cal_tk.destroy()
    edit.destroy()
    employee.destroy()
    manager.destroy()
    login.destroy()
    created_password_page.destroy()
    new_password.destroy()
    budget.destroy()
    add_budget.destroy()
    update_budget.destroy()
    extra_costs.destroy()
    budget_calculations.destroy()
    search.destroy()
    feedback.destroy()
    feedback_display.destroy()


def show_login():
    employee.withdraw()
    manager.withdraw()
    login.deiconify()


def show_cal():
    cal_tk.deiconify()
    employee.withdraw()


def show_add():
    add.deiconify()
    manager.withdraw()


def show_edit():
    edit.deiconify()
    values.withdraw()


def show_employee():
    cal_tk.withdraw()
    employee.deiconify()
    login.withdraw()
    new_password.withdraw()


def show_manager():
    edit.withdraw()
    add.withdraw()
    values.withdraw()
    manager.deiconify()
    login.withdraw()
    feedback_display.withdraw()


def show_values():
    edit.withdraw()
    values.deiconify()


def show_budget():
    manager.withdraw()
    add_budget.withdraw()
    update_budget.withdraw()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.deiconify()


def show_password():
    employee.withdraw()
    new_password.deiconify()


def show_add_budget():
    add_budget.deiconify()
    update_budget.withdraw()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.withdraw()


def show_update_budget():
    add_budget.withdraw()
    update_budget.deiconify()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.withdraw()


def show_extra_costs():
    add_budget.withdraw()
    update_budget.withdraw()
    extra_costs.deiconify()
    budget_calculations.withdraw()
    budget.withdraw()


def show_feedback():
    employee.withdraw()
    feedback.deiconify()


def show_feedback_display():
    manager.withdraw()
    feedback_display.deiconify()


# function to delete all widgets in created_password_page
def clear_value_display():
    for widget in created_password_page.winfo_children():
        widget.destroy()
    created_password_page.withdraw()


def create_password():
    original = og_password.get()
    new = created_password.get()
    if len(original) == 0 or len(new) == 0:
        tkinter.Label(new_password, text="Fill All Values", bg='red', font=("Franklin Gothic Book", 20)).grid(row=4, column=2)
    else:
        print(f"Edit ID: {edit_id}")
        pass_changer = functions.IdFunctions(edit_id)
        returned = pass_changer.change_password(original=original, new_password=new)

        if not returned:
            tkinter.Label(new_password, text="Incorrect Original Password", bg='cyan', font=("Franklin Gothic Book", 20))\
                .grid(row=4, column=2)
        else:
            for widget in new_password.winfo_children():
                if isinstance(widget, tkinter.Entry):
                    widget.delete(0, tkinter.END)
            show_employee()


def add_val():
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    month_dob = sel_month_dob.get()
    day_dob = sel_day_dob.get()
    year_dob = sel_year_dob.get()
    month_doj = sel_month_doj.get()
    day_doj = sel_day_doj.get()
    year_doj = sel_year_doj.get()
    text4 = f"{day_dob}-{month_dob}-{year_dob}"
    text5 = f"{day_doj}-{month_doj}-{year_doj}"
    text6 = sel_sex.get()
    text7 = entry1.get().replace(" ", "").casefold()
    alphabet = string.ascii_letters + string.digits
    text8 = ''.join(secrets.choice(alphabet) for x in range(6))
    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
        tkinter.Label(add, text="Fill All Values", bg="red").grid(row=3, column=1)
    else:
        functions.add_value([text1, text2, text3, text4, text5, text6, text7, text8])

    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    for widget in values.winfo_children():
        widget.destroy()

    created_password_page.deiconify()

    tkinter.Label(created_password_page, text="").grid(row=0, column=0)
    tkinter.Label(created_password_page, text="Username").grid(row=1, column=1)
    data_string = tkinter.StringVar(created_password_page)
    data_string.set(text7)
    tkinter.Entry(created_password_page, textvariable=data_string, bg="white", bd=0, state="readonly").grid(row=1, column=2)
    tkinter.Label(created_password_page, text="").grid(row=2)
    tkinter.Label(created_password_page, text="Password").grid(row=3, column=1)
    data_string = tkinter.StringVar(created_password_page)
    data_string.set(text8)
    tkinter.Entry(created_password_page, textvariable=data_string, bg="white", bd=0, state="readonly").grid(row=3, column=2)
    tkinter.Label(created_password_page, text="").grid(row=4)
    tkinter.Label(created_password_page, text="You will never be able to see this page again").grid(row=5, column=2)
    tkinter.Button(created_password_page, text="End Interaction", command=clear_value_display).grid(row=6, column=2)


def login_user():
    user = str(username.get())
    code = str(password.get())
    request_id = functions.login_check(user, code)
    if request_id == 0:
        tkinter.Label(login, text="Incorrect Details", font=("Franklin Gothic Book", 20), bg="red").grid(row=4, column=2)
        username.delete(0, tkinter.END)
        password.delete(0, tkinter.END)
    elif request_id == 1:
        show_manager()
    else:
        global edit_id
        edit_id = request_id
        print(f"Login Edit ID: {edit_id}t")
        show_employee()

    for widget in login.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, tkinter.END)


def show_all():

    for widget in values.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, tkinter.END)

    def searcher():
        search.overrideredirect(True)
        search.deiconify()
        tkinter.Label(search, text='', width=20).grid(column=0)
        returned = functions.searcher(search_value.get())
        print(returned)
        required_people = functions.read_ids(returned)
        for a in range(total_people - 1):
            for b in range(7):
                if j == 3 or j == 1:
                    unnecessary = tkinter.Label(search, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=22,
                                                text=required_people[a][b])
                else:
                    unnecessary = tkinter.Label(search, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15,
                                                text=required_people[a][b])

                unnecessary.grid(row=a, column=b+1)

    manager.withdraw()
    edit.withdraw()
    values.deiconify()
    tkinter.Label(values, text="", height=2, width=10).grid(row=0, column=0)
    people = functions.employees()
    total_people = len(people)

    if total_people > 1:
        search_value = tkinter.Entry(values, font=("Franklin Gothic Book", 15))
        search_value.grid(row=1, column=4)

        tkinter.Button(values, text="Search", font=("Franklin Gothic Book", 15), command=searcher).grid(row=1, column=2)

        tkinter.Label(values, text="ID", font=("Franklin Gothic Book", 15), width=15).grid(row=2, column=1)
        tkinter.Label(values, text="Name", font=("Franklin Gothic Book", 15), width=22).grid(row=2, column=2)
        tkinter.Label(values, text="Phone", font=("Franklin Gothic Book", 15), width=15).grid(row=2, column=3)
        tkinter.Label(values, text="Email", font=("Franklin Gothic Book", 15), width=22).grid(row=2, column=4)
        tkinter.Label(values, text="DOB", font=("Franklin Gothic Book", 15), width=15).grid(row=2, column=5)
        tkinter.Label(values, text="DOJ", font=("Franklin Gothic Book", 15), width=15).grid(row=2, column=6)
        tkinter.Label(values, text="Sex", font=("Franklin Gothic Book", 15), width=15).grid(row=2, column=7)

        for i in range(total_people-1):
            for j in range(7):
                if j == 3 or j == 1:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=22,
                                           justify='center')
                    button.insert(0, people[i+1][j])
                else:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15,
                                           justify='center')
                    button.insert(0, people[i + 1][j])

                button.grid(row=i+3, column=j+1)

    else:
        tkinter.Label(values, text="", width=25, height=2).grid(row=0, column=0)
        tkinter.Label(values, text="This database is currently empty. Go back to add an employee.",
                      font=("Franklin Gothic Book", 15)).grid(row=1, column=1)

    for c in range(total_people+3, 11):
        tkinter.Label(values, text="").grid(row=c)


def total_leave():
    tkinter.Label(cal_tk, text="Total Leave: ").grid(row=10, column=1)
    date_format = "%m/%d/%y"
    a = datetime.strptime(cal1.get_date(), date_format)
    b = datetime.strptime(cal2.get_date(), date_format)
    start = str(a)
    end = str(b)
    delta = (b - a)
    tkinter.Label(cal_tk, text=delta.days).grid(row=10, column=2)
    leaver = functions.IdFunctions(edit_id)
    if leaver.select_available_leave() is not None:
        available = leaver.select_available_leave()
    else:
        available = 30
    leaver.insert_leave(delta.days, available - delta.days, start, end)


def delete_value():
    deleter = functions.IdFunctions(delete_entry.get())
    deleter.deleting_value()
    for widget in values.winfo_children():
        widget.destroy()
    show_all()


def edit_value():
    show_edit()
    for widget in edit.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, tkinter.END)
        elif isinstance(widget, tkinter.OptionMenu):
            widget.destroy()
    for widget in edit_doj_frame.winfo_children():
        widget.destroy()
    for widget in edit_dob_frame.winfo_children():
        widget.destroy()

    editer = functions.IdFunctions(edit_entry.get())
    collected_values = editer.collect_employee_details()

    edited_day_dob.set(collected_values[3])
    edited_month_dob.set(collected_values[4])
    edited_year_dob.set(collected_values[5])

    name.insert(tkinter.END, collected_values[0])
    phone.insert(tkinter.END, collected_values[1])
    email.insert(tkinter.END, collected_values[2])

    tkinter.OptionMenu(edit_dob_frame, edited_month_dob, *months).pack(side=tkinter.LEFT)
    tkinter.OptionMenu(edit_dob_frame, edited_day_dob, *days).pack(side=tkinter.LEFT, padx=64)
    tkinter.OptionMenu(edit_dob_frame, edited_year_dob, *dob_years).pack(side=tkinter.LEFT)

    edited_day_doj.set(collected_values[6])
    edited_month_doj.set(collected_values[7])
    edited_year_doj.set(collected_values[8])

    tkinter.OptionMenu(edit_doj_frame, edited_month_doj, *months).pack(side=tkinter.LEFT)
    tkinter.OptionMenu(edit_doj_frame, edited_day_doj, *days).pack(side=tkinter.LEFT, padx=64)
    tkinter.OptionMenu(edit_doj_frame, edited_year_doj, *doj_years).pack(side=tkinter.LEFT)

    edited_sex.set(collected_values[9])

    tkinter.OptionMenu(edit, edited_sex, *["Male", "Female", "Others"]).grid(row=6, column=2)

    edit.deiconify()


def edit_button():
    editer = functions.IdFunctions(edit_entry.get())

    edited_name = name.get()
    edited_phone = phone.get()
    edited_email = email.get()
    edited_dob = f"{edited_day_dob.get()}-{edited_month_dob.get()}-{edited_year_dob.get()}"
    edited_doj = f"{edited_day_doj.get()}-{edited_month_doj.get()}-{edited_year_doj.get()}"
    edit_sex = edited_sex.get()
    data = edited_name, edited_phone, edited_email, edited_dob, edited_doj, edit_sex
    editer.edit_button(data)

    for widget in values.winfo_children():
        widget.destroy()

    show_all()
    edit.withdraw()
    values.deiconify()


def update_total_budget():
    write = open("total_budget.txt", "w")
    write.write(total_budget.get())
    write.close()


def employee_add_budget():
    result = functions.add_employee(add_budget_id.get(), add_budget_quantity.get())
    if result == 0:
        tkinter.Label(add_budget, text="This ID has been used", font=('Franklin Gothic Book', 15), foreground="red")\
            .grid(row=3, column=3)

    add_budget_id.delete(0, tkinter.END)
    add_budget_quantity.delete(0, tkinter.END)


def employee_update_budget():
    functions.edit_employee(update_budget_id.get(), update_budget_quantity.get(), update_extra_cost.get(),
                            update_cost_type.get())
    update_budget_id.delete(0, tkinter.END)
    update_budget_quantity.delete(0, tkinter.END)
    update_extra_cost.delete(0, tkinter.END)
    update_cost_type.delete(0, tkinter.END)


def add_extra_costs():
    returned = functions.add_extra_costs(extra_cost_id.get(), int(extra_costs_value.get()), extra_cost_type.get())
    if returned == 0:
        tkinter.Label(extra_costs, text="This ID has been used", font=('Franklin Gothic Book', 15), foreground="red") \
            .grid(row=3, column=3)

    extra_cost_id.delete(0, tkinter.END)
    extra_costs_value.delete(0, tkinter.END)
    extra_cost_type.delete(0, tkinter.END)


def build_budget_calc(empty):
    total_budget_people = functions.organized_budget()[1] + 3
    if empty == 1:
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people)
        tkinter.Label(budget_calculations, text="Total Budget: ", font=("Franklin Gothic Book", 15))\
            .grid(row=total_budget_people+1, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[0], font=("Franklin Gothic Book", 15), borderwidth=1,
                      relief="solid", background='white').grid(row=total_budget_people+1, column=2)
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people+2)
        tkinter.Label(budget_calculations, text="Used Budget: ", font=("Franklin Gothic Book", 15))\
            .grid(row=total_budget_people+3, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[1], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+3, column=2)
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people+4)
        tkinter.Label(budget_calculations, text="Available Budget: ", font=("Franklin Gothic Book", 15)) \
            .grid(row=total_budget_people+5, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[2], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+5, column=2)
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people+6)
        tkinter.Button(budget_calculations, text="Back", command=show_budget, font=("Franklin Gothic Book", 15))\
            .grid(row=total_budget_people+7, column=2)
        tkinter.Label(budget_calculations, text="Salaries: ", font=("Franklin Gothic Book", 15)) \
            .grid(row=total_budget_people+2, column=3)
        tkinter.Label(budget_calculations, text=functions.available_budget()[3], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+2, column=4)
        tkinter.Label(budget_calculations, text="Extra Costs: ", font=("Franklin Gothic Book", 15)) \
            .grid(row=total_budget_people+4, column=3)
        tkinter.Label(budget_calculations, text=functions.available_budget()[4], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+4, column=4)
        tkinter.Label(budget_calculations, text="", width=52).grid(column=5)
        tkinter.Button(budget_calculations, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=6)
    else:
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people)
        tkinter.Label(budget_calculations, text="Total Budget: ", font=("Franklin Gothic Book", 15)) \
            .grid(row=total_budget_people+1, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[0], font=("Franklin Gothic Book", 15), borderwidth=1,
                      relief="solid", background='white').grid(row=total_budget_people+1, column=2)
        tkinter.Label(budget_calculations, text="").grid(row=total_budget_people+2)
        tkinter.Button(budget_calculations, text="Back", command=show_budget, font=("Franklin Gothic Book", 15)) \
            .grid(row=total_budget_people+3, column=2)


def budget_update_setup():
    unorganized_edit = functions.get_edit_values(update_budget_id.get())
    update_budget_quantity.delete(0, tkinter.END)
    update_budget_quantity.insert(0, unorganized_edit[1])
    update_extra_cost.delete(0, tkinter.END)
    update_extra_cost.insert(0, unorganized_edit[2])
    update_cost_type.delete(0, tkinter.END)
    if unorganized_edit[3] is not None:
        update_cost_type.insert(0, unorganized_edit[3])


def budget_show_all():
    budget.withdraw()
    budget_calculations.deiconify()
    read_values = functions.organized_budget()
    print(read_values)
    all_budget_values = read_values[0]
    length_of_budget = read_values[1]

    if length_of_budget != 0:
        tkinter.Label(budget_calculations, text="", height=2, width=60).grid(row=0, column=0)
        tkinter.Label(budget_calculations, text="Employee ID", font=("Franklin Gothic Book", 15)).grid(row=2, column=1)
        tkinter.Label(budget_calculations, text="Salary", font=("Franklin Gothic Book", 15)).grid(row=2, column=2)
        tkinter.Label(budget_calculations, text="Extra Costs", font=("Franklin Gothic Book", 15)).grid(row=2, column=3)
        tkinter.Label(budget_calculations, text="Cost Type", font=("Franklin Gothic Book", 15)).grid(row=2, column=4)
        for i in range(length_of_budget):
            for j in range(4):
                tkinter.Label(budget_calculations, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15,
                              text=all_budget_values[i][j]).grid(row=i + 3, column=j+1)

        build_budget_calc(1)

    else:
        tkinter.Label(budget_calculations, text="", height=2, width=80).grid(row=0, column=0)
        tkinter.Label(budget_calculations, text="", width=25, height=2).grid(row=0, column=0)
        tkinter.Label(budget_calculations, text="No Added Employees",
                      font=("Franklin Gothic Book", 15)).grid(row=1, column=1)

        build_budget_calc(0)


def display_feedback():
    all_feedback = functions.read_feedback()
    if len(all_feedback) == 0:
        tkinter.Label(feedback_display, text="", width=40, height=2).grid(row=0, column=0)
        tkinter.Label(feedback_display, text="You have no feedback!",
                      font=("Franklin Gothic Book", 15)).grid(row=1, column=1)
    for i in range(len(all_feedback)):
        tkinter.Label(feedback_display, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15,
                      text=all_feedback[i][1]).grid(row=i + 3, column=1)


def submit_feedback():
    functions.send_feedback(typed_feedback.get())
    typed_feedback.delete(0, tkinter.END)
    feedback.withdraw()
    employee.deiconify()


def create_feedback():
    feedback_display.deiconify()
    manager.withdraw()
    read_feedback = functions.read_feedback()

    for widget in feedback_display.winfo_children():
        widget.destroy()

    frame = tkinter.Frame(feedback_display, width=feedback_display.winfo_screenwidth())
    frame.pack(side=tkinter.TOP, padx=20)

    s = tkinter.Scrollbar(frame, troughcolor='red')
    s.pack(side=tkinter.RIGHT, fill=tkinter.Y, padx=(0, 20), pady=20)

    t = tkinter.Text(frame, width=feedback_display.winfo_screenwidth(), height=15, wrap=tkinter.WORD,
                     yscrollcommand=s.set, font=("Franklin Gothic Book", 22))

    t.pack(side=tkinter.TOP, fill=tkinter.X, pady=20, padx=(20, 0))

    s.config(command=t.yview)

    for o in read_feedback:
        t.insert(tkinter.END, str(o[1]) + "\n\n")

    tkinter.Button(feedback_display, text="Back", font=("Franklin Gothic Book", 20), command=show_manager)\
        .pack(side=tkinter.BOTTOM, pady=75)


# Creating login UI
canvas = tkinter.Canvas(login, width=350, height=150, highlightthickness=0, bg="white")
canvas.grid(row=0, column=0)
img = (Image.open("cottonsoil.png"))
new_image = ImageTk.PhotoImage(master=canvas, image=img)
canvas.create_image(40, 30, anchor="nw", image=new_image)

tkinter.Label(login, text="Login Page", height=3, bg="white", font=("Franklin Gothic Book", 35, "bold"), fg="#6cb444")\
    .grid(row=1, column=2)
tkinter.Label(login, text="Username: ", font=("Franklin Gothic Book", 20),
              height=2, bg="white", width=18).grid(row=2, column=1)
username = tkinter.Entry(login, font=("Franklin Gothic Book", 20), bg="white", borderwidth=2, relief="solid")
username.grid(row=2, column=2)
tkinter.Label(login, text="Password: ", font=("Franklin Gothic Book", 20), height=2, bg="white").grid(row=3, column=1)
password = tkinter.Entry(login, show="*", font=("Franklin Gothic Book", 20), bg="white", borderwidth=2, relief="solid")
password.grid(row=3, column=2)

tkinter.Label(login, text="", width=77, bg="white").grid(row=4, column=3)

tkinter.Button(login, text="Enter", command=login_user, font=("Franklin Gothic Book", 20), relief="ridge", borderwidth=2,
               bg="#6cb444", fg="white").grid(row=5, column=2)

tkinter.Button(login, text="X", width=7, height=2, command=del_gui, bg="red").grid(row=0, column=4, sticky="ne")

# Creating employee UI

tkinter.Label(employee, text="", width=90, height=10).grid(row=1, column=0)
tkinter.Label(employee, text="", width=85, height=3).grid(row=1, column=2)
tkinter.Button(employee, text="Leave Application", font=("Franklin Gothic Book", 20), command=show_cal, bg="yellow").\
    grid(column=1, row=2)
tkinter.Label(employee, text="", height=2).grid(row=3, column=0)
tkinter.Button(employee, text="Submit Feedback", font=("Franklin Gothic Book", 20), command=show_feedback, bg="yellow"). \
    grid(column=1, row=4)
tkinter.Label(employee, text="", height=2).grid(row=5, column=0)
tkinter.Button(employee, text="Change Password", font=("Franklin Gothic Book", 20), command=show_password).grid(column=1, row=6)
tkinter.Label(employee, text="").grid(row=7)
tkinter.Button(employee, text="Back", command=show_login, font=("Franklin Gothic Book", 20), bg="yellow").grid(column=1, row=8)

tkinter.Button(employee, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=3, row=0)

# Creating manager UI
tkinter.Label(manager, text="", width=30, bg="white").grid(row=1, column=0)
tkinter.Label(manager, text="", width=70, bg="white").grid(row=0, column=2)
manager_canvas = tkinter.Canvas(manager, width=350, height=150, highlightthickness=0, bg="white")
manager_canvas.grid(row=0, column=0, sticky="w")
manager_img = (Image.open("cottonsoil.png"))
manager_new_image = ImageTk.PhotoImage(master=manager_canvas, image=manager_img)
manager_canvas.create_image(40, 30, anchor="nw", image=manager_new_image)

tkinter.Button(manager, text="Add Employee", command=show_add, bg="#6cb444", fg="white", font=("Franklin Gothic Book", 20), width=20)\
    .grid(column=1, row=2, padx=30)
tkinter.Label(manager, text="Manager Page", height=5, fg="#6cb444", font=("Franklin Gothic Book", 25, "bold")).grid(row=1, column=2)
tkinter.Button(manager, text="Show Employees", font=("Franklin Gothic Book", 20), command=show_all, bg="#6cb444", fg="white", width=20)\
    .grid(column=3, row=2, padx=30)
tkinter.Button(manager, text="Budget Management", command=show_budget, font=("Franklin Gothic Book", 20), bg="#6cb444", fg="white", width=20)\
    .grid(column=1, row=4, padx=30)
tkinter.Button(manager, text="Read Feedback", font=("Franklin Gothic Book", 20), command=create_feedback, bg="#6cb444", fg="white", width=20)\
    .grid(row=4, column=3, padx=30)
tkinter.Label(manager, text="", bg="white").grid(row=9, column=0)
tkinter.Button(manager, text="Back", command=show_login, height=2, width=7, bg="dark gray").grid(column=3, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(manager, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=4, row=0, sticky="n", pady=4)

# Creating add UI
tkinter.Label(add, text="", width=75, height=2).grid(row=0, column=0)
tkinter.Label(add, text="", width=66).grid(row=0, column=3)
tkinter.Label(add, text="Name: ", width=10, font=("Franklin Gothic Book", 20)).grid(row=1, column=1)
entry1 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20))
entry1.grid(row=1, column=2)
tkinter.Label(add, text="Phone: ", font=("Franklin Gothic Book", 20)).grid(row=2, column=1)
entry2 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20))
entry2.grid(row=2, column=2)
tkinter.Label(add, text="Email: ", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
entry3 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20))
entry3.grid(row=3, column=2)

tkinter.Label(add, text="DOB: ", font=("Franklin Gothic Book", 20)).grid(row=4, column=1)

frame1 = tkinter.Frame(add)
frame1.grid(row=4, column=2, sticky="nsew")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sel_month_dob = tkinter.StringVar(frame1)
sel_month_dob.set("Jan")
days = [x for x in range(1, 32)]
sel_day_dob = tkinter.StringVar(frame1)
sel_day_dob.set('1')
dob_years = [x for x in range(1980, 2005)]
sel_year_dob = tkinter.StringVar(frame1)
sel_year_dob.set('1980')
month_entry_dob = tkinter.OptionMenu(frame1, sel_month_dob, *months)
month_entry_dob.pack(side=tkinter.LEFT)
day_entry_dob = tkinter.OptionMenu(frame1, sel_day_dob, *days)
day_entry_dob.pack(side=tkinter.LEFT, padx=64)
year_entry_dob = tkinter.OptionMenu(frame1, sel_year_dob, *dob_years)
year_entry_dob.pack(side=tkinter.LEFT)
tkinter.Label(add, text="DOJ: ", font=("Franklin Gothic Book", 20)).grid(row=5, column=1)

frame2 = tkinter.Frame(add)
frame2.grid(row=5, column=2, sticky="nsew")
doj_years = [x for x in range(2015, 2022)]
sel_month_doj = tkinter.StringVar(frame2)
sel_month_doj.set("Jan")
sel_day_doj = tkinter.StringVar(frame1)
sel_day_doj.set('1')
sel_year_doj = tkinter.StringVar(frame1)
sel_year_doj.set('2015')
month_entry_doj = tkinter.OptionMenu(frame2, sel_month_doj, *months)
month_entry_doj.pack(side=tkinter.LEFT)
day_entry_doj = tkinter.OptionMenu(frame2, sel_day_doj, *days)
day_entry_doj.pack(side=tkinter.LEFT, padx=64)
year_entry_doj = tkinter.OptionMenu(frame2, sel_year_doj, *doj_years)
year_entry_doj.pack(side=tkinter.LEFT)
tkinter.Label(add, text="Sex: ", font=("Franklin Gothic Book", 20)).grid(row=6, column=1)
options = ["Male", "Female", "Others"]
sel_sex = tkinter.StringVar(add)
sel_sex.set("Male")
entry6 = tkinter.OptionMenu(add, sel_sex, *options)
entry6.grid(row=6, column=2)
tkinter.Label(add, text="").grid(column=2, row=11)
tkinter.Button(add, text="Enter", command=add_val, font=("Franklin Gothic Book", 20)).grid(column=2, row=7)
tkinter.Button(add, text="Back", command=show_manager, bg="yellow", font=("Franklin Gothic Book", 20)).grid(column=2, row=8)
tkinter.Button(add, text="X", bg="red", command=del_gui, width=7, height=2).grid(column=4, row=0)


# Creating values UI
for i in range(10):
    tkinter.Label(values, text="").grid(row=i)
tkinter.Button(values, text="Next", command=show_all, font=("Franklin Gothic Book", 12)).grid(row=10, column=3)
tkinter.Label(values, text="").grid(column=4)
tkinter.Button(values, text="Back", command=show_all, font=("Franklin Gothic Book", 12)).grid(row=10, column=5)
tkinter.Label(values, text="").grid(row=11)
tkinter.Label(values, text="ID To Delete: ", font=("Franklin Gothic Book", 15)).grid(row=12, column=3)
delete_entry = tkinter.Entry(values, width=5, font=("Franklin Gothic Book", 15))
delete_entry.grid(row=12, column=4)
deleter_send = tkinter.Button(values, text="Delete", command=delete_value, font=("Franklin Gothic Book", 15))
deleter_send.grid(row=12, column=5)
tkinter.Label(values, text="", height=3).grid(row=13)
tkinter.Label(values, text="Id to Edit: ", font=("Franklin Gothic Book", 15)).grid(row=13, column=3)
edit_entry = tkinter.Entry(values, font=("Franklin Gothic Book", 15), width=5)
edit_entry.grid(row=13, column=4)
tkinter.Button(values, text="Edit", command=edit_value, font=("Franklin Gothic Book", 15)).grid(row=13, column=5)
tkinter.Label(values, text="", height=3).grid(row=14)
tkinter.Button(values, text="Back", command=show_manager, font=("Franklin Gothic Book", 15)).grid(row=15, column=4)
tkinter.Label(values, text="", width=8).grid(row=0, column=8)
tkinter.Button(values, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=9, row=0)

tkinter.Button(edit, text="Update", command=edit_button, font=("Franklin Gothic Book", 20)).grid(column=2, row=8)
tkinter.Button(edit, text="Back", command=show_all, bg="yellow", font=("Franklin Gothic Book", 20)).grid(column=2, row=9)
tkinter.Button(edit, text="X", bg="red", command=del_gui, width=7, height=2).grid(column=4, row=0)

# Creating edit UI
tkinter.Label(edit, text="", width=75, height=2).grid(row=0, column=0)
tkinter.Label(edit, text="", width=65).grid(row=0, column=3)
tkinter.Label(edit, text="Name: ", width=10, font=("Franklin Gothic Book", 20)).grid(row=1, column=1)
name = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
name.grid(row=1, column=2)
tkinter.Label(edit, text="Phone: ", font=("Franklin Gothic Book", 20)).grid(row=2, column=1)
phone = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
phone.grid(row=2, column=2)
tkinter.Label(edit, text="Email: ", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
email = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
email.grid(row=3, column=2)
tkinter.Label(edit, text="DOB: ", font=("Franklin Gothic Book", 20)).grid(row=4, column=1)
edit_dob_frame = tkinter.Frame(edit)
edit_dob_frame.grid(row=4, column=2, sticky="nsew")
edited_month_dob = tkinter.StringVar(edit_dob_frame)
edited_day_dob = tkinter.StringVar(edit_dob_frame)
edited_year_dob = tkinter.StringVar(edit_dob_frame)
tkinter.OptionMenu(edit_dob_frame, edited_month_dob, *months).pack(side=tkinter.LEFT)
tkinter.OptionMenu(edit_dob_frame, edited_day_dob, *days).pack(side=tkinter.LEFT, padx=64)
tkinter.OptionMenu(edit_dob_frame, edited_year_dob, *dob_years).pack(side=tkinter.LEFT)

tkinter.Label(edit, text="DOJ: ", font=("Franklin Gothic Book", 20)).grid(row=5, column=1)

edit_doj_frame = tkinter.Frame(edit)
edit_doj_frame.grid(row=5, column=2, sticky="nsew")
edited_month_doj = tkinter.StringVar(edit_doj_frame)
edited_day_doj = tkinter.StringVar(edit_doj_frame)
edited_year_doj = tkinter.StringVar(edit_doj_frame)
tkinter.OptionMenu(edit_doj_frame, edited_month_doj, *months).pack(side=tkinter.LEFT)
tkinter.OptionMenu(edit_doj_frame, edited_day_doj, *days).pack(side=tkinter.LEFT, padx=64)
tkinter.OptionMenu(edit_doj_frame, edited_year_doj, *doj_years).pack(side=tkinter.LEFT)


tkinter.Label(edit, text="Sex", font=("Franklin Gothic Book", 20)).grid(column=1, row=6)
edited_sex = tkinter.StringVar(edit)
tkinter.OptionMenu(edit, edited_sex, *["Male", "Female", "Others"]).grid(row=6, column=2)

tkinter.Label(edit, text="").grid(column=0, row=7)

# Creating cal_tk UI
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year

tkinter.Label(cal_tk, text="", width=65, height=2).grid(row=0, column=0)
tkinter.Label(cal_tk, text="", width=72, height=2).grid(row=0, column=3)
tkinter.Label(cal_tk, text="Select Name: ", font=("Franklin Gothic Book", 15)).grid(row=1, column=1)
tkinter.Label(cal_tk, text="Leave Start", font=("Franklin Gothic Book", 15)).grid(row=2, column=1)
cal1 = Calendar(cal_tk, selectmode='day', year=year, month=month, day=day, font=("Franklin Gothic Book", 15))
cal1.grid(row=3, column=2)

opt_list = functions.employees()
fixed_opt_list = []
for item in opt_list:
    fixed_opt_list.append(f"{item[0]}-{item[1]}")

if len(fixed_opt_list) > 0:
    sel_val = tkinter.StringVar(cal_tk)
    sel_val.set(fixed_opt_list[0])
    person_name = tkinter.OptionMenu(cal_tk, sel_val, *fixed_opt_list)
    person_name.grid(row=1, column=2)
else:
    tkinter.Label(cal_tk, text="No Registered Employees", font=("Franklin Gothic Book", 20), bg="red").grid(row=1, column=2)

tkinter.Label(cal_tk, text="").grid(row=4, column=1)


# second calendar for ending of leave
tkinter.Label(cal_tk, text="Leave End", font=("Franklin Gothic Book", 15)).grid(row=5, column=1)
cal2 = Calendar(cal_tk, selectmode='day', year=year, month=month, day=day, font=("Franklin Gothic Book", 15))
cal2.grid(row=6, column=2)


tkinter.Label(cal_tk, text="").grid(row=7, column=2)
if len(fixed_opt_list) > 0:
    tkinter.Button(cal_tk, text="Confirm Leave", command=total_leave, font=("Franklin Gothic Book", 15)).grid(row=8, column=2)
else:
    tkinter.Label(cal_tk, text="No Registered Employees", font=("Franklin Gothic Book", 20), bg="red").grid(row=8, column=2)
tkinter.Label(cal_tk, text="").grid(row=9, column=2)

tkinter.Button(cal_tk, text="Back", command=show_employee, font=("Franklin Gothic Book", 15)).grid(row=14, column=2)

tkinter.Button(cal_tk, text="X", command=del_gui, bg="red", width=7, height=2)\
    .grid(row=0, column=4)

# designing password page

tkinter.Label(new_password, text="", width=50).grid(row=0, column=0)
tkinter.Label(new_password, text="Original Password:", font=("Franklin Gothic Book", 20)).grid(row=1, column=1)
og_password = tkinter.Entry(new_password, font=("Franklin Gothic Book", 20))
og_password.grid(row=1, column=2)
tkinter.Label(new_password, text="").grid(row=2)
tkinter.Label(new_password, text="New Password: ", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
created_password = tkinter.Entry(new_password, font=("Franklin Gothic Book", 20))
created_password.grid(row=3, column=2)
tkinter.Button(new_password, text="Send", font=("Franklin Gothic Book", 20), command=create_password).grid(row=4, column=2)
tkinter.Label(new_password, text="").grid(row=5)
tkinter.Button(new_password, text="Back", command=show_employee, font=("Franklin Gothic Book", 20)).grid(row=6, column=2)
tkinter.Label(new_password, text="", width=50).grid(column=3)
tkinter.Button(new_password, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=4)

# designing budget page

reader = open("total_budget.txt", "r")
fill_budget = reader.read()

tkinter.Label(budget, text="", width=20).grid(row=0, column=0)
tkinter.Label(budget, text="").grid(row=0, column=1)
tkinter.Label(budget, text="Budget Management", font=("Franklin Gothic Book", 30)).grid(row=1, column=2)
tkinter.Label(budget, text="", height=12, width=65).grid(row=2, column=2)
total_budget_frame = tkinter.Frame(budget)
total_budget_frame.grid(row=3, column=2)
tkinter.Label(total_budget_frame, text="Total Budget:", font=("Franklin Gothic Book", 20)).pack(side=tkinter.LEFT)
total_budget = tkinter.Entry(total_budget_frame, font=("Franklin Gothic Book", 20))
total_budget.pack(side=tkinter.LEFT, padx=40)
total_budget.insert(0, fill_budget)
tkinter.Button(total_budget_frame, text="Confirm", font=("Franklin Gothic Book", 20), command=update_total_budget)\
    .pack(side=tkinter.LEFT)
tkinter.Label(budget, text="")
tkinter.Button(budget, text="Add Employee Salary", font=("Franklin Gothic Book", 20), fg="green", command=show_add_budget)\
    .grid(row=5, column=1)
tkinter.Button(budget, text="Update Employee Salary", font=("Franklin Gothic Book", 20), fg="green", command=show_update_budget)\
    .grid(row=5, column=3)
tkinter.Label(budget, text="").grid(row=6)
tkinter.Button(budget, text="Enter Extra Costs", font=("Franklin Gothic Book", 20), fg="green", command=show_extra_costs)\
    .grid(row=7, column=1)
tkinter.Button(budget, text="Budget Calculations", font=("Franklin Gothic Book", 20), fg="green", command=budget_show_all)\
    .grid(row=7, column=3)
tkinter.Label(budget, text="").grid(row=8)
tkinter.Button(budget, text="Back", font=("Franklin Gothic Book", 20), command=show_manager).grid(row=9, column=2)
tkinter.Label(budget, text="", width=6).grid(column=4)
tkinter.Button(budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=5)

# designing add_budget page

tkinter.Label(add_budget, text="", width=55).grid(row=0, column=0)
tkinter.Label(add_budget, text="", width=35).grid(row=0, column=1)
tkinter.Label(add_budget, text="Add Budget", font=("Franklin Gothic Book", 30)).grid(row=1, column=2)
tkinter.Label(add_budget, text="").grid(row=2, column=1)
tkinter.Label(add_budget, text="Employee ID:", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
add_budget_id = tkinter.Entry(add_budget, font=("Franklin Gothic Book", 20))
add_budget_id.grid(row=3, column=2)
tkinter.Label(add_budget, text="Salary:", font=("Franklin Gothic Book", 20)).grid(row=4, column=1)
add_budget_quantity = tkinter.Entry(add_budget, font=("Franklin Gothic Book", 20))
add_budget_quantity.grid(row=4, column=2)
tkinter.Button(add_budget, text="Confirm", font=("Franklin Gothic Book", 20), fg="green",
               command=employee_add_budget).grid(row=5, column=2)
tkinter.Label(add_budget, text="").grid(row=6)
tkinter.Button(add_budget, text="Back", font=("Franklin Gothic Book", 20), command=show_budget).grid(row=7, column=2)
tkinter.Label(add_budget, text="", width=67).grid(column=3)
tkinter.Button(add_budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=4)

# designing update_budget page

tkinter.Label(update_budget, text="", width=35).grid(row=0, column=0)
tkinter.Label(update_budget, text="Update Employee Budget", font=("Franklin Gothic Book", 30)).grid(row=1, column=2)
tkinter.Label(update_budget, text="").grid(row=2, column=1)
tkinter.Label(update_budget, text="Employee ID: ", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
update_budget_id = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20))
update_budget_id.grid(row=3, column=2)
tkinter.Button(update_budget, text="Confirm", font=("Franklin Gothic Book", 20), command=budget_update_setup).grid(row=3, column=3)
tkinter.Label(update_budget, text="Salary: ", font=("Franklin Gothic Book", 20)).grid(row=4, column=1)
update_budget_quantity = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20))
update_budget_quantity.grid(row=4, column=2)
tkinter.Label(update_budget, text="Extra Cost: ", font=("Franklin Gothic Book", 20)).grid(row=5, column=1)
update_extra_cost = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20))
update_extra_cost.grid(row=5, column=2)
tkinter.Label(update_budget, text="Cost Type: ", font=("Franklin Gothic Book", 20)).grid(row=6, column=1)
update_cost_type = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20))
update_cost_type.grid(row=6, column=2)
tkinter.Button(update_budget, text="Confirm", font=("Franklin Gothic Book", 20), fg="green",
               command=employee_update_budget).grid(row=7, column=2)
tkinter.Button(update_budget, text="Back", font=("Franklin Gothic Book", 20), command=show_budget).grid(row=8, column=2)
tkinter.Label(add_budget, text="", width=52).grid(column=4)
tkinter.Button(update_budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=5)

# designing extra_costs page

tkinter.Label(extra_costs, text="", width=35).grid(row=0, column=0)
tkinter.Label(extra_costs, text="Add Extra Costs", font=("Franklin Gothic Book", 30)).grid(row=1, column=1)
tkinter.Label(extra_costs, text="").grid(row=2, column=1)
tkinter.Label(extra_costs, text="Employee ID: ").grid(row=3, column=1)
extra_cost_id = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20))
extra_cost_id.grid(row=3, column=2)
tkinter.Label(extra_costs, text="Extra Cost").grid(row=4, column=1)
extra_costs_value = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20))
extra_costs_value.grid(row=4, column=2)
tkinter.Label(extra_costs, text="Cost Type").grid(row=5, column=1)
extra_cost_type = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20))
extra_cost_type.grid(row=5, column=2)
tkinter.Button(extra_costs, text="Confirm", font=("Franklin Gothic Book", 20), fg="green",
               command=add_extra_costs).grid(row=6, column=2)
tkinter.Button(extra_costs, text="Back", font=("Franklin Gothic Book", 20), command=show_budget).grid(row=7, column=2)
tkinter.Label(extra_costs, text="", width=20).grid(column=3)
tkinter.Button(extra_costs, text="X", width=7, height=2, bg="red").grid(row=0, column=4)

# creating feedback page

tkinter.Label(feedback, text="", width=50).grid(row=0, column=0)
tkinter.Label(feedback, text="Write your Feedback", font=("Franklin Gothic Book", 20)).grid(row=1, column=1)
typed_feedback = tkinter.Entry(feedback, font=("Franklin Gothic Book", 20), width=40)
typed_feedback.grid(row=1, column=2)
tkinter.Label(feedback, text="").grid(row=2)
tkinter.Button(feedback, font=("Franklin Gothic Book", 20), text="Submit", command=submit_feedback).grid(row=3, column=2)

login.mainloop()
