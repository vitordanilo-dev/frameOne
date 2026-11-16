# import cv2

# # camera = cv2.VideoCapture(0)

# # if camera.isOpened():
# #     print('CAMERA CONECTADA')

# # else:
# #     print('erro')
# #     camera.release()
 

# camera = cv2.VideoCapture(0)

# sucesso, frame = camera.read()

# print(sucesso)

# camera.release()

# import cv2

# camera = cv2.VideoCapture(0)

# sucesso, frame = camera.read()

# if sucesso:
#     cv2.imshow("Minha câmera", frame)
#     cv2.waitKey(0)

# camera.release()
# cv2.destroyAllWindows()


# def verificar_fps(fps):

#     if fps <= 0 :
#         raise ValueError('FPS INVÁLIDO')
#         return false
    
#     print('Câmera conectada com sucesso.')


# try:
#     resultado = verificar_fps(-10)
 
#     print(resultado)


# except ValueError as erro:
#     print(f'ERRO: {erro}')


# Abrindo nossos recursos de câmera, responsabilidade abrir a câmera.

import cv2



def abrir_camera():

    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        raise RuntimeError ('Erro ao abrir a câmera')
    
    largura = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


    return [camera, largura, altura]



def abrir_gravacao(largura, altura):

    gravador = cv2.VideoWriter(

        'video_teste.mp4',
         cv2.VideoWriter_fourcc(* 'mp4v'),
         60.0,
         (largura, altura)

    )

    if not gravador.isOpened():
        raise RuntimeError('Erro ao abrir a gravação')
    
    return gravador



def capturar_frames(camera):
    
     sucesso, frame = camera.read()

     if not sucesso:
        raise ValueError('Falha ao receber frames.')
    
     cv2.imshow('captura', frame)
     return frame



def gravando_frames(gravador, frame):

     gravador.write(frame)

     if frame is None:
        raise ValueError('Erro ao gravar os frames') 

     return gravador 



# Abrindo nosso Sistema, responsabilidade iniciar nossa aplicação , camera e gravador 

def abrir_sistema():

        try:
            
         camera, largura, altura = abrir_camera()

         gravadores = abrir_gravacao(largura ,altura)

         while True:

          video = capturar_frames(camera)

          frames = gravando_frames(gravadores, video)


          if cv2.waitKey(1) & 0xff == ord('q'):
            print('gravação finalizada com sucesso')
            break

        except RuntimeError as erro:
            print(f'Erro: {erro}')
        
        except ValueError as erro:
            print(f'Erro: {erro}')


        finally:
            camera.release()
            gravadores.release()
            cv2.destroyAllWindows()
            print('Recursos liberados com sucesso')


abrir_sistema()
# 08/11
# documentação dias 07/11 e 08/11. Funções evoluiram, onde todo o fluxo esta funcionando e gravando frames e guardando em um arquivo mp4. 
# alguns tratamentos de erros foram colocados tambem, evolui durante a semana esse codigo





