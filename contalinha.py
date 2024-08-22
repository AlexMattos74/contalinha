
import os

def QuantasLinhas(path):
    f = open("/home/contalinha/output/output.csv", "a")
    total = 0
    print("path","file_name", "linhas_totais", "linhas_codigo","linhas_comentario","linhas_branco","linhas_ponto_virgula",sep=";", file= f)
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files: 
            print(os.path.join(p,file))       
            arquivo = open(os.path.join(p, file ), "r" , encoding="latin-1")
            linhas_totais = 0
            linhas_branco = 0
            linhas_comentario = 0
            linhas_codigo = 0
            linhas_ponto_virgula = 0
            for linha in arquivo:
                linhas_totais = linhas_totais + 1
                linha_strip = linha[0:68]
                linha_strip = linha_strip.strip(" ")
                print(linha_strip)
                if (linha_strip == "" or linha_strip == "\n"):
                    linhas_branco = linhas_branco + 1
                if linha_strip[0:1] == "*":
                    if (linha_strip == "*\n" or linha_strip == "*"):
                        linhas_branco = linhas_branco + 1
                    else:
                        linhas_comentario = linhas_comentario + 1
                if linha_strip[0:2] == "/*":
                    linhas_comentario = linhas_comentario + 1
                if linha_strip[0:1] == ";" or linha_strip[0:3] == ";\n":
                    linhas_ponto_virgula = linhas_ponto_virgula + 1
            linhas_codigo = linhas_totais - (linhas_branco + linhas_comentario + linhas_ponto_virgula )  

            arquivo.close()             
            print(os.path.join(p,file),file, linhas_totais, linhas_codigo,linhas_comentario,linhas_branco,linhas_ponto_virgula,sep=";", file= f)
            total = total + linhas_totais
        print(total,)



QuantasLinhas('/home/contalinha/data')
