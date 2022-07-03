from settlers_of_valgard.settlement import Settlement


def work(settlement : Settlement):
    for settler in settlement.settlers:
        if settler.workplace is not None:
            pass