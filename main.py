import random
import keyboard
import sys
while True:
    if keyboard.is_pressed('q'):
        sys.exit('bye')
    if keyboard.is_pressed('e'):   
        H = random.randint(1, 10)
        if H == 1:
            import quotes
            quotes.writeitloser()
        if H == 2:
            import quotes
            quotes.anotherwrite()
        if H == 3:
            import quotes
            quotes.kkg()
        if H == 4:
            import quotes
            quotes.finalvidtalk()
        if H == 5:
            import quotes
            quotes.call()
        if H == 6:
            import quotes
            quotes.ad()
        if H == 7:
            import quotes
            quotes.orphan()
        if H == 8:
            import quotes
            quotes.speech()
        if H == 9:
            import quotes
            quotes.twitter()
        if H == 10:
            import quotes
            quotes.yes()