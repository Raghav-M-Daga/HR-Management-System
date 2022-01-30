import tkinter
from PIL import ImageTk, Image
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raghav2007",
    database="hr_db")

my_cursor = mydb.cursor()


def login_check(username, password):
    my_cursor.execute("SELECT * FROM People")
    people = my_cursor.fetchall()
    for value in range(len(people)):
        if (people[value][7], people[value][8]) == (username, password):
            return people[value][0]

    return 0


def add_value(data):
    my_cursor.execute("SELECT * FROM people")
    people = my_cursor.fetchall()
    try:
        nearest_id = people[-1][0] + 1
    except:
        nearest_id = 1

    insert_stmnt = "INSERT INTO people(employee_id, name, phone, email, dob, doj, sex, username, password) " \
                   "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data.insert(0, nearest_id)
    my_cursor.execute(insert_stmnt, data)
    mydb.commit()


def employees():
    my_cursor.execute("SELECT * FROM People")
    people = my_cursor.fetchall()
    return people


class IdFunctions:

    def __init__(self, task_id):
        self.task_id = task_id

    def edit_button(self, data):
        print(data)
        update = "UPDATE people SET name=%s, phone=%s, email=%s, dob=%s, doj=%s, sex=%s WHERE employee_id=%s"
        remade_data = []
        for value in data:
            remade_data.append(value)
        remade_data.append(self.task_id)
        my_cursor.execute(update, remade_data)
        mydb.commit()

    def deleting_value(self):
        val_delete = self.task_id
        delete_statement1 = "DELETE FROM leave_track WHERE leaverId=%s"
        delete_statement2 = "DELETE FROM budget WHERE employee_id=%s"
        delete_statement3 = "DELETE FROM people WHERE employee_id=%s"
        my_cursor.execute(delete_statement1, (val_delete, ))
        my_cursor.execute(delete_statement2, (val_delete, ))
        my_cursor.execute(delete_statement3, (val_delete, ))
        mydb.commit()

    def collect_employee_details(self):
        my_cursor.execute("SELECT * FROM people WHERE employee_id=%s", (self.task_id, ))
        details = my_cursor.fetchall()[0]
        print(details)
        name = details[1]
        phone = details[2]
        email = details[3]
        dob_day = details[4].split("-")[0]
        dob_month = details[4].split("-")[1]
        dob_year = details[4].split("-")[2]
        doj_day = details[5].split("-")[0]
        doj_month = details[5].split("-")[1]
        doj_year = details[5].split("-")[2]
        sex = details[6]

        return name, phone, email, dob_day, dob_month, dob_year, doj_day, doj_month, doj_year, sex

    def insert_leave(self, leaves, available, start, end_leave):
        leave_stmnt = "INSERT INTO leave_track(leaverId, leaves, available, start, end) VALUES(%s, %s, %s, %s, %s)"
        my_cursor.execute(leave_stmnt, (self.task_id, leaves, available, start, end_leave))
        mydb.commit()

    def select_available_leave(self):
        leave_stmnt = "SELECT available FROM leave_track WHERE leaverId=%s"
        my_cursor.execute(leave_stmnt, (self.task_id, ))
        available = my_cursor.fetchall()
        if len(available) > 0:
            print(available)
            return available[0][0]

    def change_password(self, original, new_password):
        print(self.task_id)
        my_cursor.execute("SELECT password FROM people WHERE employee_id=%s", (self.task_id, ))
        correct_password = my_cursor.fetchall()[0][0]
        print(correct_password)
        if str(original) == correct_password:
            my_cursor.execute("UPDATE people SET password=%s WHERE employee_id=%s", (str(new_password), self.task_id))
            mydb.commit()
            return True
        else:
            return False


def add_employee(employee_id, salary):
    my_cursor.execute("SELECT * FROM budget")
    budget_values = my_cursor.fetchall()
    print(budget_values)
    added_budget_ids = []
    for value in budget_values:
        added_budget_ids.append(value[0])

    print(added_budget_ids)

    for value in added_budget_ids:
        if int(employee_id) == int(value):
            return 0

    my_cursor.execute("SELECT * FROM people")
    people_values = my_cursor.fetchall()
    people_ids = []
    for value in people_values:
        people_ids.append(value[0])

    print(people_ids)

    for value in people_ids:
        if int(employee_id) == int(value):
            return 0

    my_cursor.execute("INSERT INTO budget(employee_id, salary) VALUES (%s, %s)", (employee_id, salary))
    mydb.commit()
    return 1


def add_extra_costs(employee_id, extra_cost: int, cost_type):
    my_cursor.execute("SELECT * FROM budget")
    budget_values = my_cursor.fetchall()
    print(budget_values)
    added_budget_ids = []
    for value in budget_values:
        added_budget_ids.append(value[0])

    print(added_budget_ids)

    for value in added_budget_ids:
        if int(employee_id) == int(value):
            return 0
        else:
            my_cursor.execute("UPDATE budget SET extra_cost=%s, cost_type=%s WHERE employee_id=%s",
                              (extra_cost, cost_type, employee_id))
            return 1
    mydb.commit()


def edit_employee(employee_id, salary, extra_cost, cost_type):
    my_cursor.execute("UPDATE budget SET salary=%s, extra_cost=%s, cost_type=%s WHERE employee_id=%s",
                      (salary, extra_cost, cost_type, employee_id))
    mydb.commit()


def available_budget():
    read = open("total_budget.txt", "r")
    total_budget = int(read.read())
    my_cursor.execute("SELECT * FROM budget")
    used = 0
    salary = 0
    extra = 0
    all_values = my_cursor.fetchall()
    for value in all_values:
        salary += int(value[1])
        extra += int(value[2])
        used += int(value[1])
        used += int(value[2])

    return total_budget, used, total_budget - used, salary, extra


def get_edit_values(employee_id):
    my_cursor.execute("SELECT * FROM budget WHERE employee_id=%s", (employee_id,))
    edit_values = my_cursor.fetchall()[0]
    return edit_values


def check_for_existence():
    my_cursor.execute("SELECT employee_id FROM budget")
    return my_cursor.fetchall()


def organized_budget():
    my_cursor.execute("SELECT * FROM budget")
    budgets = my_cursor.fetchall()
    return budgets, len(budgets)


def send_feedback(feedback):
    my_cursor.execute("SELECT * FROM feedback")
    people = my_cursor.fetchall()
    try:
        nearest_id = people[-1][0] + 1
    except:
        nearest_id = 1

    my_cursor.execute("INSERT INTO feedback(position, content) VALUES(%s, %s)", (nearest_id, feedback))
    mydb.commit()


def read_feedback() -> list:
    my_cursor.execute("SELECT * FROM feedback")
    return my_cursor.fetchall()


def searcher(target: str) -> list:

    my_cursor.execute("SELECT * FROM people")
    array = my_cursor.fetchall()
    del array[0]

    findings = []

    length = len(target)
    for i in range(length, 2, -1):
        to_find = target[:i]
        for item in array:
            if to_find == item[1][:i].casefold():
                if item[0] not in findings:
                    findings.append(item[0])

    print(findings)
    return findings


def read_ids(id_list):
    all_values = []
    for value in id_list:
        my_cursor.execute("SELECT * FROM people WHERE employee_id=%s", (value, ))
        all_values.append(my_cursor.fetchall()[0])

    print(all_values)
    return all_values


def end():
    mydb.commit()
    my_cursor.close()
    mydb.close()
