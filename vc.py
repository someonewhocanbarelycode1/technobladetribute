import random
import keyboard
import sys
while True:
    if keyboard.is_pressed('q'):
        sys.exit('bye')
    if keyboard.is_pressed('e'):   
        H = random.randint(1, 10)
        if H == 1:
            import cannibal
            cannibal.writeitloser()
        if H == 2:
            import slmccl
            slmccl.anotherwrite()
        if H == 3:
            import athiest
            athiest.kkg()
        if H == 4:
            import technosfinal
            technosfinal.finalvidtalk()
        if H == 5:
            import tyrant
            tyrant.call()
        if H == 6:
            import duel
            duel.ad()
        if H == 7:
            import orphans
            orphans.orphan()
        if H == 8:
            import skyblock
            skyblock.speech()
        if H == 9:
            import canceledorcancelled
            canceledorcancelled.twitter()
        if H == 10:
            import spanish
            spanish.yes()