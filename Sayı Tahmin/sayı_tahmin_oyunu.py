
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0  # attempts değişkenini burada başlatıyoruz

    print("1 ile 100 arasında bir sayı tuttum. Bakalım bilebilecek misin?")

    while True:
        try:
            guess = int(input("Tahminin nedir?: "))  # Kullanıcıdan tahmin al
            attempts += 1  # Deneme sayısını bir artır

            if guess < number_to_guess:
                print("Daha büyük bir sayı dene.")
            elif guess > number_to_guess:
                print("Daha küçük bir sayı dene.")
            else:
                print(f"Tebrikler! {attempts} denemede doğru tahmin ettin.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")  # Geçersiz girdi durumu
if __name__ == "__main__":
    guess_the_number()


