from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QMessageBox
from layout import *
from menu import *
from data import *
from study import *
from random import choice
from layout2 import *

#q = choice(quest_list)
#q.show_data(questionLb, result_answ, rbtn_list)

q = 0

points = 0

#https://github.com/SvitlanaMa/memory

def start_test2():
    global points
    points = 0
    global q
    q = 0
    shuffle(quest_list)
    quest_list[q].show_data2(question2)
    menu_window.hide()
    open_window.show()

#timer = QTimer()
#timer.setInterval(1000)

def list_click():
    for q in quest_list:
        if q.question == qw_list.currentItem().text():
            q.show_data_study(pict_lb, ans_lb)
            break

#def 

def ok_click():
    global q
    if okey_btn.text() == "Відповісти":
        if button_group.checkedButton():
            q.chek_result(rbtn_list, result)
            show_result()
    else:
        q = choice(quest_list)
        q.show_data(questionLb, result_answ, rbtn_list)
        show_question()

def ok_click2():
    global q
    global points
    if q < 10:
        print(quest_list[q].right)
        if quest_list[q].right == otvet.text().strip():
            points = points + 1
            print(points)
            print('Верно')
        else:
            
            print('Не верно')
        q = q + 1
        quest_list[q].show_data2(question2)
    else:
        results_window.exec_()
        print('Опрос закончен')       
        back_to_menu3()


def show_data():
    pass 
def check_result():
    pass

def start_study():
    timer.start()
    qw_list.clear()
    for q in quest_list:
        qw_list.addItem(q.question)
    menu_window.hide()
    study_window.show()

def back_to_menu3():
    results_window.hide()
    menu_window.show()
    open_window.hide()

def back_to_menu():
    main_window.hide()
    study_window.hide()
    menu_window.show()

def back_to_menu2():
    main_window.hide()
    menu_window.hide()
    study_window.show()



def start_test():
    menu_window.hide()
    main_window.show()

#def crate_test():
    #main_window.hide()
    #crate_test.show()




test_btn.clicked.connect(start_test)
okey_btn.clicked.connect(ok_click)
create_btn.clicked.connect(start_study)
menu_btn.clicked.connect(back_to_menu)
qw_list.itemClicked.connect(list_click)
new_btn.clicked.connect(start_test2)
okey2_btn.clicked.connect(ok_click2)

main_window = QWidget()
main_window.setWindowTitle('Закрите тестування')
main_window.resize(600, 500)
main_window.move(0, 0)



menu_window = QWidget()
menu_window.setWindowTitle('Мой проект')
menu_window.resize(400, 400)
menu_window.move(0, 0)

open_window = QWidget()
open_window.setWindowTitle('Відкрите тестування')
open_window.resize(400, 600)
open_window.move(0, 0)
open_window.setLayout(layout1)

menu_window.show()

menu_window.setLayout(menu_line)
main_window.setLayout(layout_card)

results_window = QMessageBox()
results_window.setText('Результат:' + str(points))

study_window = QWidget()
study_window.resize(700, 400)
study_window.setWindowTitle("Бестиарий")
# study_window.move(0, 0)
study_window.setLayout(study_line)

#main_window.show()



app.exec_()