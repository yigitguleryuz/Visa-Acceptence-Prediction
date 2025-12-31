# Visa-Acceptence-Prediction
# Kullanılan Teknolojiler
Dil: Python
Veri Analizi & ML: Pandas, NumPy, Scikit-learn, LazyPredict
Backend: FastAPI, Uvicorn, Pydantic
Frontend: GEMINI
Model Depolama: Pickle

IT Project management dersinde hazırladğımız Visa Application Roof için basit bir taslak tool hazırladım. Hazırladığımız sentetik dataseti önce gerekli preprocess, scaling ve encoding işlemlerinden geçirdim.

<img width="601" height="272" alt="image" src="https://github.com/user-attachments/assets/d8999d2a-a969-4f7f-870a-e0b8eeb54bd3" />

Daha sonra bir Logistic Regression ML modeli oluşuturdum. 

<img width="839" height="346" alt="image" src="https://github.com/user-attachments/assets/e66a6e5f-7d84-4f5b-9efe-59662a53cd42" />

Bu modeli Pickle kullanarak pyCharm IDE'sine aktardım.

<img width="417" height="187" alt="image" src="https://github.com/user-attachments/assets/56b710a3-3071-4062-9eb2-fa79dab1517b" />

Kaydettiğim bu model ile https://github.com/atilsamancioglu/DiamondMLProject projesinden yararlanarak kendime bir basit backend oluşturdum. Ve pickle ile aldığım ML modelini FastAPI ve Uvicorn kullanarak ürüne dönüştürmeye çalıştım. Frontend için TAMAMEN YAPAY ZEKA kullandım.

<img width="1364" height="719" alt="image" src="https://github.com/user-attachments/assets/566ac9c6-f5ea-4793-9356-e95d37174853" />

Kullanıcının verdiği bilgilere göre predict ve predict_proba modüllerini işleyerek bize geri bildiriyor.

<img width="401" height="515" alt="image" src="https://github.com/user-attachments/assets/9cfb066f-0437-4b80-a1ac-ed83226b835d" />

Ayrıca site içinde yapılan tahmin oranlarını canlı olarak görüntüleyebilir, ve ülkelerin kabul oranlarına bakabilirsiniz.

<img width="270" height="588" alt="image" src="https://github.com/user-attachments/assets/b6547eb9-59b0-4737-95ce-1b0066df9f1b" />

