#         0     1    2    3     4    5    6     7    8     9    10    11
tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
for tone in tones:
    print(tone, end=' ')
print('\n')

tones.extend(tones)
initial_tone = input('Molimo unesite pocetni ton akorda: ')
initial_tone_index = tones.index(initial_tone.upper())

print('Durski akord') # C dur
print(f'{tones[initial_tone_index]} {tones[initial_tone_index + 4]} {tones[initial_tone_index + 7]}')

print('Molski akord') # c mol
print(f'{tones[initial_tone_index]} {tones[initial_tone_index + 3]} {tones[initial_tone_index + 7]}')
