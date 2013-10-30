#!/usr/bin/python
class Bird:
    song = "Squaawk!"
    def sing(self):
        print self.song

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members+=1
        #self.members+=1

bird = Bird()
bird.sing()
m1=MemberCounter()
m1.init()
print m1.members
m2=MemberCounter()
m2.init()
#print MemberCounter.members
print m2.members
print m1.members


