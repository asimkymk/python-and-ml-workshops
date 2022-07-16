#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp> 
#include <iostream>
#include <stdio.h>
#include <opencv2\opencv.hpp>
#include <conio.h>
#include <fstream>
#include <string>

using namespace std;
using namespace cv;

void anaMenu();

//programýn en fazla kaydedebileceði pozitif ve negatif resim sýnýrý
int pozitifResimSiniri = 200;
int negatifResimSiniri = 100;

//cascade iþleminde program önceki adýmlarýn üzerine yazmadan
//yani onlarý silmeden (stage2.xml gibi) 
//sýnýflandýrmaya baþladýðýndan programýn hata vermemesi
//için her adýmda cascade klasörü boþaltýldý.
void cascadeKlasoruSil()
{
	char komut[200];
	_snprintf_s(komut, 200, "del /q cascade\\*.xml");
	system(komut); //cascade klasöründeki xml dosyalari silindi
}

//önceki eðitimlerden kalan kalýntýlarý temizler
void dosyalariSil()
{
	char komut[200];

	_snprintf_s(komut, 200, "del /q pozitif\\*.*");
	system(komut); //pozitif klasörü boþaltýldý

	_snprintf_s(komut, 200, "del /q negatif\\*.*");
	system(komut);//negatif klasörü boþaltýldý

	system("del / q pozitifResim.vec");

	//text dosyalarýnýn içi boþaltýldý
	ofstream file;

	file.open("negatif.txt");
	file << "";
	file.close();

	file.open("pozitif.txt");
	file << "";
	file.close();

	file.open("resimSayisiPozitif.txt");
	file << 0;
	file.close();

	file.open("resimSayisiNegatif.txt");
	file << 0;
	file.close();

	//clear screen yani ekraný sil komutu 
	system("cls");
	anaMenu();
}

char kameraPenceresiAdi[60] = "Nesne Takip";

int negatifResimSayisi()
{
	string satir;
	ifstream myfile("resimSayisiNegatif.txt");

	getline(myfile, satir);
	getline(myfile, satir);
	myfile.close();

	int sayi = atoi(satir.c_str()); //string ifade integer'a çevrildi
	return sayi;
}

int pozitifResimSayisi()
{
	string satir;
	ifstream myfile("resimSayisiPozitif.txt");

	getline(myfile, satir);
	myfile.close();

	int sayi = atoi(satir.c_str()); //string ifade integer'a çevrildi
	return sayi;
}

void negatifResimSayisiKaydet(int sayi)
{
	ofstream file;
	file.open("resimSayisiNegatif.txt");
	file << sayi;
}

void pozitifResimSayisiKaydet(int sayi)
{
	ofstream file;
	file.open("resimSayisiPozitif.txt");
	file << sayi;
}

//pozitif resimleri kaydeder
int pozitifSayici = 0;
void pozitifResimKaydet()
{
	VideoCapture vid(0);

	pozitifSayici = pozitifResimSayisi();

	namedWindow(kameraPenceresiAdi, CV_WINDOW_AUTOSIZE);

	ofstream file;
	file.open("pozitif.txt", ios::app);

	Mat arka; //üzerine çizgi çizmek ve yazý yazmak için kullanýlan deðiþken.

	vector<int> sparam;
	sparam.push_back(CV_IMWRITE_JPEG_QUALITY);
	sparam.push_back(50);

	char yazi[250]; //yüzde d li terimleri yazabilmek için kullanýlan dizi

	int genislik = 120;
	createTrackbar("Genislik", kameraPenceresiAdi, &genislik, 320);
	int yukseklik = 120;
	createTrackbar("Yukseklik", kameraPenceresiAdi, &yukseklik, 240);
	int xeks1 = 200, xeks2 = 440, yeks1 = 120, yeks2 = 360;

	//pozitif resim kaydýna hemen baþlama,
	//b tuþuna basmayý bekle
	int basla = -1;

	while (true)
	{
		char a = waitKey(33);

		//27 sayisi esc tuþunun ascii tablosundaki karþýlýðýdýr.
		if ((a == 27) || (pozitifSayici > pozitifResimSiniri - 1))
		{
			file.close();
			destroyAllWindows();
			pozitifResimSayisiKaydet(pozitifSayici);
			break;
		}

		Mat frame;
		vid.read(frame);
		flip(frame, frame, 1);

		xeks1 = (640 - (genislik * 2)) / 2;
		xeks2 = xeks1 + (genislik * 2);
		yeks1 = (480 - (yukseklik * 2)) / 2;
		yeks2 = yeks1 + (yukseklik * 2);

		arka = Mat::zeros(frame.size(), frame.type());
		line(arka, Point(xeks1, 0), Point(xeks1, 480), Scalar(0, 255, 0), 1); //arka plana belirlenen büyüklükte frame oluþturulur. 
		line(arka, Point(xeks2, 0), Point(xeks2, 480), Scalar(0, 255, 0), 1);
		line(arka, Point(0, yeks1), Point(640, yeks1), Scalar(0, 255, 0), 1);
		line(arka, Point(0, yeks2), Point(640, yeks2), Scalar(0, 255, 0), 1);

		if (basla == -1) //eðer foto kaydý baþlamadýysa bilgilendirme yazisi için.
		{
			putText(arka, "Nesneyi Ekranin Ortasina Tutunuz", Point(20, 30), CV_FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));
			putText(arka, "'b' tusu ile egitime baslayiniz…", Point(20, 60), CV_FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));
			putText(arka, "cikis icin esc tusuna basili tutunuz.", Point(10, 460), CV_FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));
		}
		if (a == 'b') //klavyeden b ye basýlýrsa baslayý deðiþtirir. 
			basla = basla*(-1);

		if (basla == 1)
		{
			pozitifSayici++;

			char resimYazisi[60]; //yazilacak resim icin karakter dizisi olusturuluyor 
			_snprintf_s(resimYazisi, 60, "Resim Ekleniyor: %d", pozitifSayici);
			putText(arka, resimYazisi, Point(10, 30), CV_FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));

			//belirtilen yola resim kaydedildi.
			_snprintf_s(yazi, 250, "pozitif/%d.jpg", pozitifSayici);
			imwrite(yazi, frame, sparam);

			//text dosyasýna resim yolu kaydedildi
			_snprintf_s(yazi, 250, "pozitif\\%d.jpg", pozitifSayici);
			file << yazi << " 1 " << xeks1 << " " << yeks1 << " " << (genislik * 2) << " " << (yukseklik * 2) << endl; //belirtilen yolla beraber kýrpýlma oraný girildi. 
		}
		frame = frame + arka; //webcamdan alýnan frame e yazýlar ve çizgiler eklenerek kullanýcýya gösterildi. 
		imshow(kameraPenceresiAdi, frame);
	}
}

