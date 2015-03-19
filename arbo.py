import os.path 
import hashlib

class Arbo:

    def md5_for_file(name, block_size=2**20):
        with open(name, 'rb') as f:
            md5 = hashlib.md5()
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
            return (name, md5.hexdigest())

    def get(path = "."):
        
        exclude = ['.storeit']

        fichier=[]  
        for root, dirs, files in os.walk(path):  
            for i in files:  
                if filter(lambda name: not i.endwith(name), exclude):
                    fichier.append(os.path.join(root, i))

        return list(map(Arbo.md5_for_file, fichier))
