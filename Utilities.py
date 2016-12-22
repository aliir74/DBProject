import datetime as t


def getFormattedDate():
    formattedDate = ("" + str(t.datetime.now().year) + "-"
                           + str(t.datetime.now().month) + "_"
                           + str(t.datetime.now().day) + " "
                           + str(t.datetime.now().hour) + ":"
                           + str(t.datetime.now().minute) + ":"
                           + str(t.datetime.now().second) +"" )
    return formattedDate