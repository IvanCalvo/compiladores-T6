from midiutil import MIDIFile

def note_to_midi(note):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_name = note[:-1]
    octave = int(note[-1])
    midi_value = (octave + 1) * 12 + notes.index(note_name)
    return midi_value

class Gerador:
    def __init__(self):
        self.nome = ''
        self.riffs = {}
        self.ultimo = 'DURACAO'
        self.time = 0
        self.track    = 0
        self.channel  = 0
        self.tempo    = 60   # In BPM
        self.volume   = 120  # 0-127, as per the MIDI standard
        self.program = 3
        self.MyMIDI = MIDIFile(1) 
        self.MyMIDI.addProgramChange(self.track, self.channel, self.time, self.program)
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)
        
    def addRiff(self,riff):
        if riff not in self.riffs:
            self.riffs[riff] = {'nota':[],'duracao':[]}
        else:
            print('RIFF JA EXISTENTE')
    def addNota(self,riff,nota):
        if self.ultimo == 'DURACAO':

            if riff in self.riffs:
                self.riffs[riff]['nota'].append(nota)
                self.ultimo = 'NOTA'
            else:
                print('RIFF NÃO ENCONTRADO')
        else:
            return 'ERRO! REPETICAO DE NOTA!'
    def addDuracao(self,riff,duracao):
        if self.ultimo == 'NOTA':
            if riff in self.riffs:
                self.riffs[riff]['duracao'].append(duracao)
                self.ultimo = 'DURACAO'
            else:
                print(f"{riff} RIFF NÃO ENCONTRADO")
        else: 
            return 'ERRO! REPETIÇÃO DE DURAÇÃO!'

    def Debug(self):
        print(self.riffs)
        
    def Tocar(self,riff):
        
        for i in range(len(self.riffs[riff]['nota'])):
            if(self.riffs[riff]['nota'][i]) == '-':
                self.time += (self.riffs[riff]['duracao'][i]) * 0.1
            else:
                self.MyMIDI.addNote(self.track, self.channel, note_to_midi(self.riffs[riff]['nota'][i]), self.time, self.riffs[riff]['duracao'][i], self.volume)
                self.time+= (self.riffs[riff]['duracao'][i]) * 0.1
    def Gerar(self):
        with open(f"{self.nome}.mid", "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

g1 = Gerador()