import mysql.connector
from mysql.connector import Error

marks = {}
word_freq = {
             '1968': ["The Hong Kong flu, also known as the 1968 flu pandemic, was a flu pandemic whose outbreak in 1968 and 1969 killed between one and four million people globally","NO"],
             '1981': ["The global pandemic of HIV/AIDS (human immunodeficiency virus infection and acquired immunodeficiency syndrome) began in 1981, and is an ongoing worldwide public health issue","NO"],
             '1857': ["The Indian Rebellion of 1857 was a major uprising in India in 1857–58 against the rule of the British East India Company, which functioned as a sovereign power on behalf of the British Crown","NO"],
             '1920': ["Though the United States was founded under democratic principles, only a minority of its population – in the beginning only white landowning males over the age of 21 – could actually vote. But after the 19th Amendment of the Constitution was passed, women finally gain a voice and the right to cast their ballots, though the voting rights fight was far from over for many African American women, especially in the South","Yes"],
             '1921': ["In a prequel to the rise of Mao Zedong and Red China, the Chinese Communist Party is founded and three weeks later it convenes its first National Congress that is attended by Mao. It would take another 28 years before the Republic of China becomes the People's Republic of China.","Yes"],
             '1927': ['When the monoplane The Spirit of St. Louis touches down at Le Bourget Field in Paris on the evening of May 21, Charles Lindbergh becomes the first person to fly over the Atlantic Ocean nonstop, making him one of the heroes of the age. His feat fires the imagination of aspiring aviators about the commercial possibilities of fligh',"Yes"]
             
             }

print("  -------MENU------")
print(" a – Add travel log \n d – Remove travel log \n u – Update travel log \n o – Output entire log in console \n s – Save travel log to database \n q – Quit")


while(1):
    x = input("Selected option is ")
    if(x=='a'):
        year = input("Enter Year: ")
        marks[year.title()] = word_freq[year]
        print("What you see: ",word_freq[year][0],"\nYou want to visit again: ",word_freq[year][1])

    elif(x=='d'):
        delete = input("Enter Year: ")
        marks.pop(delete)
        print("successfully Deleted")
    elif(x=='u'):
        update = input("Enter the year:  ")
        revisit = input("Update the Revisit:  ")
        marks[update][1]=revisit
    elif(x=='o'):
        print(marks)

    elif(x=='s'):
        def getList(dict):
            list = []
            for key in dict.keys():
                list.append(key)  
            return list
        b=getList(marks)
        res = [eval(i) for i in b]
        db = mysql.connector.connect(host="cis3368dall.cmjen6ln1nx7.us-east-2.rds.amazonaws.com",    # your host, usually localhost
                             user="admin",         # your username
                             passwd="pakistan123",  # your password
                             db="CIS3368")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        cur = db.cursor()
        for i in range(len(marks)):
            sql = ("INSERT INTO CIS3368.log(log_year, log_comment,revisit) VALUES (%s, %s,%s)", (res[i], marks[str(res[i])][0], marks[str(res[i])][1]))
            cur.execute(*sql)
            db.commit()
        marks={}
    elif(x=='q'):
        print("Quit")
        break;
        