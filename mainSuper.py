import hashlib,json
from datetime import datetime

class Block():
    def __init__(self,tstamp,voterInfo,previoushash=''):
        self.nonce = 0
        self.tstamp = tstamp
        self.voterInfo = voterInfo
        self.previoushash = previoushash
        self.hash = self.calcHash()
    
    def __str__(self):
        string =" Chain Nounce : " + str(self.nonce)+"\n"
        string += "voterInfo: " +str(self.voterInfo)+"\n"
        string += "Old hash: " +str(self.previoushash)+"\n"
        string += "New hash :" + str(self.hash)+"\n"

        return string 
    
    
    def calcHash(self):
        block_string = json.dumps({"Chain Nonce":self.nonce,"VotinggTimestamp":str(self.tstamp),"voterInfo":self.voterInfo,"previoushash":self.previoushash},sort_keys=True).encode()
        return hashlib.sha512(block_string).hexdigest()
        #sha512 used to make Voter blocks encrypted and Secure than 128
        #OLD AND newer hash will generate 512 encry keys 
    def mineBlock(self,difficulty):
        while(self.hash[:difficulty] != str('').zfill(difficulty)):
            self.nonce += 1
            self.hash = self.calcHash()
        

    
        

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(),]
        self.difficulty = 3

    def generateGenesisBlock(self):
        return Block(0,'01/01/2020','First Block')

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self,newBlock):
        newBlock.previoushash = self.getLastBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1,len(self.chain)):
            prevb = self.chain[i-1]
            currb = self.chain[i]
            if(currb.hash != currb.calcHash()):
                print("Invalid Block")
                return False
            if(currb.previoushash != prevb.hash):
                print("Invalid Chain")
                return False
        return True
            

bchain = BlockChain()
i=1
while i!="quit":

    age = int(input("Enter Your age: "))
    if age >= 18:
        print("You Can Vote You are Elegible to Vote ")
    else:
        print("Sorry You are Below 18 System Abort !")
        exit(1)
    
    name = str(input("Enter voter name: "))
    
       
    vote = int(input("Press the no. to vote:\n1 - BJP (Narendra Modi)\n2 - INC (Rahul Gandhi)\n3 - AAP (Arvind Kejriwal)\n4 - BSP\n5 - ShivSena\n6 - NOTA\n"))
    if vote == 1:
        elected = "BJP (Narendra Modi)"
    elif vote ==2 :
        elected = "Congress (Rahul Gandhi)"
    elif vote == 3:
        elected = "AAP (Arvind Kejriwal)"
    elif vote == 4:
        elected = "BSP (Mayawati)"
    elif vote == 5:
        elected = "ShivSena (Aditya Thackrey)"
    else:
        elected = "NOTA"
        print("No Part Selected Pls Select Party in next Stream")
        exit(1)
    patInfo = "Name: "+name +"\nAge: "+str(age)+"\nElected Party: "+elected
    bchain.addBlock(Block(datetime.now(),patInfo))
    i = input("type quit to End Voting and view Total E-Voting Details \n type cont to Continue Adding Voters :")


for b in bchain.chain:
    print(b)
