segundos = float(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = segundos // 86400
horas = segundos // 3600 - dias * 24
minutos = segundos // 60 - (horas * 60) - (dias * 1440)
seg = segundos - (dias * 86400) - (horas * 3600) - (minutos * 60)
print(int(dias),"dias", int(horas),"horas", int(minutos),"minutos", int(seg),"segundos")


