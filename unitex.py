#       RIGHI Racim
#       BOURENANE Rania
#       L3 ACAD A
import os 
#os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin Delaf.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courier new\" -s 12")