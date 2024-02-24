# simple-ransomware

Os paketini ve cryptography paketi içerisinde bulunan fernet şifreleme algoritmasını kullandım.

Socket paketini kullanarak internet bağlantısı kontrolu yaptım bu sayede mail gönderiminde eğer internetim yoksa bir sonsuz döngü başlicak ve internete bağlanma gerçekleşene kadar devam edicek.

time paketi ile mail gönderimi denemelerini 5 saniyede bir olacak şekilde sınırladım.

Smtp paketini kullanarak oluşturulan anahtarın kendi mailime gönderimini sağladım.

Ransomware içinde bulunduğu klasörde olan bütün dosyaları şifrelemek için kullanılır, Ransomdecrypter ise bu şifreyi çözmek için yazılmış koddur oluşturulan anahtarı istenilen girişe yazarak dosyalar şifreden kurtulur.

Fernet, simetrik bir şifreleme algoritmasıdır yani bu demek oluyorki tek anahtar ile hem şifreleme hemde çözme işlemi yapılabilir.

Fernet veri bütünlüğünü sağlamak için Hash-based Message Authentication Code kullanır.Bu verinin aynı kaldığının yani değiştirilmediğini doğrulamak için kullanılır.
