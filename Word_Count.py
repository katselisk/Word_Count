from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import docx

L1 =""
L2 =""
Fn =""

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Καταμέτρηση Λέξεων")
        self.minsize(540, 80)

        
        

        
        self.button = ttk.Button( text="Open A File", command=self.fileDialog).grid(column=0, row=10)
        
        
        self.var=IntVar()
        Checkbutton(self, text="Να αφαιρεθούν λέξεις μικρότερες απο 3 γράμματα", variable=self.var).grid(column=5, row=5, sticky=W)
        


        self.button2 = ttk.Button( text="Save File", command=self.filesave).grid(column=0, row=15)
        

   

    def fileDialog(self):
        
        global L1
        global L2
        self.tem = {""}



        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetype=(("Word files", "*.docx"), ("all files", "*.*")))
        self.label = ttk.Label( text="")
        self.label.grid(column=5, row=10)
        self.label2 = ttk.Label( text="")
        self.label2.grid(column=5, row=15)


        
        doc = docx.Document(self.filename)
        global Fn
        Fn = self.filename
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        
        kimeno = ('\n'.join(fullText))
        kimeno = kimeno.strip('\n')
        kimeno=kimeno.replace('.', ' ')
        kimeno=kimeno.replace('\\', ' ')
        kimeno=kimeno.replace('@', ' ')
        kimeno=kimeno.replace('www', ' ')
        kimeno=kimeno.replace('http', ' ')
        kimeno=kimeno.replace(',', ' ')
        kimeno=kimeno.replace('.', ' ')
        kimeno=kimeno.replace('ή', ' ')
        kimeno= kimeno.lower()
        
        lexis = list(kimeno.split(" "))
        
        pattern = '[0-9]'
        lexis = [re.sub(pattern, '', i) for i in lexis]

        listC = ["-",'//','.','(',')','_','«',':',',',]
        for c in listC :
            lexis = [ele.replace(c, '') for ele in lexis] 
             

        if self.var.get() == 1 :
            v=3
           
        else:
            v=0
            

        
        for lexi in lexis:
            if len(lexi) > v:
                self.tem.add(lexi)
            else:
                continue
        
        L1 = f'Το σύνολο των λέξεων στο αρχείο είναι {len(lexis)} λέξεις' 
        L2 = f'Βγάζοντας τις διπλές και λέξεις μικρότερες απο 3 γράμματα έχουμε {(len(self.tem)-1)} λέξεις'
        
        self.label.configure(text=L1)
        self.label2.configure(text=L2 )

        
        
    
    def filesave(self):
            
        self.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Save to txt",defaultextension=".txt" , encoding='utf-8' )
        file1 = open(self.filename ,"w")
        file1.writelines(f'Από το αρχείο {Fn}. ')
        file1.writelines(f'{L1}.\n{L2}\n')
        file1.writelines('\n')
        file1.writelines("οι λέξεις που μετρήθηκαν ειναι : ")
        file1.writelines("\n")
        for x in self.tem:
            file1.writelines(x+", ")
        
        file1.close() 
        print (f'το αρχείο αποθηκεύτηκε στο : {self.filename}')
    

root = Root()
root.mainloop()




