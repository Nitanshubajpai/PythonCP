#install pygame module first

from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import pygame

playlist = []

class Application(Frame):
    
    def __init__(self,master):
        super(Application, self).__init__(master)
        
       
        self.playlistbox = Listbox(self, width = 40, height = 10, selectmode = SINGLE) #TODO: ---> BROWSE, MULTIPLE, EXTENDED (p.379)
        for song in playlist:
            self.playlistbox.insert(END, song)
            
        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row = 1)
        self.playButton = Button(self, text = 'Play', command = self.play)
        self.loopButton = Button(self, text = 'Loop', command = self.loop)
        self.addButton = Button(self, text = 'Add', command = self.add)
        self.playButton.grid(row=4, column = 0)
        self.loopButton.grid(row=4, column = 1)
        self.addButton.grid(row=4, column = 2)
        self.pack()
        
        
        pygame.init()

    def play(self):
        if(len(playlist) == 0):
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:    
            pygame.mixer.music.stop()
            selectedSongs = self.playlistbox.curselection()
            global playlistbox
            playIt = playlist[int(selectedSongs[0])]
            pygame.mixer.music.load(playIt)
            pygame.mixer.music.play(0, 0.0)
            

    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,0.0)

    def add(self):
        file = tk.askopenfilenames(initialdir='C:/Users/Nitanshubajpai/music')  
        songsTuple = root.splitlist(file)   
        songsList = list(songsTuple)        
        
        for song in songsList:              
            playlist.append(song);          
            tempArray = song.split('/')     
            songShort = tempArray[len(tempArray)-1]
            self.playlistbox.insert(END, songShort)
        
root = Tk()
root.title('Music Player')
root.geometry('500x200')
app = Application(root)
app.mainloop()
