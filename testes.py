# # rascunho FrameOne, arquivo usado para testes e aplicação de novos conhecimentos


# import cv2

# # Aqui o programa acessa a  camera do meu note, com a classe do video capture, atraves da instancia que eu estou criando. (camera)
# camera = cv2.VideoCapture(0)


# # Aqui o codigo so entrará nesse if se a camera não abrir, pois isopened faz essa validacao
# if not camera.isOpened():
#     raise RuntimeError('Erro ao abrir a Câmera')
#     exit()   # Aprendi esse metodo novo, onde finaliza o programa inteiro

# # Aqui o código serve para pegar as informacoes de largura e altura da camera que esta sendo utilizada na videocapture
# largura = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# altura = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


# gravador = cv2.VideoWriter(
#     "meu_video.mp4",
#     cv2.VideoWriter_fourcc(*"mp4v"),
#     30.0,
#     (largura,altura)
#     )


# if not gravador.isOpened():
#     print('Erro ao inicar a câmera')
#     camera.release()
#     exit()

# while True:
#     sucesso, frame = camera.read()

#     if not sucesso:
#         break

#     # altura, largura, canais = frame.shape

#     # frame[0:altura//2, :] = [0,0,0]
    

#     gravador.write(frame)

#     cv2.imshow('Sistema de replay', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# camera.release()
# gravador.release()
# cv2.destroyAllWindows()

# print("video finalizado")







