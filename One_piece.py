#MENUS
menu00= "Menu 0 (One Piece)".center(40,"=")+"\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit\n" #MENU PRINCIPAL
menu02 = "Menu02 Create".center(40,"=")+"\n1)Create Character\n2)Create Weapon\n3)Go back\n" #MENU CREAR
menu021="Menu021 New Character".center(40,"=") #MENU CREAR PERSONAJE
menu_cat = "Side of the new character:\n1)Marine\n2)Pirates" #MENU CATEGORIA
menu_cat_m = "Range or crew of the new character:\n1) Admiral\n2) ViceAdmiral\n3) Lieutenant" #MENU CATEGORIA MARINES
menu_cat_p = "Range or crew of the new character:\n1) Straw hat\n2) Pirates Buggy\n3) Pirates Rocks" #MENU CATEGORIA PIRATAS
menu022= "Menu022 (New Weapon)".center(40, "=") #MENU CREAR ARMA
menu03= "Menu 03 (Edit Menu)".center(40,"=")+"\n1)Edit character\n2)Edit weapon\n3)Go back\n" #MENU EDITAR
menu031= "Menu 031 (Select Character to Edit)".center(40,"=") #MENU EDITAR PERSONAJE
menu032= "Menu 032 (Select Weapon to Edit)".center(40, "=") #MENU EDITAR ARMAS
menu032X= "Menu 032X (Weapon Feature to Edit)".center(40,"=")+"\n1)Name\n2)Plus Strength\n3)Plus speed\n4)Go back\n" #MENU EDITAR ARMAS 2
menu04_listar = "Menu04 (List)".center(40,"=")+"\n1)List Characters\n2)List Weapons\n3)List Side\n4)List Range\n5)Go back"
menu041_listcharacters = "Menu041 (List Characters)".center(40,"=")+"\n1)List by ID\n2)List by name\n3)List bu Streght\n4)List by speed\n5)Go back"
menu042_listweapons = "Menu042 (List Weapons)".center(40,"=")+"\n1)List by ID\n2)List by name\n3)List bu Streght\n4)List by speed\n5)Go back"
cabecera_weapon_id = "Characters ordered by ID".center(60,"=")+ "\n"+"{:>3}{:>15}{:>15}{:>10}{:>15}".format("ID","Name","strength","speed","two_hand")+"\n"+"*"*60+"\n"


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
        opc = input("->Option: ")
        if not opc.isdigit():
            print("Invalid Option".center(40, "="))
            input("Press enter to continue")
        elif not (int(opc) in range(1, 4)):
            print("Invalid Option".center(40, "="))
            input("Press enter to continue")
        else:
            opc = int(opc)
            if opc == 1:
                flg_021 = True
                flg_00 = False

                while flg_021:
                    nombre_personaje = input("Name of the new character:\n")
                    print(menu_cat)
                    opc = input("->Option: ")
                    if not opc.isdigit():
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                    elif not (int(opc) in range(1, 3)):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            print(menu_cat_m)
                            opc_create = input("->Option: ")

                            if not opc_create.isdigit():
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue")
                            elif not (int(opc_create) in range(1, 4)):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue")
                            else:
                                opc_create = int(opc_create)
                                if opc_create == 1:
                                    categoria = 4
                                    fuerza = 5
                                    velocidad = 6
                                elif opc_create == 2:
                                    categoria = 5
                                    fuerza = 7
                                    velocidad = 6
                                elif opc_create == 3:
                                    categoria = 6
                                    fuerza = 5
                                    velocidad = 5

                                new_character = {"name": nombre_personaje,"category": categoria,"weapons": [],
                                                 "strength": fuerza,"speed": velocidad,"experience": 0}

                                # Escoger armas
                                armas_disponibles = "Available Weapons".center(40, "=")
                                armas_personajes = "Character Weapons:".center(40, "=")
                                sin_armas = "None".center(30, "-")
                                agregar_armas = "Add Weapons:\nWeapon Id) To add weapon Id\n0) Finish add weapons\n-Weapon Id) Delete weapon Id"
                                flg_escoger_armas = True

                                while flg_escoger_armas:
                                    rangelist = []
                                    puede_elegir_mas = True

                                    if len(new_character["weapons"]) >= 2:
                                        puede_elegir_mas = False

                                    # Revisar si ya tiene un arma de dos manos
                                    tiene_two_hand = False
                                    for w in new_character["weapons"]:
                                        if dict_weapons[w]["two_hand"]:
                                            tiene_two_hand = True
                                            puede_elegir_mas = False
                                            break

                                    # Rangelist con las armas que puede escoger
                                    if puede_elegir_mas:
                                        for a in dict_weapons:
                                            arma = dict_weapons[a]
                                            if tiene_two_hand and not arma["two_hand"]:
                                                continue
                                            if len(new_character["weapons"]) == 1 and not \
                                            dict_weapons[new_character["weapons"][0]]["two_hand"]:
                                                if arma["two_hand"]:
                                                    continue
                                            rangelist.append(a)

                                    # Mostrar rangelist
                                    if len(rangelist) == 0:
                                        print("rangelist = [0]")
                                    else:
                                        print("rangelist =", rangelist)

                                    print(armas_disponibles)

                                    # Mostrar armas disponibles para escoger
                                    if puede_elegir_mas:
                                        for a in dict_weapons:
                                            arma = dict_weapons[a]
                                            if tiene_two_hand and not arma["two_hand"]:
                                                continue
                                            if len(new_character["weapons"]) == 1 and not \
                                            dict_weapons[new_character["weapons"][0]]["two_hand"]:
                                                if arma["two_hand"]:
                                                    continue
                                            print("{} ) {}, Strength: {}, Speed {}".format(
                                                a, arma["name"], arma["strength"], arma["speed"]))
                                    else:
                                        sin_armas = "None".center(30, "-")
                                        print(sin_armas)

                                    print("\n" + armas_personajes)
                                    if len(new_character["weapons"]) == 0:
                                        print(sin_armas)
                                    else:
                                        for w in new_character["weapons"]:
                                            arma = dict_weapons[w]
                                            print("{} ) {}, Strength: {}, Speed {}".format(
                                                w, arma["name"], arma["strength"], arma["speed"]))

                                    print("\n" + agregar_armas)
                                    opc_edit = input("->Option: ")

                                    # Salir
                                    if opc_edit == "0":
                                        flg_escoger_armas = False
                                        flg_02 = True

                                    elif len(opc_edit) > 1 and opc_edit[0] == "-" and opc_edit[1:].isdigit():
                                        weapon_id = int(opc_edit[1:])
                                        if weapon_id in new_character["weapons"]:
                                            new_character["weapons"].remove(weapon_id)
                                        else:
                                            print("Invalid Option".center(40, "="))
                                            input("Enter to continue")

                                    elif opc_edit.isdigit():
                                        weapon_id = int(opc_edit)
                                        if puede_elegir_mas and weapon_id in dict_weapons:
                                            new_character["weapons"].append(weapon_id)
                                        else:
                                            print("Invalid Option".center(40, "="))
                                            input("Enter to continue")

                                    else:
                                        print("Invalid Option".center(40, "="))
                                        input("Enter to continue")

                                # Guardar personaje
                                new_id = len(dict_characters) + 1
                                dict_characters[new_id] = new_character
                                fuerza_total = 0
                                velocidad_total = 0
                                new_id = len(dict_characters) + 1
                                dict_characters[new_id] = new_character

                                for w in new_character["weapons"]:
                                    arma = dict_weapons[w]
                                    fuerza_total = fuerza_total + fuerza + arma["strength"]
                                    velocidad_total = velocidad_total + velocidad + arma["speed"]

                                fuerza_total = fuerza_total % 10
                                velocidad_total = velocidad_total % 10

                                # Actualizar personaje
                                new_character["strength"] = fuerza_total
                                new_character["speed"] = velocidad_total

                                # Mostrar los datos del nuevo personaje
                                if len(new_character["weapons"]) == 0:
                                    armas_str = ""
                                else:
                                    armas_str = ""
                                    for w in new_character["weapons"]:
                                        arma = dict_weapons[w]
                                        if armas_str != "":
                                            armas_str = armas_str + ", "
                                        armas_str = armas_str + "{}".format(arma["name"])


                                # Datos del nuevo personaje
                                datos = (("\nThe new player will be:\n\nID: {}\nName: {}\nCategory: {}\nWeapons: {}\nStrength: {}\nSpeed: {}\nExperience: {}\n").format
                                         (new_id,new_character["name"],dict_categorys[new_character["category"]],
                                          armas_str,new_character["strength"],new_character["speed"],new_character["experience"]))

                                print(datos)

                                opc_save = input("Save this player S/N\n")
                                if opc_save.lower() == "s":
                                    print("Player saved!")
                                    flg_021= False
                                    flg_02 = False
                                    flg_00= True
                                else:
                                    print("Player not saved.")
                                    flg_021 = False
                                    flg_02 = False
                                    flg_00 = True

                        elif opc == 2:
                            print(menu_cat_p)
                            opc_create = input("->Option: ")

                            if not opc_create.isdigit():
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue")
                            elif not (int(opc_create) in range(1, 4)):
                                print("Invalid Option".center(40, "="))
                                input("Press enter to continue")
                            else:
                                opc_create = int(opc_create)
                                if opc_create == 1:
                                    categoria = 1
                                    fuerza = 5
                                    velocidad = 6
                                elif opc_create == 2:
                                    categoria = 2
                                    fuerza = 7
                                    velocidad = 6
                                elif opc_create == 3:
                                    categoria = 3
                                    fuerza = 5
                                    velocidad = 5

                                new_character = {"name": nombre_personaje,"category": categoria,"weapons": [],"strength": fuerza,
                                                 "speed": velocidad,"experience": 0}

                                # Escoger armas
                                armas_disponibles = "Available Weapons".center(40, "=")
                                armas_personajes = "Character Weapons:".center(40, "=")
                                sin_armas = "None".center(30, "-")
                                agregar_armas = "Add Weapons:\nWeapon Id) To add weapon Id\n0) Finish add weapons\n-Weapon Id) Delete weapon Id"
                                flg_escoger_armas = True

                                while flg_escoger_armas:
                                        rangelist = []
                                        puede_elegir_mas = True

                                        if len(new_character["weapons"]) >= 2:
                                            puede_elegir_mas = False

                                        # Revisar si ya tiene un arma de dos manos
                                        tiene_two_hand = False
                                        for w in new_character["weapons"]:
                                            if dict_weapons[w]["two_hand"]:
                                                tiene_two_hand = True
                                                puede_elegir_mas = False
                                                break

                                        # Rangelist con las armas que puede escoger
                                        if puede_elegir_mas:
                                            for a in dict_weapons:
                                                arma = dict_weapons[a]
                                                if tiene_two_hand and not arma["two_hand"]:
                                                    continue
                                                if len(new_character["weapons"]) == 1 and not \
                                                        dict_weapons[new_character["weapons"][0]]["two_hand"]:
                                                    if arma["two_hand"]:
                                                        continue
                                                rangelist.append(a)

                                        if len(rangelist) == 0:
                                            print("rangelist = [0]")
                                        else:
                                            print("rangelist =", rangelist)

                                        print(armas_disponibles)

                                        if len(new_character["weapons"]) >= 2:
                                            puede_elegir_mas = False

                                        for w in new_character["weapons"]:
                                            if dict_weapons[w]["two_hand"]:
                                                puede_elegir_mas = False
                                                break

                                        tiene_two_hand = False
                                        for w in new_character["weapons"]:
                                            if dict_weapons[w]["two_hand"]:
                                                tiene_two_hand = True
                                                break

                                        if puede_elegir_mas:
                                            for a in dict_weapons:
                                                arma = dict_weapons[a]
                                                if tiene_two_hand and not arma["two_hand"]:
                                                    continue
                                                if len(new_character["weapons"]) == 1 and not \
                                                        dict_weapons[new_character["weapons"][0]]["two_hand"]:
                                                    if arma["two_hand"]:
                                                        continue
                                                print("{} ) {}, Strength: {}, Speed {}".format(
                                                    a, arma["name"], arma["strength"], arma["speed"]))
                                        else:
                                            print(sin_armas)

                                        print("\n" + armas_personajes)
                                        if len(new_character["weapons"]) == 0:
                                            print(sin_armas)
                                        else:
                                            for w in new_character["weapons"]:
                                                arma = dict_weapons[w]
                                                print("{} ) {}, Strength: {}, Speed {}".format(
                                                    w, arma["name"], arma["strength"], arma["speed"]))

                                        print("\n" + agregar_armas)
                                        opc_edit = input("->Option: ")

                                        if opc_edit == "0":
                                            flg_escoger_armas = False
                                            flg_02 = True

                                        elif len(opc_edit) > 1 and opc_edit[0] == "-" and opc_edit[1:].isdigit():
                                            weapon_id = int(opc_edit[1:])
                                            if weapon_id in new_character["weapons"]:
                                                new_character["weapons"].remove(weapon_id)
                                            else:
                                                print("Invalid Option".center(40, "="))
                                                input("Enter to continue")

                                        elif opc_edit.isdigit():
                                            weapon_id = int(opc_edit)
                                            if puede_elegir_mas and weapon_id in dict_weapons:
                                                new_character["weapons"].append(weapon_id)
                                            else:
                                                print("Invalid Option".center(40, "="))
                                                input("Enter to continue")

                                        else:
                                            print("Invalid Option".center(40, "="))
                                            input("Enter to continue")

                                # Guardar personaje
                                new_id = len(dict_characters) + 1
                                dict_characters[new_id] = new_character
                                fuerza_total = 0
                                velocidad_total = 0
                                new_id = len(dict_characters) + 1
                                dict_characters[new_id] = new_character

                                for w in new_character["weapons"]:
                                    arma = dict_weapons[w]
                                    fuerza_total = fuerza_total + fuerza + arma["strength"]
                                    velocidad_total = velocidad_total + velocidad + arma["speed"]

                                fuerza_total = fuerza_total % 10
                                velocidad_total = velocidad_total % 10

                                # Actualizar personaje
                                new_character["strength"] = fuerza_total
                                new_character["speed"] = velocidad_total

                                # Mostrar los datos del nuevo personaje
                                if len(new_character["weapons"]) == 0:
                                    armas_str = ""
                                else:
                                    armas_str = ""
                                    for w in new_character["weapons"]:
                                        arma = dict_weapons[w]
                                        if armas_str != "":
                                            armas_str = armas_str + ", "
                                        armas_str = armas_str + "{}".format(arma["name"])

                                # Datos del nuevo personaje
                                datos = (("\nThe new player will be:\n\nID: {}\nName: {}\nCategory: {}\nWeapons: {}\nStrength: {}\nSpeed: {}\nExperience: {}\n").format
                                         (new_id, new_character["name"], dict_categorys[new_character["category"]],
                                          armas_str, new_character["strength"], new_character["speed"],
                                          new_character["experience"]))

                                print(datos)

                                opc_save = input("Save this player S/N\n")
                                if opc_save.lower() == "s":
                                    print("Player saved!")
                                    flg_021 = False
                                    flg_02 = False
                                    flg_00 = True
                                else:
                                    print("Player not saved.")
                                    flg_021 = False
                                    flg_02 = False
                                    flg_00 = True
                        elif opc == 3:
                            flg_021 = False
                            flg_02 = True


            # CREACION DE ARMAS
            elif opc == 2:
                flg_022 = True
                while flg_022:
                    print(menu022)

                    # Nombre del arma
                    new_weapon = input("Name of the new weapon:\n")
                    new_weapon.replace(" ","")

                    # añadir fuerza
                    new_strength = input("Weapon Strength 1-9:\n->Strength: ")
                    while not new_strength.isdigit() or int(new_strength) not in range(1, 10):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                        new_strength = input("Weapon Strength 1-9:\n")
                    new_strength = int(new_strength)

                    # añadir velocidad
                    new_speed = input("Weapon Speed 1-9:\n->Speed: ")
                    while not new_speed.isdigit() or int(new_speed) not in range(1, 10):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                        new_speed = input("Weapon Speed 1-9:\n")
                    new_speed = int(new_speed)

                    # tipo de arma una mano o a dos manos
                    print("Kind of Weapon:\n1)One hand\n2)Two hands")
                    opc_hand = input("->Option: ")
                    # siempre que no sea digito o la opcion no sea ni 1 o 2... invalido y se repite
                    while not opc_hand.isdigit() or int(opc_hand) not in (1,2):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                        opc_hand = input("->Option: ")
                    if int(opc_hand) == 2:
                        two_hand = True
                    else:
                        two_hand = False

                    # Confirmar guardado
                    menu_confirmar_guardado = ("Name: {}\nStrength: {}\nSpeed: {}\nTwo hands type: {}"
                                               .format(new_weapon,new_strength,new_speed,two_hand))
                    print(menu_confirmar_guardado)

                    # Confirmar guardado
                    opc_save = input("Save this weapon S/N: ").lower()
                    while opc_save not in ("s", "n"):
                        print("Invalid Option".center(40, "="))
                        input("Press enter to continue")
                        opc_save = input("Save this weapon S/N: ")

                    if opc_save.lower() == "s":
                        # crear nuevo ID automáticamente
                        new_id = len(dict_weapons) + 1
                        dict_weapons[new_id] = {
                            "name": new_weapon,
                            "strength": new_strength,
                            "speed": new_speed,
                            "two_hand": two_hand
                        }
                        print("Saved new weapon with id = {}".format(new_id))
