
print("THE MYSTERY OF BLACKWOOD ISLAND")


name = input("Enter Your Name- ").upper()
print("\nWELCOME", name , "THE MYSTERY OF BLACKWOOD ISLAND")
print("\nYou wake up on a beach after a terrible shipwreck.")
print("You don't remember how you got here.")
print("You remember only one thing...")
print('"Find the lighthouse before sunset."')

print("\nYou check your pockets.")
print("You have:")
print("- A pocket knife")
print("- A lighter")
print("- A rope")
print("- One bottle of water")

print("\nYou notice a strange symbol carved into a piece of wood:")
print("▲ - 17 - ●")

print("\nThere are three possible routes.")
print("1. Jungle")
print("2. River")
print("3. Bridge")

choice = input("\nWhich route do you choose? ").lower()


# =========================================================
# JUNGLE
# =========================================================

if choice == "1" or choice == "jungle".lower():

    print("\nYou enter the jungle.")
    print("After walking for a while, you discover an abandoned campsite.")

    print("\nYou find:")
    print("- An empty backpack")
    print("- A compass")
    print("- A notebook")
    print("- A locked metal box")

    print("\nYou open the notebook.")

    print('"The lighthouse keeper is not who he claims to be."')
    print('"The bridge is safe, but the river is not."')
    print('"17 - ▲ - ●"')

    choice = input(
        "\nWhat do you do?\n"
        "1. Search the campsite\n"
        "2. Leave the campsite\n"
        "3. Try to break the box\n"
        "Choose: "
    ).lower()

    # SEARCH CAMPSITE

    if choice == "1" or choice == "search".lower():

        print("\nYou search the campsite carefully.")

        print("You find a small key underneath the backpack.")

        print("You use the key to open the metal box.")

        print("\nInside you find:")
        print("- A flashlight")
        print("- A radio")
        print("- A photograph")

        print("\nThe photograph shows the lighthouse.")

        print('On the back it says:')
        print('"If the lighthouse light is RED, do not enter."')

        print("\nYou remember the warning.")

        print("You continue toward the lighthouse.")

        print("\nAfter walking for an hour, you reach the lighthouse.")

        print("The lighthouse light is RED.")

        choice = input(
            "\nWhat do you do?\n"
            "1. Enter the lighthouse\n"
            "2. Wait outside\n"
            "3. Use the radio\n"
            "Choose: "
        ).lower()

        # ENTER LIGHTHOUSE

        if choice == "1" or choice == "enter".lower():

            print("\nYou enter the lighthouse.")

            print("The door suddenly locks behind you.")

            print("You hear footsteps coming down the stairs.")

            print("A man appears.")

            print('"You should not have come here."')

            print("\nGAME OVER!")
            print("THE LIGHTHOUSE KEEPER FOUND YOU.")

        # WAIT

        elif choice == "2" or choice == "wait".lower():

            print("\nYou hide behind some rocks.")

            print("After several minutes, a man leaves the lighthouse.")

            print("He is carrying a radio.")

            print("You wait until he disappears.")

            print("You enter the lighthouse.")

            print("\nInside you find a control room.")

            print("There are three switches.")

            print("RED")
            print("BLUE")
            print("GREEN")

            print("\nA message is written on the wall:")
            print('"Only one color tells the truth."')

            choice = input(
                "\nWhich color do you choose? "
            ).lower()

            if choice == "blue".lower():

                print("\nYou press the BLUE switch.")

                print("Nothing happens.")

                print("Then you hear a CLICK.")

                print("A secret door opens.")

                print("\nBehind the door is a tunnel.")

                print("You walk through the tunnel.")

                print("At the end you discover a small boat.")

                print("You remember everything you learned.")

                print("The island was testing you.")

                print("\nYou start the boat.")

                print("You sail away from Blackwood Island.")

                print("\n================================")
                print("        GOOD ENDING!")
                print("     YOU ESCAPED THE ISLAND")
                print("================================")

            elif choice == "red".lower():

                print("\nYou press the RED switch.")

                print("An alarm suddenly starts.")

                print("The lighthouse doors lock.")

                print("\nGAME OVER!")

            elif choice == "green".lower():

                print("\nYou press the GREEN switch.")

                print("The room becomes completely dark.")

                print("You hear footsteps behind you.")

                print("\nGAME OVER!")

            else:

                print("\nInvalid choice.")
                print("GAME OVER.")

        # RADIO

        elif choice == "3" or choice == "radio".lower():

            print("\nYou turn on the radio.")

            print("Static fills the room.")

            print("Then you hear a voice.")

            print('"The lighthouse is not the exit."')

            print('"Look beneath the island."')

            print("\nYou look around the lighthouse.")

            print("You discover a hidden trapdoor.")

            print("You open it.")

            print("There is a tunnel underneath the lighthouse.")

            print("\nYou enter the tunnel.")

            print("At the end you find an old boat.")

            print("\nYou escape the island!")

            print("\nGOOD ENDING!")

        else:

            print("\nInvalid choice.")
            print("GAME OVER.")

    # LEAVE CAMPSITE

    elif choice == "2" or choice == "leave".lower():

        print("\nYou decide to leave the campsite.")

        print("You continue walking through the jungle.")

        print("After an hour you become completely lost.")

        print("The sun begins to set.")

        print("You hear something moving behind you.")

        print("You turn around.")

        print("You see nothing.")

        print("\nGAME OVER!")
        print("YOU GOT LOST IN THE JUNGLE.")

    # BREAK BOX

    elif choice == "3" or choice == "break".lower():

        print("\nYou try to break the metal box.")

        print("You hit it with a rock.")

        print("CRACK!")

        print("The box breaks.")

        print("Unfortunately, you damaged everything inside.")

        print("The map is destroyed.")

        print("You have no idea where the lighthouse is.")

        print("\nGAME OVER!")

    else:

        print("\nInvalid choice.")
        print("GAME OVER.")


