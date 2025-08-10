import commands
import gemini
import voice_io as v

while True:
    
    v.inp()

    if v.a == "open spotify":
        commands.spotify()
        v.out("opening spotify")
    elif v.a == "open chrome":
        commands.chrome()
        v.out("opening chromme")
    elif v.a == "open youtube":
        commands.youtube()
        v.out("oprning youtube")
    elif v.a == "open telegram":
        commands.telegram()
        ("opening telegram")
    elif v.a == "open reddit":
        commands.reddit()
        v.out("opening reddit")
    elif v.a == "open audio relay":
        commands.audiorelay()
        v.out("opening audio relay")
    elif v.a == "take screenshot":
        commands.ss()
        v.out("screenshot takken")
    else:
        ans = gemini.ask_gemini(v.a)
        print(ans)
        v.out(ans)


