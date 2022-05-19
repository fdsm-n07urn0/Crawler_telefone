import time
import threading

def fazer_requisicao_web():
    print('Fazendo requisição web...')
    time.sleep(3)
    print('Terminei a requisição')


# Pra fazer mais de uma requisição ao mesmo tempo
thread_1 = threading.Thread(target=fazer_requisicao_web)   # Colocar fazer_requisicao_web sem () no final
thread_1.start()

thread_2 = threading.Thread(target=fazer_requisicao_web)   # Colocar fazer_requisicao_web sem () no final
thread_2.start()

thread_3 = threading.Thread(target=fazer_requisicao_web)   # Colocar fazer_requisicao_web sem () no final
thread_3.start()


#print('Chegou aqui')
#for i in range(10):
    #fazer_requisicao_web()