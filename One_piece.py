#MENUS
menu00= "Menu 0 (One Piece)".center(40,"=")+"\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit\n"
menu02 = "Menu02 Create".center(40,"=")+"\n1)Create Character\n2)Create Weapon\n3)Go back\n"
menu021="Menu021 New Character".center(40,"=")
menu022= "Mennu022 (New Weapon)".center(40, "=")
menu04_listar = "Menu04 (List)".center(40,"=")+"\n1)List Characters\n2)List Weapons\n3)List Side\n4)List Range\n5)Go back"
menu041_listcharacters = "Menu041 (List Characters)".center(40,"=")+"\n1)List by ID\n2)List by name\n3)List bu Streght\n4)List by speed\n5)Go back"
menu042_listweapons = "Menu042 (List Weapons)".center(40,"=")+"\n1)List by ID\n2)List by name\n3)List bu Streght\n4)List by speed\n5)Go back"


#DICCIONARIOS
dict_characters = {
    1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :7,"experience": 0},
    2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":0},
    3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :6,"experience": 0 },
    4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4,"experience" : 0},
    5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience": 0},
    6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,"experience" : 0},
    7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,"experience" : 0},
    8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,"experience" : 0},
    9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,"experience" : 0},
    10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,"experience" : 0},
    11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,"experience" : 0},
    12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,"experience" : 0},
    13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,"experience" : 0},
    14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,"experience" : 0},
    15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,"experience" : 0},
 }
dict_weapons = { 
    1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
    2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
    3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
    4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
    5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
 }
dict_crews = { 
    1 : {"name" : "Straw hat","members": [8,6]},
    2 : {"name" : "Pirates Buggy","members": [1,3,5]},
    3: {"name": "Pirates Rocks","members": [2,4,7,]}
 }
dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
 2 : {"name" : "ViceAdmiral","members": [12,13]},
 3: {"name": "Lieutenant","members": [14,15]}
 }
dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

flg_00=True
flg_02=False
flg_021=False
flg_04=False
salir = False
while not salir:
    print(menu00)
    opc=input("Option:\n")
    if not opc.isdigit():
        print("Invalid Option".center(30,"="))
        input("Enter to continue")
    elif not (int(opc) in range(1,6)):
        print("Invalid Option".center(30,"="))
        input("Enter to continue")
    else:
        opc=int(opc)
        if opc == 1:
            print("Play")
        elif opc == 2:
            flg_00=False
            flg_02=True
        elif opc == 3:
            print("Edit")
        elif opc == 4:
            flg_00=False
            flg_04=True
        elif opc == 5:
            salir = True
            print("-"*20+"\nHasta la proxima!\n"+"-"*20)
    #MENU OPC 2
    while flg_02:
        print(menu02)
        opc=input("Option:\n")
        if not opc.isdigit():
            print("Invalid Option".center(40,"="))
            input("Enter to continue")
        elif not (int(opc) in range(1,4)):
            print("Invalid Option".center(40,"="))
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc == 1:
                print("Create Character")
            elif opc == 2:
                print("Create Weapons")
            elif opc == 3:
                flg_00= True
                flg_02=False

    #MENU OPC 4
    while flg_04:
        print(menu04_listar)
        opc=input("Option:\n")
        if not opc.isdigit():
            print("Invalid Option".center(40,"="))
            input("Enter to continue")
        elif not (int(opc) in range(1,6)):
            print("Invalid Option".center(40,"="))
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc == 1:
                flg_041=True
                flg_04=False
                while flg_041:
                    print(menu041_listcharacters)
                    opc=input("Option:\n")
                    if not opc.isdigit():
                        print("Invalid Option".center(40,"="))
                        input("Enter to continue")
                    elif not (int(opc) in range(1,6)):
                        print("Invalid Option".center(40,"="))
                        input("Enter to continue")
                    else:
                        opc=int(opc)
                        if opc == 1:
                            print("List by ID")
                        elif opc == 2:
                            print("List by name")
                        elif opc == 3:
                            print("List by Streght")
                        elif opc == 4:
                            print("List by speed")
                        elif opc == 5:
                            flg_041=False
                            flg_04=True
            elif opc == 2:
                flg_042=True
                flg_04=False
                while flg_042:
                    print(menu042_listweapons)
                    opc=input("Option:\n")
                    if not opc.isdigit():
                        print("Invalid Option".center(40,"="))
                        input("Enter to continue")
                    elif not (int(opc) in range(1,6)):
                        print("Invalid Option".center(40,"="))
                        input("Enter to continue")
                    else:
                        opc=int(opc)
                        if opc == 1:
                            print("List by ID")
                        elif opc == 2:
                            print("List by name")
                        elif opc == 3:
                            print("List by Streght")
                        elif opc == 4:
                            print("List by speed")
                        elif opc == 5:
                            flg_042=False
                            flg_04=True
            elif opc == 3:
                print("List Side")
            elif opc == 4:
                print("List Range")