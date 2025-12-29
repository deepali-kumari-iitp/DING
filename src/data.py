import os
<<<<<<< HEAD
 
=======

>>>>>>> 6b5a171 (Implemented the init function 🦆🦆)
Ding_dir = ".ding"

def init():
    cwd = os.getcwd()
    ding_path = os.path.join(cwd, Ding_dir)

    if os.path.exists(ding_path):
<<<<<<< HEAD
        print("It is already a ding repository")
        return

    os.mkdir(ding_path)
    print(f"Initialisied a ding repo in {ding_path}")
=======
        print("It is a ding repository")
        return

    os.mkdir(ding_path)
    print(f"Initialisied an ding repo in {ding_path}")
>>>>>>> 6b5a171 (Implemented the init function 🦆🦆)