# =========================================================
# RIVER
# =========================================================

elif choice == "2" or choice == "river".lower():

    print("\nYou follow the river.")

    print("The water looks clean.")

    print("You are extremely thirsty.")

    print("You kneel down to drink.")

    print("Suddenly...")

    print("You see two eyes underneath the water.")

    print("A HUGE CROCODILE!")

    choice = input(
        "\nWhat do you do?\n"
        "1. Swim across\n"
        "2. Use the boat\n"
        "3. Follow the river\n"
        "Choose: "
    ).lower()

    # SWIM

    if choice == "1" or choice == "swim".lower():

        print("\nYou jump into the river.")

        print("You swim as fast as you can.")

        print("Suddenly something grabs your leg.")

        print("The crocodile!")

        print("\nGAME OVER!")

    # BOAT

    elif choice == "2" or choice == "boat".lower():

        print("\nYou discover an old wooden boat.")

        print("You inspect it.")

        print("There is a large hole in the bottom.")

        print("You remember that you have a rope.")

        choice = input(
            "\nDo you repair the boat using the rope? (yes/no): "
        ).lower()

        if choice == "yes".lower():

            print("\nYou use your rope to repair the boat.")

            print("The boat is strong enough to cross.")

            print("You safely cross the river.")

            print("\nYou discover an old village.")

            print("There is a small house nearby.")

            print("Smoke is coming from the chimney.")

            choice = input(
                "\nDo you knock on the door? (yes/no): "
            ).lower()

            if choice == "yes".lower():

                print("\nAn old man opens the door.")

                print("You're the first person I've seen in years.")

                print("You notice a lighthouse photograph on his wall.")

                choice = input(
                    "\nDo you ask him about the lighthouse? (yes/no): "
                ).lower()

                if choice == "yes".lower():

                    print("\nThe man's face suddenly changes.")

                    print('"You should not go there."')

                    print("You realize he is hiding something.")

                    print("\nYou leave the house.")

                    print("You continue toward the lighthouse.")

                    print("\nYou find the lighthouse.")

                    print("The light is RED.")

                    print("You remember the warning.")

                    print("\nYou decide not to enter.")

                    print("You search around the lighthouse.")

                    print("You find a hidden tunnel.")

                    print("The tunnel leads to a boat.")

                    print("\nYou escape the island!")

                    print("\nGOOD ENDING!")

                else:

                    print("\nYou trust the old man.")

                    print("He gives you food and water.")

                    print("You stay at his house.")

                    print("You never discover the secret.")

                    print("\nMYSTERY ENDING.")

            else:

                print("\nYou decide not to knock.")

                print("You continue walking.")

                print("Eventually you reach the lighthouse.")

                print("\nYou escape through a hidden tunnel.")

                print("\nGOOD ENDING!")

        else:

            print("\nYou enter the boat without repairing it.")

            print("The boat begins filling with water.")

            print("You fall into the river.")

            print("\nGAME OVER!")

    # FOLLOW RIVER

    elif choice == "3" or choice == "follow".lower():

        print("\nYou decide to follow the river.")

        print("After walking for a long time, you discover an old bridge.")

        print("You remember the notebook:")

        print('"The bridge is safe, but the river is not."')

        print("\nYou cross the bridge safely.")

        print("On the other side you find a sign.")

        print("LIGHTHOUSE → 2 KM")

        print("\nYou follow the sign.")

        print("You reach the lighthouse.")

        print("The light is RED.")

        choice = input(
            "\nDo you enter the lighthouse or wait outside(enter/wait)? "
        ).lower()

        if choice == "enter".lower():

            print("\nYou enter.")

            print("The door locks behind you.")

            print("GAME OVER!")

        elif choice == "wait".lower():

            print("\nYou wait outside.")

            print("A man leaves the lighthouse.")

            print("You wait until he disappears.")

            print("You enter.")

            print("You discover a secret tunnel.")

            print("The tunnel leads to a boat.")

            print("\nGOOD ENDING!")

        else:

            print("\nInvalid choice.")
            print("GAME OVER.")

    else:

        print("\nInvalid choice.")
        print("GAME OVER.")