######################################################################################################################

                    # salir del menú de creación
                    flg_022 = False
                    flg_00 = True
            elif opc == 3:
                flg_00= True
                flg_02=False

    # MENU OPC 3
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
                        print("ID: {},Name: {},Category: {},Weapons: {},Strength: {},Speed: {},Experience: {}".format(id,mostrar_character["name"],
                        dict_categorys[mostrar_character["category"]],weapons_str,mostrar_character["strength"],mostrar_character["speed"],mostrar_character["experience"]))

                    id_personaje=int(input("ID to edit:\n"))
                    #comprobar si esta en el diccionario
                    if id_personaje in dict_characters:
                        personaje = dict_characters[id_personaje]
                        print("Select feature to edit to character ID:{}, Name: {} ".format(id_personaje,personaje["name"]))
                        flg_0311= True
                        flg_031 = False

                        #Menu editar
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
                                # Editar nombre del personaje
                                if opc_edit == 1:
                                    name_edit= input("Enter the new name:\n")
                                    opc_save=input("Do you want to change name {} by {}?\n".format(personaje["name"],name_edit))
                                    while opc_save.lower() != "n" and opc_save.lower() != "y":
                                        print("wrong option")
                                        opc_save = input("Do you want to change name {} by {}?\n".format(personaje["name"], name_edit))
                                    # Para guardar los cambios
                                    if opc_save.lower() == "y":
                                        personaje["name"] = name_edit
                                        flg_0311 = False
                                        flg_031 = False
                                        flg_00 = True
                                    # No se guardan los cambios
                                    elif opc_save.lower() == "n":
                                        print("Don't save changes")
                                        flg_0311 = False
                                        flg_031 = False
                                        flg_00 = True


                                # Editar armas del personaje
                                elif opc_edit == 2:
                                    rangelist = []
                                    armas_disponibles = "Available Weapons".center(40, "=")
                                    armas_personajes = "Character Weapons:".center(40, "=")
                                    sin_armas = "None".center(30, "-")
                                    agregar_armas = "Add Weapons:\nWeapon Id) To add weapon Id\n0) Finish add weapons\n-Weapon Id) Delete weapon Id"
                                    flg_0312 = False

                                    # Entrar al menu de editar armas
                                    flg_0312 = True
                                    flg_031 = False
                                    while flg_0312:
                                        rangelist = []
                                        puede_elegir_mas = True

                                        if len(personaje["weapons"]) >= 2:
                                            puede_elegir_mas = False

                                        # Revisar si ya tiene un arma de dos manos
                                        tiene_two_hand = False
                                        for w in personaje["weapons"]:
                                            if dict_weapons[w]["two_hand"]:
                                                tiene_two_hand = True
                                                puede_elegir_mas = False
                                                break

                                        # Llenar rangelist con las armas que puede escoger
                                        if puede_elegir_mas:
                                            for a in dict_weapons:
                                                arma = dict_weapons[a]
                                                if tiene_two_hand and not arma["two_hand"]:
                                                    continue
                                                if len(personaje["weapons"]) == 1 and not \
                                                dict_weapons[personaje["weapons"][0]]["two_hand"]:
                                                    if arma["two_hand"]:
                                                        continue
                                                rangelist.append(a)

                                        # Mostrar rangelist antes del menú
                                        if len(rangelist) == 0:
                                            print("rangelist = [0]")
                                        else:
                                            print("rangelist =", rangelist)

                                        # Mostrar menú
                                        print(armas_disponibles)

                                        if puede_elegir_mas:
                                            for a in rangelist:  
                                                arma = dict_weapons[a]

                                                # Mostrar armas según reglas
                                                print("{} ) {}, Strength: {}, Speed {}".format(
                                                    a, arma["name"], arma["strength"], arma["speed"]))
                                        else:
                                            print(sin_armas)

                                        # Armas actuales del personaje
                                        print("\n" + armas_personajes)
                                        if len(personaje["weapons"]) == 0:
                                            print(sin_armas)
                                        else:
                                            for w in personaje["weapons"]:
                                                arma = dict_weapons[w]
                                                print("{} ) {}, Strength: {}, Speed {}".format(
                                                    w, arma["name"], arma["strength"], arma["speed"]
                                                ))

                                        print("\n" + agregar_armas)
                                        opc_edit = input("->Option: ")

                                        if opc_edit == "0":
                                            flg_0312 = False
                                            flg_0311 = False
                                            flg_031 = False
                                            flg_03 = True

                                        elif len(opc_edit) > 1 and opc_edit[0] == "-" and opc_edit[1:].isdigit():
                                            weapon_id = int(opc_edit[1:])
                                            if weapon_id in personaje["weapons"]:
                                                personaje["weapons"].remove(weapon_id)
                                            else:
                                                print("Invalid Option".center(40, "="))
                                                input("Enter to continue")

                                        elif opc_edit.isdigit():
                                            weapon_id = int(opc_edit)
                                            if puede_elegir_mas and weapon_id in dict_weapons:
                                                personaje["weapons"].append(weapon_id)
                                            else:
                                                print("Invalid Option".center(40, "="))
                                                input("Enter to continue")

                                        else:
                                            print("Invalid Option".center(40, "="))
                                            input("Enter to continue")

                                elif opc_edit == 3:
                                    flg_0311=False
                                    flg_031 = False
                                    flg_03= True


            elif opc == 2:
                flg_032= True
                flg_032x = False
                while flg_032:
                    print(menu032)
                    # Mostrar armas a editar
                    for w in dict_weapons:
                        arma = dict_weapons[w]
                        print("{} ) {}, Strength: {}, Speed {}".format(w, arma["name"], arma["strength"], arma["speed"]))
                    opc_edit_weapon=input("ID weapon to edit:\n")
                    if not opc_edit_weapon.isdigit():
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    elif not int(opc_edit_weapon) in dict_weapons:
                        print("Invalid Option".center(40, "="))
                        input("Enter to continue")
                    else:
                        opc_edit_weapon=int(opc_edit_weapon)
                        arma=dict_weapons[opc_edit_weapon]
                        flg_032= False
                        flg_032x = True

                        # Entramos al menu32X
                        while flg_032x:
                            print(menu032X)
                            print("Select feature to edit to weapon ID: {}, Name: {}".format(opc_edit_weapon,arma["name"]))
                            opc_weapon=  input("->Option: ")
                            if not opc_weapon.isdigit():
                                print("Invalid Option".center(40, "="))
                                input("Enter to continue")
                            elif not (int(opc_weapon) in range(1, 5)):
                                print("Invalid Option".center(40, "="))
                                input("Enter to continue")
                            else:
                                opc_weapon= int(opc_weapon)
                                # Nuevo nombre del arma
                                if opc_weapon == 1:
                                        weapon_edit = input("Enter the new name:\n")
                                        while not weapon_edit.replace(" ","").isalpha():
                                            print("Invalid Option".center(40, "="))
                                            input("Enter to continue")
                                            weapon_edit = input("Enter the new name:\n")
                                        opc_save = input("Do you want to change name {} by {}?\n".format(arma["name"],weapon_edit))
                                        while opc_save.lower() != "n" and opc_save.lower() != "y":
                                            print("wrong option")
                                            opc_save = input("Do you want to change name {} by {}?\n".format(arma["name"],weapon_edit))
                                        # Para guardar los cambios
                                        if opc_save.lower() == "y":
                                                arma["name"] = weapon_edit
                                                flg_032 = False
                                                flg_032x = False
                                                flg_00 = True
                                        # No se guardan los cambios
                                        elif opc_save.lower() == "n":
                                                print("Don't save changes")
                                                flg_032 = False
                                                flg_032x = False
                                                flg_00 = True
                                # Nueva fuerza del arma
                                elif opc_weapon == 2:
                                    new_strength = input("Enter the new strength:\n")
                                    while not new_strength.isdigit() or int(new_strength) not in range(1, 10):
                                        print("Invalid Option".center(40, "="))
                                        input("Enter to continue")
                                        new_strength = input("Enter the new strength:\n")

                                    opc_save = input("Do you want to change Strength {} by {} in the weapon {}?\n".format(arma["strength"],
                                                                                                                                  new_strength,arma["name"]))
                                    while opc_save.lower() != "n" and opc_save.lower() != "y":
                                            print("wrong option")
                                            opc_save = input("Do you want to change Strength {} by {} in the weapon {}?\n".format(arma["strength"],
                                                                                                                                      new_strength,arma["name"]))
                                    # Para guardar los cambios
                                    if opc_save.lower() == "y":
                                                arma["strength"] = int(new_strength)
                                                flg_032 = False
                                                flg_032x = False
                                                flg_00 = True
                                    # No se guardan los cambios
                                    elif opc_save.lower() == "n":
                                                print("Don't save changes")
                                                flg_032 = False
                                                flg_032x = False
                                                flg_00 = True

                                # Nueva velocidad del arma
                                elif opc_weapon ==3:
                                    new_speed = input("Enter the new Speed:\n")
                                    while not new_speed.isdigit() or int(new_speed) not in range(1, 10):
                                        print("Invalid Option".center(40, "="))
                                        input("Enter to continue")
                                        new_speed = input("Enter the new Speed:\n")

                                    opc_save = input("Do you want to change Speed {} by {} in the weapon {}?\n".format(arma["speed"],
                                                new_speed, arma["name"]))
                                    while opc_save.lower() != "n" and opc_save.lower() != "y":
                                            print("wrong option")
                                            opc_save = input(
                                                "Do you want to change Speed {} by {} in the weapon {}?\n".format(
                                                    arma["speed"],
                                                    new_speed, arma["name"]))
                                    # Para guardar los cambios
                                    if opc_save.lower() == "y":
                                            arma["speed"] = int(new_speed)
                                            flg_032 = False
                                            flg_032x = False
                                            flg_00 = True
                                    # No se guardan los cambios
                                    elif opc_save.lower() == "n":
                                            print("Don't save changes")
                                            flg_032 = False
                                            flg_032x = False
                                            flg_00 = True
                                # Salir
                                elif opc_weapon == 4:
                                    flg_032= False
                                    flg_032x= False
                                    flg_03= True





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
                            datos_id_character = ""
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

                                datos_id_character = datos_id_character + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id][
                                    "name"],
                                                                                         suma_fuerza,
                                                                                         suma_velocidad,
                                                                                         dict_characters[id][
                                                                                             "experience"])
                            print(datos_id_character)
                            input("Enter to continue")
                        elif opc == 2:
                            print("List by name")
                            datos_name_character = ""
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

                                datos_name_character = datos_name_character + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                        suma_fuerza,
                                                                                        suma_velocidad,
                                                                                        dict_characters[id]["experience"])

                            print(datos_name_character)
                        elif opc == 3:
                            print("List by StreNght")
                            datos_strength_character = ""
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

                                datos_strength_character = datos_strength_character + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                            suma_fuerza,
                                                                                            suma_velocidad,
                                                                                            dict_characters[id]["experience"])
                            print(datos_strength_character)
                        elif opc == 4:
                            print("List by speed")
                            #  Listar personajes POR SPEED
                            datos_speed_character = ""
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


                                datos_speed_character = datos_speed_character + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_characters[id]["name"],
                                                                                            suma_fuerza,
                                                                                            suma_velocidad,
                                                                                            dict_characters[id]["experience"])
                            print(datos_speed_character)
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
                            list_weapons = list(dict_weapons.keys())
                            datos_id_arma = ""
                            print(cabecera_weapon_id)

                            # ORDENAR ID
                            for pasada in range(len(list_weapons)-1):
                                cambio = False

                                for i in range(len(list_weapons)-1-pasada):
                                    if list_weapons[i] > list_weapons[i+1]:
                                        cambio = True
                                        aux = list_weapons[i]
                                        list_weapons[i] = list_weapons[i+1]
                                        list_weapons[i+1]= aux

                                if not cambio:
                                    break

                            # PARA MOSTRAR
                            for id in list_weapons:
                                # dict_characters[id]
                                arma =""

                                if dict_weapons[id]["two_hand"]:
                                    arma = "True"
                                else:
                                    arma = "False"
                                datos_id_arma = datos_id_arma + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_weapons[id]["name"],
                                                                                            dict_weapons[id]["strength"],
                                                                                            dict_weapons[id]["speed"],
                                                                                            arma)
                            print(datos_id_arma)
                        elif opc == 2:
                            print("List by name")
                            # Listar armas POR NAME
                            print(cabecera_weapon_id)
                            list_weapons = list(dict_weapons.keys())
                            datos_name_arma = ""

                            for pasada in range(len(list_weapons)-1):
                                cambio = False

                                for i in range(len(list_weapons)-1-pasada):
                                    nombre_arma_inicial = dict_weapons[list_weapons[i]]["name"]
                                    nombre_arma_siguiente = dict_weapons[list_weapons[i + 1]]["name"]
                                    if nombre_arma_inicial > nombre_arma_siguiente:
                                        cambio = True
                                        aux = list_weapons[i]
                                        list_weapons[i] = list_weapons[i+1]
                                        list_weapons[i+1]= aux

                                if not cambio:
                                    break

                            for id in list_weapons:
                                arma = ""

                                if dict_weapons[id]["two_hand"]:
                                    arma = "True"
                                else:
                                    arma = "False"
                                datos_name_arma =  datos_name_arma + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_weapons[id]["name"],
                                                                                                                        dict_weapons[id]["strength"],
                                                                                                                        dict_weapons[id]["speed"],
                                                                                                                        arma)

                            print(datos_name_arma)
                        elif opc == 3:
                            print("List by Strenght")
                            print(cabecera_weapon_id)
                            list_weapons = list(dict_weapons.keys())
                            datos_strength_arma = ""

                            for pasada in range(len(list_weapons)-1):
                                cambio = False

                                for i in range(len(list_weapons)-1-pasada):
                                    fuerza_arma_inicial = dict_weapons[list_weapons[i]]["strength"]
                                    fuerza_arma_siguiente = dict_weapons[list_weapons[i + 1]]["strength"]
                                    if fuerza_arma_inicial > fuerza_arma_siguiente:
                                        cambio = True
                                        aux = list_weapons[i]
                                        list_weapons[i] = list_weapons[i+1]
                                        list_weapons[i+1]= aux

                                if not cambio:
                                    break

                            for id in list_weapons:
                                arma = ""

                                if dict_weapons[id]["two_hand"]:
                                    arma = "True"
                                else:
                                    arma = "False"
                                datos_strength_arma =  datos_strength_arma + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_weapons[id]["name"],
                                                                                                                        dict_weapons[id]["strength"],
                                                                                                                        dict_weapons[id]["speed"],
                                                                                                                        arma)

                            print(datos_strength_arma)
                        elif opc == 4:
                            print("List by speed")
                            print(cabecera_weapon_id)
                            list_weapons = list(dict_weapons.keys())
                            datos_speed_arma = ""

                            for pasada in range(len(list_weapons)-1):
                                cambio = False

                                for i in range(len(list_weapons)-1-pasada):
                                    speed_arma_inicial = dict_weapons[list_weapons[i]]["speed"]
                                    speed_arma_siguiente = dict_weapons[list_weapons[i + 1]]["speed"]
                                    if speed_arma_inicial > speed_arma_siguiente:
                                        cambio = True
                                        aux = list_weapons[i]
                                        list_weapons[i] = list_weapons[i+1]
                                        list_weapons[i+1]= aux

                                if not cambio:
                                    break

                            for id in list_weapons:
                                arma = ""

                                if dict_weapons[id]["two_hand"]:
                                    arma = "True"
                                else:
                                    arma = "False"
                                datos_speed_arma =  datos_speed_arma + "{:>3}{:>15}{:>15}{:>10}{:>15}\n".format(id, dict_weapons[id]["name"],
                                                                                                                        dict_weapons[id]["strength"],
                                                                                                                        dict_weapons[id]["speed"],
                                                                                                                        arma)

                            print(datos_speed_arma)
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