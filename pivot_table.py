# importamos librerias
import pandas as pd
import numpy as np

empleados = {"Author": ["joseluna", "sixt93", "alberto", "carlosz", "jgbesq",
                              "nuri90", "santiago8", "joseluna", "alberto", "jgbesq",
                              "sixt93", "santiago8", "santiago8", "nico23", "alberto"],
                   "Sentiment": ["positive", "negative", "positive", "negative", "negative",
                                 "neutral", "neutral", "positive", "positive", "negative", "negative",
                                 "neutral", "neutral", "neutral", "positive"],
                   "country": ["Ecuador", "Colombia", "Francia", "USA", "UK", "Spain", "Chile",
                               "Peru", "Francia", "Panama", "Portugal", "Chile", "Bolivia", "USA", "USA"],
                   "Theme": ["PA", "CA", "OT", "OT", "PA", "EV", "KS", "KS", "OT", "KS", "OT", "KS", "PA", "PA", "KS"]}

df = pd.DataFrame(empleados, columns=['Author', 'Sentiment', 'country', 'Theme'])

pivot = df.pivot_table(index=['Author', 'Sentiment'], values=['country', 'Theme'], aggfunc='sum')

print(pivot)



