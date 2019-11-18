#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import subprocess


def main():
    with open('/home/igor/latexpruebas/query.tsv') as members:
        # la ventaja de DictReader es que crea diccionarios tomando
        # como key el nombre de la columna sin necesidad de decirle nada...
        lector = csv.DictReader(members, delimiter='\t')
        for l in lector:
            ordenreligiosa = l['order'].split("Q")
            relorders.add('Q' + ordenreligiosa[1])
            lugarnacimiento = l['lugarnacimiento'].split("Q")
            places.add('Q' + lugarnacimiento[1])


def extraercoords():
    coordenadas = subprocess.run(["wd", "coord", places.pop()], stdout=subprocess.PIPE)
    coords = coordenadas.stdout.decode("utf-8").split()
    return coords


# estos son sets que no permiten duplicados
relorders = set()
places = set()


if __name__ == "__main__":
    main()
    extraercoords()
