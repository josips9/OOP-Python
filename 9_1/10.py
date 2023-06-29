"""
10 Kreirati klasu Student uz pomoć init metode. Unutar
konstruktora definirati: (fname,lname, reg).

10.1 Također definirati argument objekta (unos se ne zahtjeva ali se varijabla
nalazi u init metodi) self.izborni_studenta = ['Obavezan'] (sadrži odmah
obavezan predmet u polju). To znači da svaki student ima obavezan kolegij

10.2 Kreirati također dva argumenta klase smjer = "IT" te svi mogući kolegiji koje
jedan student može upisati
izborni_kolegiji = ['Algoritmi', 'Multimedija','Python', 'Machine Learning', 'Java', 'PHP', 'JavaScript'
,'Obavezan']

10.3 Kreirati metodu registracija_izbornog koja omogućuje studentu unos više
izbornih predmeta koji su ponuđeni unutar izborni_kolegiji
(*izborni_predmeti). Sve unesene izborne predmete unosimo u
self.izborni_studenta[]

10.4 Kreirati metodu klase neizabrani_kolegiji_studenata koja omogućuje ispis
svih kolegija koje niti jedan student nije upisao (kreirati argument klase
prazno polje naziva neizabrani_kolegiji gdje smještamo neizabrane izborne)

10.5 Kreirati metodu klase ispis_svih_studenata koja ispisuje imena i prezimena
svih upisanih studenata i broj izbornih (obavezni preskočiti) npr.
"""


class Student:
    smjer = "IT"
    izborni_kolegij = ['Algoritmi', 'Multimedija', 'Python',
                        'Machine Learning', 'Java', 'PHP', 'JavaScript', 'Obavezan']
    neizabrani_kolegiji = []
    izabrani_kolegiji = []
    popis_svih_studenata = {}

    def  __init__(self, fname, lname, reg):
        self.izborni_studenta = ['Obvezan']
        self.fname = fname
        self.lname = lname
        self.reg = reg
        self.ime_prezime = self.fname + " " + self.lname
        Student.popis_svih_studenata[self.ime_prezime] = 0

    def registracija_izbornog(self, *kwargs):
        for element in kwargs:
            self.izborni_studenta.append(element)
            Student.izabrani_kolegiji.append(element)
        Student.popis_svih_studenata[self.ime_prezime] += len(kwargs)

    @classmethod
    def neizabrani_kolegij_studenata(cls):
        skup_neizabranih = set(Student.izborni_kolegij) - \
            set(Student.izabrani_kolegiji)

        for element in skup_neizabranih:
            print(element)

    @classmethod
    def ispis_svih_studenata(cls):
        for k, v in Student.popis_svih_studenata.items():
            print(k, v)


student1 = Student('ivo', 'ivić', 2)
student2 = Student('pero', 'perić', 3)
student3 = Student('maja', 'majić', 4)

student1.registracija_izbornog("Multimedija", "Python")
student2.registracija_izbornog("Multimedija", "Python", "Machine Learning")
student3.registracija_izbornog("Algoritmi")

print(student1.izborni_studenta)
print("***********************\n")
print(student2.izborni_studenta)
print("***********************\n")
print(student3.izborni_studenta)
print("***********************\n")

print("Izabrani:")
print(Student.izabrani_kolegiji)
print("")

print("Izborni:")
print(Student.izborni_kolegij)
print("")

print("Neizabrani:")
Student.neizabrani_kolegij_studenata()
print("")

print("Svi studenti:")
Student.ispis_svih_studenata()


