from random import shuffle

# class Test:
#     def init(self, quest_list, quantity = 5):

#         # self.current_quest = 0

class Questions:
    def __init__(self, question, right, wrong1, wrong2, wrong3, img = None):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.img = img
    
    def show_data(self, quest_lb, result_answ, rbtn_list):
        quest_lb.setText(self.question + "<br>" + f"<img src={self.img} height=100>")
        result_answ.setText(self.right)
        shuffle(rbtn_list)
        rbtn_list[0].setText(self.right)
        rbtn_list[1].setText(self.wrong1)
        rbtn_list[2].setText(self.wrong2)
        rbtn_list[3].setText(self.wrong3)

    def show_data2(self, quest_lb):
        quest_lb.setText(self.question + "<br>" + f"<img src={self.img} height=100>")
        
    def show_data_study(self, pict_lb, answ_lb):
        pict_lb.setText(f"<img src={self.img} height=100>")
        answ_lb.setText(self.right)

    def chek_result(self, rbtn_list, result):
        if rbtn_list[0].isChecked():
            result.setText("вірно!")
        else:
            result.setText("не вірно!")


q1 = Questions("У якому році ввели у стрій лінкор King Georg 5", "1940", "1939", "1941", "1945", "princeofwales.jpg")
q2 = Questions("У якому році ввели у стрій лінкор Bismark", "1940", "1933", "1914", "1942", "bismark.jpg")
q3 = Questions("У якому році ввели у стрій лінкор Nevada", "1916", "1937", "1932", "1922", "nevada.jpg")
q4 = Questions("У якому році ввели у стрій лінкор Yamato", "1941", "1911", "1943", "1929", "yamato.jpg")
q5 = Questions("У якому році ввели у стрій крейсер Alaska", "1944", "2017", "1923", "1947", "alaska.jpg")
q6 = Questions("У якому році ввели у стрій крейсер Prinz Eugen", "1939", "1940", "1934", '1932', "Eugen.png")
q7 = Questions("У якому році ввели у стрій лінкор Elizabeth", "1915", "1920", "1930", "1900", "elizabeth.jpg")
q8 = Questions("У якому році ввели у стрій лінкор Dreadnought", "1906", "1903", "1917", "1879", "dreadnought.jpg")
q9 = Questions("У якому році ввели у стрій лінкор Jersey", "1942", "1905", "1940", "1953", "jersey.jpg")
q10 = Questions("У якому році ввели у стрій лінкор Haruna", "1942", "1905", "1940", "1913", "Haruna.jpg")
q11 = Questions("У якому році ввели у стрій лінкор Scharnhorst", "1936", "1908", "1940", "1937", "Scharnhorst.jpg")
q12 = Questions("У якому році ввели у стрій лінкор Gneisenau", "1936", "1917", "1942", "1957", "Gneisenau.jpg")
q13 = Questions("У якому році ввели у стрій лінкор Tirpitz", "1942", "1939", "1947", "1911", "Tirpitz.jpg")
q14 = Questions("У якому році ввели у стрій лінкор Musashi", "1927", "1905", "1940", "1931", "Musashi.jpg")
q15 = Questions("У якому році ввели у стрій авіаносець Shinano", "1944", "1914", "1940", "1951", "Shinano.jpg")
q16 = Questions("У якому році ввели у стрій лінкор Kongo", "1942", "1913", "1940", "1976", "Kongo.jpg")
q17 = Questions("У якому році ввели у стрій лінкор Iowa", "1942", "1905", "1943", "1911", "Iowa.jpg")
q18 = Questions("У якому році ввели у стрій лінкор Royal Oak", "1942", "1905", "1914", "1963", "Royal Oak.jpg")
q19 = Questions("У якому році ввели у стрій лінкор Hood", "1942", "1918", "1940", "1945", "Hood.jpg")

quest_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19]