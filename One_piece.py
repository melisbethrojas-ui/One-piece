#MENUS
menu00= "Menu 0 (One Piece)".center(40,"=")+"\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit\n"
menu02 = "Menu02 Create".center(40,"=")+"\n1)Create Character\n2)Create Weapon\n3)Go back\n"
menu021="Menu021 New Character".center(40,"=")
menu022= "Menu022 (New Weapon)".center(40, "=")
menu03= "Menu 03 (Edit Menu)".center(40,"=")+"\n1)Edit character\n2)Edit weapon\n3)Go back\n"
menu031= "Menu 031 (Select Caracter to Edit)".center(40,"=")
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
flg_03=False
flg_04=False
salir = False
while not salir:
    print(menu00)
    opc=input("->Option: ")
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
            flg_00=False
            flg_03=True
        elif opc == 4:
            flg_00=False
            flg_04=True
        elif opc == 5:
            salir = True
            print("-"*20+"\nHasta la proxima!\n"+"-"*20)
    #MENU OPC 2
    while flg_02:
        print(menu02)
        opc=input("->Option: ")
        if not opc.isdigit():
            print("Invalid Option".center(40,"="))
            input("Press enter to continue")
        elif not (int(opc) in range(1,4)):
            print("Invalid Option".center(40,"="))
            input("Press enter to continue")
        else:
            opc=int(opc)
            if opc == 1:
                flg_021 = False
                flg_00 = True
                #
                # Name: new_character
                # Category: ViceAdmiral
                # Weapons:
                # Strength: 9
                # Speed: 6
                # Experience: 0
                # Save this player S\N
                while flg_021:
                    new_character= input("Name of the new character:\n")
                    new_character.replace(" ","")
                    print("Side of the new character:\n1)Marine\n2)Pirates")
                    opc=input("->Option: ")
                    if not opc.isdigit():
                        print("Invalid Option".center(40,"="))
                        input("Press enter to continue")
                    elif not (int(opc) in range(1,3)):
                        print("Invalid Option".center(40,"="))
                        input("Press enter to continue")
                    else:
                        if opc == 1:
                            print("1) Admiral 2) ViceAdmiral 3) lieutenant")
                    # else:
                    #     print("Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) lieutenant")
                    #     opc=input("->Option: ")
                    #     if not opc.isdigit():
                    #         print("Invalid Option".center(40,"="))
                    #         input("Press enter to continue")
                    #     elif not (int(opc) in range(1,4)):
                    #         print("Invalid Option".center(40,"="))
                    #         input("Press enter to continue")
                    #     #else:

            elif opc == 2:
                print("Create Weapons")
            elif opc == 3:
                flg_00= True
                flg_02=False

    while flg_03:
        print(menu03)
        opc = input("->Option: ")
        if not opc.isdigit():
            print("Invalid Option".center(30, "="))
            input("Enter to continue")
        elif not (int(opc) in range(1, 4)):
            print("Invalid Option".center(30, "="))
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc == 1:
                flg_03 = False
                flg_031 = True
                flg_0311 = False
                while flg_031:
                    print(menu031)
                    flg_0311 = False
                    flg_031 = True
                    menu_edit= "1)Name\n2)Weapons\n3)Go Back"
                    #Ver personajes a editar
                    for id in dict_characters:
                        mostrar_character = dict_characters[id]
                        #Convertir weapons en nombres
                        weapons_str = ""
                        for w in mostrar_character["weapons"]:
                            if weapons_str == "":
                                weapons_str = dict_weapons[w]["name"]
                            else:
                                weapons_str = weapons_str+ "," + dict_weapons[w]["name"]
                        print("ID: {},Name: {},Category: {},Weapons: {},Strength: {},Speed: {},Experience: {}".format(
                        id,
                        mostrar_character["name"],
                        dict_categorys[mostrar_character["category"]],
                        weapons_str,
                        mostrar_character["strength"],
                        mostrar_character["speed"],
                        mostrar_character["experience"]))
                    id_personaje=int(input("ID to edit:\n"))
                    if id_personaje in dict_characters:
                        personaje = dict_characters[id_personaje]
                        print("Select feature to edit to character ID:{}, Name: {} ".format(id_personaje,personaje["name"]))
                        flg_0311= True
                        flg_031 = False
                        while flg_0311:
                            print(menu_edit)
                            opc_edit = input("->Option: ")
                            if not opc_edit.isdigit():
                                print("Invalid Option".center(30, "="))
                                input("Enter to continue")
                            elif not (int(opc_edit) in range(1, 4)):
                                print("Invalid Option".center(30, "="))
                                input("Enter to continue")
                            else:
                                opc_edit=int(opc_edit)
                                #editar nombre
                                if opc_edit == 1:
                                    name_edit= input("Enter the new name:\n")
                                    name_edit.replace(" ","")
                                    opc_save=input("Do you want to change name {} by {}?\n".format(personaje["name"],name_edit))
                                    while opc_save.lower() != "n" and opc_save.lower() != "y":
                                        print("wrong option")
                                        opc_save = input(
                                            "Do you want to change name {} by {}?\n".format(personaje["name"], name_edit))
                                    if opc_save.lower() == "y":
                                        personaje["name"] = name_edit
                                        flg_0311 = False
                                        flg_031 = False
                                        flg_03 = False
                                        flg_00 = True
                                    elif opc_save.lower() == "n":
                                        print("Don't save changes")
                                        flg_0311 = False
                                        flg_031 = False
                                        flg_03 = False
                                        flg_00 = True


                                #editar armas del personaje
                                elif opc_edit == 2:
                                    rangelist= []
                                    armas_disponibles= "Available Weapons".center(40,"=")
                                    armas_personajes = "Character Weapons:".center(40,"=")
                                    sin_armas="None".center(30,"-")
                                    for w in personaje["weapons"]:
                                        rangelist.append(w)
                                    print("rangelist = ",rangelist)
                                    print(armas_disponibles)
                                    if len(dict_weapons) == 0:
                                        print(sin_armas)
                                    else:
                                        for a in dict_weapons:
                                            armas= dict_weapons[a]
                                        print(armas_personajes)
                                        print("{} ) {}, Strength: {}, Speed {}".format(a, armas["name"], armas["strength"], armas["speed"]))
                                        flg_0311 = False
                                        flg_031 = False
                                        flg_03 = False
                                        flg_00 = True
                                elif opc_edit == 3:
                                    flg_0311=False
                                    flg_031 = True

                    flg_00 = True
                    flg_03=False




            elif opc == 2:
                print("Edit Weapons")
            elif opc == 3:
                flg_00 = True
                flg_03=False