# =========================================================
# BRIDGE
# =========================================================

elif choice == "3" or choice == "bridge".lower():

    print("\nYou decide to cross the old bridge.")

    print("The bridge looks extremely dangerous.")

    print("You remember something from the notebook:")

    print('"The bridge is safe, but the river is not."')

    print("\nYou carefully cross the bridge.")

    print("You reach the other side safely.")

    print("\nYou discover an abandoned village.")

    print("One house has smoke coming from the chimney.")

    choice = input(
        "\nDo you investigate the house? (yes/no): "
    ).lower()

    if choice == "yes".lower():

        print("\nYou knock on the door.")

        print("An old man opens it.")

        print("You're the first person I've seen in years.")

        print("You notice a photograph of the lighthouse.")

        choice = input(
            "\nDo you ask him about the lighthouse? (yes/no): "
        ).lower()

        if choice == "yes".lower():

            print("\nThe old man becomes nervous.")

            print('"The lighthouse keeper disappeared twenty years ago."')

            print("But something doesn't make sense.")

            print("You remember the notebook:")

            print('"The lighthouse keeper is not who he claims to be."')

            choice = input(
                "\nDo you search the house? (yes/no): "
            ).lower()

            if choice == "yes".lower():

                print("\nYou search the house.")

                print("You discover a hidden basement.")

                print("Inside are:")
                print("- Old radios")
                print("- Maps")
                print("- Photographs")

                print("\nEvery photograph shows the same lighthouse.")

                print("Every photograph has the symbol:")

                print("▲ - 17 - ●")

                print("\nYou finally understand.")

                print("The symbol is a code.")

                print("You find three objects:")

                print("A clock showing 17:00")
                print("A triangle-shaped key")
                print("A circular button")

                print("\nYou remember the order:")

                print("17 - ▲ - ●")

                choice = input(
                    "\nEnter the code in the correct order."
                    "\nType: 17 triangle circle\n"
                    "Your answer: "
                ).lower()

                if choice == "17 triangle circle".lower():

                    print("\nCLICK!")

                    print("A secret door opens.")

                    print("Inside you find a radio.")

                    print("The radio turns on.")

                    print("If you're hearing this, the lighthouse keeper has found you.")

                    print("\nYou escape through a hidden tunnel.")

                    print("The tunnel leads to a small boat.")

                    print("\nYou start the boat.")

                    print("You sail away from Blackwood Island.")

                    print("\n================================")
                    print("        PERFECT ENDING!")
                    print("     YOU SOLVED THE MYSTERY")
                    print("================================")

                else:

                    print("\nThe code is wrong.")

                    print("A loud alarm begins.")

                    print("The basement door locks.")

                    print("\nGAME OVER!")

            else:

                print("\nYou decide not to search the house.")

                print("You leave the village.")

                print("You never discover the secret.")

                print("\nMYSTERY ENDING.")

        else:

            print("\nYou decide not to ask questions.")

            print("The old man gives you some food.")

            print("You leave the village.")

            print("You never discover the secret.")

            print("\nMYSTERY ENDING.")

    else:

        print("\nYou decide to ignore the house.")

        print("You continue toward the lighthouse.")

        print("You eventually reach it.")

        print("The light is RED.")

        print("You remember the warning.")

        print("\nYou decide not to enter.")

        print("You wait until night.")

        print("A boat arrives near the island.")

        print("You signal the boat.")

        print("\nGOOD ENDING!")
        print("YOU WERE RESCUED.")


