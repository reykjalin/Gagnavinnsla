til a� l�ta forriti� virka � Windows, me� anaconda �arf a� hafa python 2.7
til �ess �arf:
1. conda create --name python27 python=2.7
	til a� b�a til python2.7 enviroment � ankoncda
2. sl� inn: activate python27
	til a� fara � python2.7
	n� virkar skipanir eins og pip, python vi� python 2.7
3. Installa pakkar sem �arf til a� keyra skr� me� �v� a� sl� in:
	pip install geopy
	(best a� nota conda installer � sta� fyrir pip, �v� �� finnur conda besta �tgafu fyrir einviroment sem ma�u er �)
	 conda install -c https://conda.anaconda.org/anaconda PAKKI
	 	Pakkar:
	 	1. basemap
	 	2. pandas
	 	3. matplotlib
	 	4. numpy
	 	5. pillow
	 	6. sqlalchemy 
	 	7. pygeocoder
		8. psycopg2
	 	
4. Ef kemur ASCII villa, �arf a� b�ta � efsta l�nu � k��an # coding=utf-8	
5. Til a� fara ut �r enviroment sl� in: deactivate

til a� activate enviroment aftur seinna, �arf a� sl� in: activate python27

Mac: 
Til �ess a� setja upp eftirfarandi pakka � mac �arf a� skrifa eftirfarandi inn � terminal.

basemap		: pip3 install basemap --allow-all-external --allow-unverified basemap
geopy		: pip3 install geopy
pandas		: pip3 install pandas
matplotlib	: pip3 install matplotlib
numpy		: pip3 install numpy
SQLAlchemy 	: pip3 install sqlalchemy
pygeocoder 	: pip3 install pygeocoder
psycopg2 	: pip3 install psycopg2
moviepy		: pip3 install moviepy
Pillow 		: pip3 install Pillow