import numpy as np  #koristimo je zbog lakse manipulacije nizovima
from scipy.signal import butter, lfilter # biblioteke namenjene za obradu signala
import matplotlib.pyplot as plt  #koristi se za pravljenje bilo kakvih grafika na ekranu
from math import pi  #broj 3.14
from scipy import fftpack  #furijeova transformacija

frekvencija1 = 20 #frekvencija prve sinusoide
frekvencija2 = 30 #frekvencija druge sinusoide
vreme = 1 #vreme trajanja signala
Fs = 200 #frekvencija citanja vrednosti, na svakih 1/Fs sekundi uzimamo vrednost signala i pakujemo u niz x-ose
vremenski_razmak = 1/Fs #razmak na x osi (vremenskoj osi) izmedju svake vrednosti

x = np.arange(0, vreme, vremenski_razmak) #funkcija sama pravi niz od 0 do 4 sa clanom na svakih vremesnki_razmak sekundi

sinusoida1 = np.sin(2 * pi * frekvencija1 * x) #pravljenje prve sinusoide
sinusoida2 = np.sin(2 * pi * frekvencija2 * x) #pravljenje druge sinusoide

sinusoida_ukupno = sinusoida1 + sinusoida2 #zbir dve sinusoide

sinusoida_ukupno_fft = np.abs(fftpack.fft(sinusoida_ukupno)) #taj zbir u furijeovom domenu, kada se zumira na prva dva peaka,
                                                            #vidi se da se javljaju na 20 i 30 frekvencije

plt.figure() #pravi prozor gde se crta grafik
plt.plot(sinusoida_ukupno_fft) #crta nam grafik, x osa se podrazumevano uzima za frekvenciju


shum = np.random.normal(0, 0.8, np.size(sinusoida_ukupno)) #pravi se sum da bi se zakomplikovale stvari

sinusoida_suntava = sinusoida_ukupno + shum #ovime smo napravili neki suntavi signal koji podseca na sinusoidu

sinusoida_suntava_fft = np.abs(fftpack.fft(sinusoida_suntava)) #prebacili smo da vidimo sta se desava sa tim signalom u
                                                                #furijeovom domenu

def bandpass_filter(data, Fth_L, Fth_H, Fs, order): #data je y osa koja treba da se izfiltrira (ostatak objasnjen dole)
    f_max = 0.5 * Fs
    low_cutoff = Fth_L/f_max
    high_cutoff = Fth_H/f_max
    b, a = butter(order, np.array([low_cutoff, high_cutoff]), btype='bandpass')
    y = lfilter(b, a, data)
                            #butter vraca dva parametra uz pomoc kojih lfilter razume sta treba da radi nad signalom
    return y

order = 9 #koliko je uzak bandpass filter
Fth_H = 35 #frekvencija posle koje secemo
Fth_L = 15 #frekvencija pre koje secemo

sinusoida_filtrirana = bandpass_filter(sinusoida_suntava, Fth_L, Fth_H, Fs, order)
#filter se primenjuje na signal u normalnom domenu, ne furijeovom, iako signal radi na furijeovom domenu

#sinusoida_invertovana = fftpack.ifft(sinusoida_ukupno_fft)

plt.figure()
plt.plot(x, sinusoida_filtrirana)

plt.show() #prikazuje nam sve prozore na ekranu

