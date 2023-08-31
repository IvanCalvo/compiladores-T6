from midiutil import MIDIFile

# Função que irá converter uma nota para o seu respectivo valor MIDI
def note_to_midi(note):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_name = note[:-1]
    octave = int(note[-1])
    midi_value = (octave + 1) * 12 + notes.index(note_name)
    return midi_value

class Gerador:
    def __init__(self):
        self.nome = '' #nome da musica
        self.riffs = {} #dicionáiro que irá guardar as notas dos riffs e as suas respectivas durações
        self.time = 0 #Inicia o tempo 0
        self.track    = 0 #Inicia na track 0 (só terá uma track)
        self.channel  = 0 #Inicia no channel 0 (Só terá um channel)
        self.tempo    = 60   # Batidas por minuto
        self.volume   = 120  # Volume da música
        self.program = 3 #Instrumento
        self.MyMIDI = MIDIFile(1) #Criando o objeto MIDIFile
        self.MyMIDI.addProgramChange(self.track, self.channel, self.time, self.program) #Muda o instrumento
        self.MyMIDI.addTempo(self.track, self.time, self.tempo) #Define o tempo
        
    #Cria um riff no dicionário dos riffs
    def addRiff(self,riff):
        if riff not in self.riffs:
            self.riffs[riff] = {'nota':[],'duracao':[]}
        else:
            print('RIFF JA EXISTENTE')

    #Adiciona uma nota atrelado a um riff
    def addNota(self,riff,nota):

        if riff in self.riffs:
            self.riffs[riff]['nota'].append(nota)
            self.ultimo = 'NOTA'
        else:
            print('RIFF NÃO ENCONTRADO')
      
    #Adiciona uma duração atrelado a um riff 
    def addDuracao(self,riff,duracao):
        if riff in self.riffs:
            self.riffs[riff]['duracao'].append(duracao)
            self.ultimo = 'DURACAO'
        else:
            print(f"{riff} RIFF NÃO ENCONTRADO")
   

    #Função para printar o riff
    def Debug(self):
        print(self.riffs)
        
    #Função que irá adicionar as notas e as suas respectivas durações ao objeto MyMIDI, ele será usado posteriormente para poder gerar a música
    def Tocar(self,riff):
        
        for i in range(len(self.riffs[riff]['nota'])):
            if(self.riffs[riff]['nota'][i]) == '-':
                self.time += (self.riffs[riff]['duracao'][i]) * 0.1
            else:
                self.MyMIDI.addNote(self.track, self.channel, note_to_midi(self.riffs[riff]['nota'][i]), self.time, self.riffs[riff]['duracao'][i], self.volume)
                self.time+= (self.riffs[riff]['duracao'][i]) * 0.1 #A duração será feita em milissegundos

    #Gera a música e salva em um arquivo .mid
    def Gerar(self):
        with open(f"{self.nome}.mid", "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

g1 = Gerador()