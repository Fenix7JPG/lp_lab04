from polymorphic_fish import PezPayaso, Tiburon

def enElPacifico(pez):
    pez.nadar()


sammy = Tiburon()
casey = PezPayaso()

enElPacifico(sammy)
enElPacifico(casey)
