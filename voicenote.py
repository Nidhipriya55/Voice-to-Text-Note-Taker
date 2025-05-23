import tkinter as tk
from datetime import datetime
import speech_recognition as sr 

class VoiceNoteApp:
    def __init__(self, root):
       self.root = root 
       self.root.title("Voice note taker")

       self.root.geometry("600x800")
       self.root.config(bg="#4bca51")

       self.filename = self.get_filename()
       self.language = "en-US"

       self.language_lable = tk.Label(
           root,
           text = "Select language for notes",
           font=("Arial",12),
           bg="#f0f8ff"
       )
       self.language_lable.pack(pady=5)

       self.language_var = tk.StringVar(value="en-US")
       self.language_menu = tk.OptionMenu(
           root,
           self.language_var,
           "en-US","hi-IN","bn-BD"
       )
       
       self.language_menu.config(
           width=15,
           font=("Arial",12),
           relief="solid",
           bg="#e0f7fa"
       )
       self.language_menu.pack(pady=10)

       self.record_button = tk.Button(
           root,
           text="Start recording",
           command=self.take_voice_note,
           font=("Arial",14),
           relief="solid",
           bg = "#00796b",
           fg="white",
           width=20,
           height=2
       )

       self.record_button.pack(pady=10)

       self.view_button = tk.Button(
           root,
           text="View file",
           font=("Arial",14),
           relief="solid",
           bg = "#00796b",
           fg="white",
           width=20,
           height=2
       )

       self.view_button.pack(pady=10)


       self.delete_button = tk.Button(
           root,
           text="Delete file",
           font=("Arial",14),
           relief="solid",
           bg = "#00796b",
           fg="white",
           width=20,
           height=2
       )

       self.delete_button.pack(pady=10)

       self.exit_button = tk.Button(
           root,
           text="Exit",
           font=("Arial",14),
           relief="solid",
           bg = "#00796b",
           fg="white",
           width=20,
           height=2
       )

       self.exit_button.pack(pady=10)


       self.notes_display = tk.Text(
           root,
           width = 50,
           height = 10,
           font=("Arial",14),
           bg = "#f1f1f1",
           fg="#212121",
           bd = 2
       )

       self.notes_display.pack(pady=10)

    def get_filename(self):
        date = datetime.now().strftime("%y-%m-%d")
        return f"notes_{date}.txt"

    def take_voice_note(self):
        # initialize the recognizer
        recognizer =  sr.Recognizer() 
        # mic to take the input 
        mic = sr.Microphone()

        print("Hello Hello, You can talk: ")

        # its for exception handling 
        try: 
            with mic as source:
                # adjusting the ambience 
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.record(source, duration=5)
                print("Converting your audio to text...")
                note = recognizer.recognize_google(audio, language=self.language)

                timestamp = datetime.now().strftime("%y-%m-%d %H: %M: %S")
                print(note)

            # writting into a file 
            with open(self.filename,"a", encoding="utf-8") as file:
                file.write(timestamp + " " + note + "\n")

        except Exception as e:
            print("I am not able to procees the audio")


# calling function
if __name__ == "__main__":
    root = tk.Tk() # main window 
    app = VoiceNoteApp(root)
    root.mainloop()