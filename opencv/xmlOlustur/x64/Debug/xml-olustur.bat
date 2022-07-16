:aktif sürücüye geçildi
%~d0

:aktif klasöre geçildi
cd %~dp0

:numNeg in sağına negatif.txt dosyasındaki negatif resim sayısı yazılır
:numPos<=(Vektör dosyasında toplam pozitif örnek sayısı-Negatif örnek sayısı)/(1+(aşama sayısı-1)*(1-minhitrate))) 
:200 tane pozitif, 100 tane negatif resim için ve 5 aşama için numPos degerini 98 alabilirsiniz.
opencv_traincascade.exe -data cascade -vec pozitifResim.vec -bg negatif.txt -numPos 98 -numNeg 100 -numStages 5 -minHitRate 0.995 -maxFalseAlarmRate 0.25 -mem 10240 -w 24 -h 24

pause