# MENU OPC 4
    while flg_04:
        print(menu04_listar)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Invalid Option".center(40, "="))
            input("Enter to continue")
        elif not (int(opc) in range(1, 6)):
            print("Invalid Option".center(40, "="))
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == 1:
                flg_041 = True
                flg_04 = False
                while flg_041:
                    print(menu041_listcharacters)
                    opc = input("Option:\n")
                    if not opc.isdigit():
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    elif not (int(opc) in range(1, 6)):
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            print("List by ID")
                            datos_id = ""
                            cabecera_character_id = "Characters ordered by ID".center(60,
                                                                                      "=") + "\n" + "{:>3}{:>15}{:>15}{:>10}{:>15}".format(
                                "ID",
                                "Name", "strength",
                                "speed",
                                "experience") + "\n" + "*" * 60
                            list_characters = list(dict_characters.keys())
                            print(cabecera_character_id)

                            # ORDENAR ID
                            for pasada in range(len(list_characters) - 1):
                                cambio = False

                                for i in range(len(list_characters) - 1 - pasada):
                                    if list_characters[i] > list_characters[i + 1]:
                                        cambio = True
                                        aux = list_characters[i]
                                        list_characters[i] = list_characters[i + 1]
                                        list_characters[i + 1] = aux

                                if not cambio:
                                    break

                            # PARA MOSTRAR
                            for id in list_characters:
                                # dict_characters[id]
                                suma_fuerza = dict_characters[id]["strength"]
                                suma_velocidad = dict_characters[id]["speed"]

                                for arma_id in dict_characters[id]["weapons"]:
                                    # dict_weapons[arma_id]
                                    suma_fuerza = suma_fuerza + dict_weapons[arma_id]["strength"]
                                    suma_velocidad = suma_velocidad + dict_weapons[arma_id]["speed"]

                                datos_id = datos_id + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id][
                                    "name"],
                                                                                         suma_fuerza,
                                                                                         suma_velocidad,
                                                                                         dict_characters[id][
                                                                                             "experience"])
                            print(datos_id)
                            input("Enter to continue")
                        elif opc == 2:
                            print("List by name")
                            datos_name = ""
                            list_characters = list(dict_characters.keys())
                            cabecera_character_name = "Characters ordered by NAME".center(60, "=") + "\n" + "{:>3}{:>15}{:>15}{:>10}{:>15}".format("ID","Name","Strength","Speed","Experience")+ "\n" + "*" * 60
                            print(cabecera_character_name)
                            for pasada in range(len(list_characters) - 1):
                                cambio = False
                                for i in range(len(list_characters) - 1 - pasada):
                                    nombre_inicial = dict_characters[list_characters[i]]["name"]
                                    nombre_siguiente = dict_characters[list_characters[i + 1]]["name"]

                                    if nombre_inicial > nombre_siguiente:
                                        cambio = True
                                        aux = list_characters[i]
                                        list_characters[i] = list_characters[i + 1]
                                        list_characters[i + 1] = aux
                                if not cambio:
                                    break

                            for id in list_characters:
                                # dict_characters[id]
                                suma_fuerza = dict_characters[id]["strength"]
                                suma_velocidad = dict_characters[id]["speed"]

                                for arma_id in dict_characters[id]["weapons"]:
                                    # dict_weapons[arma_id]
                                    suma_fuerza = suma_fuerza + dict_weapons[arma_id]["strength"]
                                    suma_velocidad = suma_velocidad + dict_weapons[arma_id]["speed"]

                                datos_name = datos_name + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                        suma_fuerza,
                                                                                        suma_velocidad,
                                                                                        dict_characters[id]["experience"])

                            print(datos_name)
                        elif opc == 3:
                            print("List by StreNght")
                            datos_strength = ""
                            list_characters = list(dict_characters.keys())
                            cabecera_character_strength = "Characters ordered by STRENGTH".center(60, "=") + "\n" + "{:>3}{:>15}{:>15}{:>10}{:>15}".format("ID","Name","Strength","Speed","Experience")+ "\n" + "*" * 60
                            print(cabecera_character_strength)

                            for pasada in range(len(list_characters)-1):
                                cambio = False

                                for i in range(len(list_characters)-1-pasada):
                                    # cogue el valor de fuerza del personaje
                                    suma_fuerza = dict_characters[list_characters[i]]["strength"]

                                    # suma la fuerza del primer personaje
                                    for arma_id in dict_characters[list_characters[i]]["weapons"]:
                                        suma_fuerza = suma_fuerza + dict_weapons[arma_id]["strength"]

                                    suma_fuerza_siguiente = dict_characters[list_characters[i+1]]["strength"]
                                    #suma la fuerza del siguiente

                                    for arma_id in dict_characters[list_characters[i+1]]["weapons"]:
                                        suma_fuerza_siguiente = suma_fuerza_siguiente +  dict_weapons[arma_id]["strength"]

                                    if suma_fuerza > suma_fuerza_siguiente:
                                        cambio = True
                                        aux = list_characters[i]
                                        list_characters[i] = list_characters[i+1]
                                        list_characters[i+1]= aux

                                if not cambio:
                                    break

                            for id in list_characters:
                                # dict_characters[id]
                                suma_fuerza = dict_characters[id]["strength"]
                                suma_velocidad = dict_characters[id]["speed"]

                                for arma_id in dict_characters[id]["weapons"]:
                                    # dict_weapons[arma_id]
                                    suma_fuerza = suma_fuerza + dict_weapons[arma_id]["strength"]
                                    suma_velocidad = suma_velocidad + dict_weapons[arma_id]["speed"]

                                datos_strength = datos_strength + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                            suma_fuerza,
                                                                                            suma_velocidad,
                                                                                            dict_characters[id]["experience"])
                            print(datos_strength)
                        elif opc == 4:
                            print("List by speed")
                            #  Listar personajes POR SPEED
                            datos_speed = ""
                            list_characters = list(dict_characters.keys())
                            cabecera_character_speed = "Characters ordered by SPEED".center(60, "=") + "\n" + "{:>3}{:>15}{:>15}{:>10}{:>15}".format("ID","Name","Strength","Speed","Experience")+ "\n" + "*" * 60
                            print(cabecera_character_speed)
                            for pasada in range(len(list_characters)-1):
                                cambio = False

                                for i in range(len(list_characters)-1-pasada):
                                    # cogue el valor de fuerza del personaje
                                    suma_velocidad = dict_characters[list_characters[i]]["speed"]

                                    # suma la fuerza del primer personaje
                                    for arma_id in dict_characters[list_characters[i]]["weapons"]:
                                        suma_velocidad = suma_velocidad+ dict_weapons[arma_id]["speed"]

                                    suma_velocidad_siguiente = dict_characters[list_characters[i+1]]["speed"]

                                    #suma la fuerza del siguiente
                                    for arma_id in dict_characters[list_characters[i+1]]["weapons"]:
                                        suma_velocidad_siguiente = suma_velocidad_siguiente +  dict_weapons[arma_id]["speed"]

                                    if suma_velocidad > suma_velocidad_siguiente:
                                        cambio = True
                                        aux = list_characters[i]
                                        list_characters[i] = list_characters[i+1]
                                        list_characters[i+1]= aux

                                if not cambio:
                                    break

                            for id in list_characters:
                                # dict_characters[id]
                                suma_fuerza = dict_characters[id]["strength"]
                                suma_velocidad = dict_characters[id]["speed"]

                                for arma_id in dict_characters[id]["weapons"]:
                                    # dict_weapons[arma_id]
                                    suma_fuerza = suma_fuerza + dict_weapons[arma_id]["strength"]
                                    suma_velocidad = suma_velocidad + dict_weapons[arma_id]["speed"]


                                datos_speed = datos_speed + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                            suma_fuerza,
                                                                                            suma_velocidad,
                                                                                            dict_characters[id]["experience"])
                            print(datos_speed)
                        elif opc == 5:
                            flg_041 = False
                            flg_04 = True
            elif opc == 2:
                flg_042 = True
                flg_04 = False
                while flg_042:
                    print(menu042_listweapons)
                    opc = input("Option:\n")
                    if not opc.isdigit():
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    elif not (int(opc) in range(1, 6)):
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            print("List by ID")
                        elif opc == 2:
                            print("List by name")
                        elif opc == 3:
                            print("List by Streght")
                        elif opc == 4:
                            print("List by speed")
                        elif opc == 5:
                            flg_042 = False
                            flg_04 = True
            elif opc == 3:
                print("List Side")
            elif opc == 4:
                print("List Range")
            elif opc == 5:
                flg_04=False
                flg_00= True