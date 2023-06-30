"""
Objekti- student- kreirati klasu student te atribute objekta ime u
__init__. Nadodati property groupMember= None (ne unosi se u
konstruktoru ali je definiran u init metodi)

2.1 Kreirati repr gdje se ispisuje samo ime

2.2 Kreirati metodu setGroupMember koja postavlja kolegu našem objektu

2.3 postavljamo uvjet u metdu setGroupMember slučaju da je groupMember već
postavljen da se ispisuje poruka, imamo partnera
"""

class Student:
    def  __init__(self, ime):
        self.ime = ime
        self.groupMember = None

    def __repr__(self):
        self.f'{self.ime} je naziv ovog objekta'

    def set_Group_Member(self, other):
        self.groupMember = other
        other.groupMember = self
