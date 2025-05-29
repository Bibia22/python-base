import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

while True:

    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break
    
    if all(info.values()):
        break

    for key in keys:
        if info[key] is not None:
            continue
        try:
           info[key] = int(input(f"{key}?").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break
            
temp, umidade = info.values()

if temp > 45:
    print("ALERTA!!! Perigo de calor extremo")
elif temp * 3 >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and <= 10:
    print("Frio") 
elif temp < 0:
    print("ALERTA!!! Frio extremo")
