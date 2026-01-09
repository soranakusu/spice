
template = """
* source *
VDD vdd 0 1

* input
VA a 0 dc {A}
VB b 0 dc {B}
VC c 0 dc {C}
VD d 0 dc {D}


* MOSFET model
.model PMOS PMOS (LEVEL = 1 VTO = -0.5 KP = 50u)
.model NMOS NMOS (LEVEL = 1 VTO = 0.5 KP = 100u)

* A NAND B
Mpa m_mid a vdd vdd PMOS
Mpb m_mid b vdd vdd PMOS

Mna YB a n_mid 0 NMOS
Mnb n_mid b 0 0 NMOS

* C NAND D
Mpc YB c m_mid vdd PMOS
Mpd YB d vdd m_mid PMOS

Mnc YB c n_mid 0 NMOS
Mnd n_mid d 0 0 NMOS

.control

op
print v(YB)

.endc

.end
"""

for A in range (2):
    for B in range (2):
        for C in range (2):
            for D in range (2):
                textA = template.replace('{A}', str(A))
                textB = textA.replace('{B}', str(B))
                textC = textB.replace('{C}', str(C))
                textD = textC.replace('{D}', str(D))
                print(A, B, C, D)
                print("-------------------")
                print(textD)
                print("-------------------")
                
                filename = "case" + str(A) + str(B) + str(C) + str(D) + ".cir"

                out = open(filename, "w")
                out.write(textD)
                out.close()

                


