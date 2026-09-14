from datetime import datetime, timedelta


#remedios
futuro = 0


remedio = input("Insira o nome do Remédio: ")

horas_intervalo = int(input("De quantas em quantas horas é necessario tomar: "))

calculo_doses = int(input(" Quantas Doses deseja calcular ?                        "))

#apartir_dose = int(input("A partir de qual dose deseja visualizar"))

pular_dose = int(input("Qual dose voce deseja pular ?"))

horas_agora = datetime.now()

timedelta(hours=horas_intervalo)

print(f"Nome do remédio: {remedio}")

print(f"Horas Intervalo: {horas_intervalo} em {horas_intervalo} horas")

print(f"Horas agora: {horas_agora.hour} horas e {horas_agora.minute} Minutos ")
###O 02d significa:

print(f"{horas_agora.hour:02d}:{horas_agora.minute:02d}")



#futuro = horas_agora + timedelta(hours=horas_intervalo)

#segunda = horas_agora + timedelta(hours=horas_intervalo * 2 )

#terceira = horas_agora + timedelta(hours=horas_intervalo * 3 )

#quarta = horas_agora + timedelta(hours=  horas_intervalo * 4 )

#print(f"Proxima DOSE : {futuro.hour:02d}:{futuro.minute:02d} ")

#print(f"SEGUNDA DOSE: {segunda.hour:02d}:{segunda.minute:02d}  ")


#print(f"Terceira DOSE:  {terceira.hour:02d}:{terceira.minute:02d}  ")


#print(f"quarta  DOSE:  {quarta.hour:02d}:{quarta.minute:02d}  ")
####Mostre um número inteiro (d) ocupando pelo menos 2 posições (2),
# ### colocando 0 na frente quando necessário.
print(f"dose pulada: {pular_dose}")
print(f"Quantidade: {calculo_doses}")
for i in range(1, calculo_doses + 1): ##o input que eu insire no PROPRIO IUNPUT tem INT convertido de string #entao eu aplico quantas vezes eu quiser
    if i == pular_dose:
        continue
     #$ """"""SE i for igual a pular_dose, CONTINUE para a próxima repetição.""""""""""""
    
    numero_dose = i
    multiplicador = i # criei uma  variavel chamada multiplicador que recebe i
        
        #proxima_dose = i #1,2,3,4,5 dose 
        #eu removi proxima dose pq nao faz sentido ele recebe um contador 1,2,3,4,5
    # print(i)
    proxima_dose = horas_agora + timedelta(hours=horas_intervalo * multiplicador ) 

    print(f"dose: {numero_dose} : {proxima_dose.hour:02d}:{proxima_dose.minute:02d} ")


        