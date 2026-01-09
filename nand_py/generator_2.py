import os

outdir = './caseABCD'
input_file = r'./ABCD.cir'
file_name_template = 'case{}{}{}{}.cir'

with open(input_file, 'r', encoding='UTF-8') as file:
    template = file.read()

# os.mkdir(outdir)

for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                content = template.format(A, B, C, D)
                out_filename = file_name_template.format(A, B, C, D)
                output_path = outdir + '/' + out_filename

                with open(output_path, 'w', encoding='UTF-8') as outfile:
                    outfile.write(content)
