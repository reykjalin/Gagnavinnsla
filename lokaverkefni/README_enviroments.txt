til að láta forritið virka á Windows, með anaconda þarf að hafa python 2.7
til þess þarf:
1. conda create --name python27 python=2.7
	til að búa til python2.7 enviroment í ankoncda
2. slá inn: activate python27
	til að fara í python2.7
	nú virkar skipanir eins og pip, python við python 2.7
3. Installa pakkar sem þarf til að keyra skrá með því að slá in:
	pip install geopy
	(best að nota conda installer í stað fyrir pip, því þá finnur conda besta útgafu fyrir einviroment sem maðu er í)
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
	 	
4. Ef kemur ASCII villa, þarf að bæta í efsta línu í kóðan # coding=utf-8	
5. Til að fara ut úr enviroment slá in: deactivate

til að activate enviroment aftur seinna, þarf að slá in: activate python27

Mac: 
Til þess að setja upp eftirfarandi pakka í mac þarf að skrifa eftirfarandi inn í terminal.

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