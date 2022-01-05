import cv2  # Se importa cv para procesar la imagen.
import face_recognition  # Se importa face_recognition, que tiene modelos precargados.

# Se indica que será capturado un archivo de video.
video_capture = cv2.VideoCapture(0)
face_locations = []

# Se indica un ciclo que será el encargado de repetir para encontrar rostros.
while True:
    # Tomamos un único cuadro del video
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Conversión de BGR a RGB.

    # Encuentra todos los rostros en el cuadro actual.
    face_locations = face_recognition.face_locations(rgb_frame)

    # Se crea un rectángulo que rodeará cada rostro reconocido.
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Muestra los resultados
        cv2.imshow('Video', frame)

        # Se indica la tecla de escape
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
