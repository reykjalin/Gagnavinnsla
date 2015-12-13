til að láta forritið virka á Windows, með anaconda þarf að hafa python 2.7
til þess þarf:
1. conda create --name python27 python=2.7
	til að búa til python2.7 enviroment í ankoncda
2. slá inn: activate python27
	til að fara í python2.7
	nú virkar skipanir eins og pip, python við python 2.7
3. Installa pakkar sem þarf til að keyra skrá með því að slá in:
	(best að nota conda installer í stað fyrir pip, því þá finnur conda besta útgafu fyrir einviroment sem maðu er í)
	 conda install -c https://conda.anaconda.org/anaconda PAKKI
	 	Pakkar:
	 	1. basemap
	 	2. pandas
	 	3. matplotlib
	 	4. geopy
	 	5. numpy
	 	6. pil
4. Ef kemur ASCII villa, þarf að bæta í efsta línu í kóðan # coding=utf-8	
5. Til að fara ut úr enviroment slá in: deactivate

til að activate enviroment aftur seinna, þarf að slá in: activate python27