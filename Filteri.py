import numpy as np  #koristimo je zbog lakse manipulacije nizovima
from scipy.signal import butter, lfilter # biblioteke namenjene za obradu signala
import matplotlib.pyplot as plt  #koristi se za pravljenje bilo kakvih grafika na ekranu
from math import pi  #broj 3.14

Fs = 200   #frekvencija citanja vrednosti, na svakih 1/Fs sekundi uzimamo vrednost signala i pakujemo u niz x-ose
vreme = 4  #vreme trajanja signala
frekvencija = 10 #frekvencija sinusoide
x_osa = np.arange(0, vreme, 1/Fs)  #funkcija sama pravi niz od 0 do 4 sa Fs*t clanova niza (svaki clan na razmaku 1/Fs)
sinusoida = np.sin(2*pi*frekvencija*x_osa)  #pravljenje sinusoide
shum = np.random.normal(0, 0.8, np.size(sinusoida))  #pravi se sum da bi se zakomplikovale stvari
y_osa = sinusoida + shum #ovime smo napravili neki suntavi signal koji podseca na sinusoidu

plt.figure()
plt.plot(x_osa, y_osa) #da vidimo kako izgleda

#pravimo filter

def bandpass_filter(data, Fth_L, Fth_H, Fs, order): #data je y osa koja treba da se izfiltrira (ostatak objasnjen dole)
    f_max = 0.5 * Fs
    low_cutoff = Fth_L/f_max
    high_cutoff = Fth_H/f_max
    b, a = butter(order, np.array([low_cutoff, high_cutoff]), btype='bandpass')
    y = lfilter(b, a, data)
                            #butter vraca dva parametra uz pomoc kojih lfilter razume sta treba da radi nad signalom
    return y

Fth_L1 = 8 #donja granica opsecanja
Fth_H1 = 12 #gornja granica opsecanja
order = 5 #brzina izvrsavanja filtera
y_osa_filtrirana = bandpass_filter(y_osa, Fth_L1, Fth_H1, Fs, order) #primenimo filter na y osu

plt.figure()
plt.plot(x_osa, y_osa_filtrirana) #da vidimo kako to izgleda
plt.show()