# =========================================================
# INVALID START
# =========================================================

else:

    print("\nYou stand on the beach.")

    print("You can't decide which path to take.")

    print("The sun begins to set.")

    print("\nGAME OVER!")
    
#                          ┌──────────────┐
#                          │    START     │
#                          │  BEACH       │
#                          └──────┬───────┘
#                                 │
#                  ┌──────────────┼──────────────┐
#                  │              │              │
#               LEFT            RIVER          BRIDGE
#                  │              │              │
#                  ▼              ▼              ▼
#           ┌────────────┐ ┌────────────┐ ┌────────────┐
#           │  JUNGLE    │ │   RIVER    │ │   BRIDGE   │
#           └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
#                 │              │              │
#           ┌─────┴─────┐   ┌────┼─────┐   ┌────┴─────┐
#           │           │   │    │     │   │          │
#        CABIN        CAVE SWIM FOLLOW CROSS       STATUE
#           │           │   │    │     │              │
#           │           │   │    │     │       ┌──────┼──────┐
#           │           │   │    │     │       │      │      │
#           │           │   │    │     │      FIRE   WATER   LEAF
#           │           │   │    │     │       │      │      │
#           ▼           ▼   ▼    ▼     ▼       ▼      ▼      ▼
#        CABIN       CAVE  DEAD RIVER  TREE   TUNNEL  WATER  OLD MAN
#           │           │       │     │        │      │      │
#       ┌───┼───┐       │       │     │        │      │   ┌──┴──┐
#       │   │   │       │       │     │        │      │   │     │
#     HIDE KEY WINDOW   │       │     │        │      │ TRUST RUN
#       │   │    │      │       │     │        │      │   │     │
#       ▼   │    ▼      ▼       │     ▼        ▼      ▼   ▼     ▼
#     DEAD  │   DEAD    DEAD   BOAT  LIGHT   TREASURE CONTINUE DEAD
#           │                   │      │       │          │
#           │                   │      │       │          │
#           ▼                   ▼      │       ├──DEAD    ▼
#       LIGHTHOUSE          REPAIR     │       │       ESCAPE
#           │                   │      │       │          │
#           ▼                   ▼      │       ▼          ▼
#       FINAL CHOICE         LIGHTHOUSE│    LAB       GOOD END
#           │                          │      │
#      ┌────┼────┐                     │      ▼
#      │    │    │                     │   GOOD END
#     SHIP STAY INVESTIGATE            │
#      │    │      │                   │
#      ▼    ▼      ▼                   │
#    GOOD MYSTERY SECRET               │
#    END   ENDING  ENDING              │
#                                      │
#                           ┌──────────┘
#                           │
#                     LIGHTHOUSE
#                           │
#                      RED LIGHT
#                           │
#                 ┌─────────┼─────────┐
#                 │         │         │
#               ENTER      WAIT      RADIO
#                 │         │         │
#                DEAD       │         │
#                           │         │
#                           ▼         ▼
#                      LIGHTHOUSE   "LIGHTHOUSE
#                        INSIDE     ISN'T EXIT"
#                           │
#                           ▼
#                      CONTROL ROOM
#                           │
#                     ┌─────┼─────┐
#                     │     │     │
#                    RED   BLUE  GREEN
#                     │     │     │
#                    TRAP  TRUTH  CLUE
#                     │     │     │
#                    DEAD   │     │
#                           └──┬──┘
#                              │
#                          FINAL CODE
#                              │
#                     17 → TRIANGLE → CIRCLE
#                              │
#                              ▼
#                        SECRET DOOR
#                              │
#                              ▼
#                        UNDERGROUND
#                           TUNNEL
#                              │
#                              ▼
#                            BOAT
#                              │
#                              ▼
#                         GOOD ENDING

