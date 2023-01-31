import cv2
import face_recognition as fr
imgVin = fr.load_image_file(r'C:\Users\marce\OneDrive\Área de Trabalho\Imagens-prog\Vinicius.jpg')
imgJason = fr.load_image_file(r'C:\Users\marce\OneDrive\Área de Trabalho\Imagens-prog\Jason.jpg')
imgVin2 = fr.load_image_file(r'C:\Users\marce\OneDrive\Área de Trabalho\Imagens-prog\Vin2.jpg')
imgChris = fr.load_image_file(r'C:\Users\marce\OneDrive\Área de Trabalho\Imagens-prog\Chris.jpg')

imgVin=cv2.cvtColor(imgVin, cv2.COLOR_BGR2RGB)
imgJason= cv2.cvtColor(imgJason, cv2.COLOR_BGR2RGB)
imgVin2 = cv2.cvtColor(imgVin2, cv2.COLOR_BGR2RGB)
imgChris = cv2.cvtColor(imgChris, cv2.COLOR_BGR2RGB)

faceLoc = fr.face_locations(imgVin)[0]
print(faceLoc)
cv2.rectangle(imgVin, (faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]), (0, 255, 0), 2)


encodeVin = fr.face_encodings(imgVin)
encodeJas = fr.face_encodings(imgJason)[0]
encodeVin2 = fr.face_encodings(imgVin2)[0]
encodeChris = fr.face_encodings(imgChris)[0]

print(encodeChris)
print('-----')
print(encodeVin)

comparacao1 = fr.compare_faces(encodeVin, encodeVin2)
print('Vinícius é a mesma pessoa que Vinícius?', comparacao1)


cv2.imshow('Vinicius', imgVin)

cv2.imshow('Vinicius', imgVin2)
cv2.waitKey(1500)

comparacao2 = fr.compare_faces(encodeVin, encodeJas)
print('Vinícius é a mesma pessoa que Jason?', comparacao2)
cv2.imshow('Vinicius', imgVin)
cv2.imshow('Jason',imgJason)
cv2.waitKey(1500)

comparacao3 = fr.compare_faces(encodeVin, encodeChris)
print('Vinícius é a mesma pessoa que Chris?', comparacao3)

cv2.imshow('Vinicius', imgVin)
cv2.imshow('Chris', imgChris)
cv2.waitKey(0)