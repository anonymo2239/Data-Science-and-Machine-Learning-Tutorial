from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
from sklearn.model_selection import train_test_split

spinach_data = "C:/Users/Alperen Arda/OneDrive/Desktop/ispanak.csv"
ready_data = pd.read_csv(spinach_data, sep=';', decimal=',')  # noktalı virgül ayırıcı ve virgül ondalık ayırıcı

# Verileri kontrol et
print("Veri örneği:")
print(ready_data.head())
print("\nSütun isimleri:", ready_data.columns)

# Verileri ayır
y = ready_data.iloc[:, 1]  # İkinci sütun
X = ready_data.iloc[:, 0].values.reshape(-1, 1)  # İlk sütun

# Eğitim ve test setlerine ayır
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Model oluştur ve eğit
model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)

# Tahmin yap
predicted = model.predict(val_X)

# Hata hesapla
error = mean_absolute_error(val_y, predicted)
print(error)