void pozitifResimKýrp()
{
	char komut[200];
	_snprintf_s(komut, 200, "opencv_createsamples.exe -info pozitif.txt -num %d -vec pozitifResim.vec -w 24 -h 24", pozitifSayici);
	system(komut);

	system("cls");
	anaMenu();
}

int negatifSayici;
void negatifResimKaydet()
{
	VideoCapture vid(0);

	negatifSayici = negatifResimSayisi();

	ofstream file;
	file.open("negatif.txt", ios::app);

	vector<int> sparam;
	sparam.push_back(CV_IMWRITE_JPEG_QUALITY);
	sparam.push_back(50);
	char yazi[250];
	while (true)
	{
		if ((waitKey(33) == 27) || (negatifSayici > negatifResimSiniri - 1))
		{
			file.close();
			destroyAllWindows();
			negatifResimSayisiKaydet(negatifSayici);
			break;
		}

		Mat frame;
		vid.read(frame);
		flip(frame, frame, 1);

		negatifSayici++;

		_snprintf_s(yazi, 250, "negatif/%d.jpg", negatifSayici);
		imwrite(yazi, frame, sparam);

		_snprintf_s(yazi, 250, "negatif\\%d.jpg", negatifSayici);
		file << yazi << endl;

		char resimYazisi[60]; //yazilacak resim icin karakter dizisi olusturuluyor 
		_snprintf_s(resimYazisi, 60, "Resim Ekleniyor: %d", negatifSayici);
		putText(frame, resimYazisi, Point(10, 30), CV_FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));

		imshow(kameraPenceresiAdi, frame);
	}
	vid.release(); //kamerayý kapattý
	system("cls");
	anaMenu();
}

void xmlDosyasiOlustur()
{
	float minHitRate = 0.995;

	int asamaSayisi;
	cout << "Asama sayisini giriniz. Ornegin 17 olabilir)" << endl;
	cin >> asamaSayisi;

	pozitifSayici = pozitifResimSayisi();
	negatifSayici = negatifResimSayisi();
	cout << "Pozitif Resim Sayisi: " << pozitifSayici << endl;
	cout << "Negatif Resim Sayisi: " << negatifSayici << endl;
	cout << "Asama Sayisi: " << asamaSayisi << endl;
	cout << "minHitRate: " << minHitRate << endl;

	int numPos = floor((pozitifSayici - negatifSayici) / (1 + (asamaSayisi - 1)*(1 - minHitRate)));
	cout << "numPos: " << numPos << endl;

	system("pause");

	char komut[500];
	_snprintf_s(komut, 500, "opencv_traincascade.exe -data cascade/ -vec pozitifResim.vec -bg negatif.txt -numPos %d -numNeg %d -numStages %d -minHitRate 0.995 -maxFalseAlarmRate 0.25 -mem 1024 -w 24 -h 24", numPos, negatifSayici, asamaSayisi);
	system(komut);

	system("cls");
	anaMenu();
}

void ilkKurulum()
{
	system("mkdir cascade");
	system("mkdir negatif");
	system("mkdir pozitif");
}

void anaMenu()
{
	system("cls");

	cout << "----------------------------------------" << endl;
	cout << "	Hosgeldiniz." << endl;
	cout << "	Ne yapmak istersiniz?" << endl;
	cout << "----------------------------------------" << endl;
	cout << "	1. Pozitif resim kaydet" << endl;
	cout << "	2. Negatif resim kaydet" << endl;
	cout << "	3. XML dosyasi olustur" << endl;
	cout << "	4. Tum verileri sil" << endl;
	cout << "	0. Programi Kapat" << endl;
	cout << "----------------------------------------" << endl;
	cout << "	Seciminiz: ";
	int secim;
	cin >> secim;

	switch (secim)
	{
	case 0:
		return;
		break;
	case 1:
		cascadeKlasoruSil();
		pozitifResimKaydet();
		pozitifResimKýrp();
		break;
	case 2:
		cascadeKlasoruSil();
		negatifResimKaydet();
		break;
	case 3:
		xmlDosyasiOlustur();
		break;
	case 4:
		cascadeKlasoruSil();
		dosyalariSil();
		break;
	}
}

int main(int argc, const char** argv)
{
	ilkKurulum(); //olmasý gereken klasörleri oluþturuyor.
	anaMenu();

	return 0;
}