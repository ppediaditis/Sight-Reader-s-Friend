import random

pitches = ["a","b","c","d","e","f","g"]

class Note:
	def __init__(self, pitch, duration, pause):
		slurred = False
		tied = False
		self.pitch = pitch
		self.duration = duration
		self.pause = pause

class Bar:
	def __init__(self, count, divisor):
		self.Notes = []
		self.count = count
		self.divisor = devisor
	
	def __init__(self):
		self.Notes = []
		self.count = 4
		self.divisor = 4
	
	def Space(self):
		#print "\nNEW SPACE"
		if len(self.Notes) == 0 :
			#print "No Notes" + str(self.count/self.divisor)
			return self.count/self.divisor
		if len(self.Notes) == 1 : 
			val = (self.count/self.divisor)-(1.0/(self.Notes[0].duration))
			#print "One note: " + str(val)
			return val
		reduced = reduce(Aggregate, map(lambda n: (1.0/n.duration), self.Notes))
		#print "REDUCED" + str(reduced)
		#print  "Final space:" +str((self.count / self.divisor) - reduced)
		return (self.count / self.divisor) - reduced

	def AddNote(self, note):
		#print "SPACE " + str(self.Space())
		#print "NEEDED " + str(1.0/(note.duration))
		if self.Space() < (1.0/(note.duration)):
			note.duration = abs(int(1.0/self.Space()))
			#print "ADJUSTING"
		self.Notes.append(note)

def Aggregate(n1, n2):
	#print str(n1) + " -- " + str(n2)
	return  n1 + n2


class Sequence:
	def __init__(self):
		self.bars = []
		self.bars.append(Bar())

	def ComposeNote(self):
		#print "Checking bar " + str(self.bars[-1].Space())
		if (self.bars[-1].Space() == 0):
			self.bars.append(Bar())
			#print "Added bar"
		duration = 2**random.randint(1,3)
		while((1.0)/duration > self.bars[-1].Space()) :
			#print "DURATION" + str(duration)
			duration = 2**random.randint(1,3)
		newNote = Note(random.randint(0,6),duration,False if random.randint(0,10) < 7 else True)
		self.bars[-1].AddNote(newNote)
		#print "Added Note" + str(newNote.duration)

class LilyPrinter:
	def Print(self,sequence):
		notes = ""
		for bar in sequence.bars:
			for note in bar.Notes:
				notes += ("r" if note.pause else pitches[note.pitch] ) + str(note.duration) + " " 

		return r"\score {\relative d' {"+notes+"}\n\midi { }\n \layout{} }"


seq = Sequence()

for i in range(0,100):
	seq.ComposeNote()

print LilyPrinter().Print(seq)
