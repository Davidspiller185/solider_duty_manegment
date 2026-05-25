from solider_manager import add_solider,remove_solider,get_all_solider
from duty_manager import add_duty_to_solider,update_duty_status,get_solider_duties

def show_menu()->None:#הצגת התפריט
     print("to add soliter press:1")
     print("to delete soliter press:2")
     print("to view list of soliter press:3")
     print("to exit press:4")

def get_user_choic()->str:#לקבל בחירה מהמשתמש
    choice=input("choice oppsion")
    return choice 

def handle_add_solider()->None:#טיפול בהוספת חייל חדש
    id=int(input("Enter id of soliter"))
    name=input("Enter a name of solider")
    add_solider(id,name)


def handle_remove_solider()->None:#מטפל בהסרת חייל
    id=int(input("Enter the id of the solder"))
    remove_solider(id)
    

def handle_view_soliders():#מטפל בהצגת כל החיילים
    lst=get_all_solider()
    print(f"the lst solder is {lst}")

def handle_add_duty():#מטפל בהוספת תורנות לחייל 
    id=int(input("Enter the solider id"))
    duty=input("Enter a duty please")
    day=input("Enter a day for the duty")
    add_duty_to_solider(id,duty,day)


def handle_update_duty_status():#מטפל בעדכון סטטוס תורנות
    id=int(input("Enter solider id"))
    name=input("Enter the duty name")
    status=input("Enter the new status")
    update_duty_status(id,name,status)


def handle_view_solider_duties():#מטפל בהצגת תורנויות של חייל
    id=int(input("Enter id solider"))
    solider_duties=get_solider_duties(id)
    print(solider_duties)



def main():#הפונקצייה  הראשית 
   # https://github.com/Davidspiller185/solider_duty_manegment
   choice=""
   while choice!="4":
       show_menu()
       choice=get_user_choic()
       match choice:
           case "1":
               handle_add_solider()
           case "2":
               handle_remove_solider()
           case "3":
               handle_view_soliders()
           case "4":
               print("Exit from the solider_duty_managment")
if __name__=="__main__":
    main()               
       
 