ATH: TÖFLUR VERÐA AÐ HEITA ÞAÐ SAMA OG Í SCHEMA, ANNARS VIRKA LEITARQUERY EKKI

-------------------- Í hvaða röð skal keyra skrár? --------------------
1. readcsv.py keyrð til að búa til insert skipanir fyrir gagnagrunn.
   ATH: skráarnöfn sem lesið er úr eru harðkóðuð
2. insert_to_db.py keyrt til að lesa insert skipanir í gagnagrunn.
   Ætti ekki að taka meira en 5 mínútur.
3. MAIN_PROGRAM.py keyrt til að keyra forrit


-------------------- Hvernig á að keyra forritið með theme  --------------------
Windows:
	1. Vera með Python 3.4.3 (eldri útgáfur ættu að virka, 3.5 styður þemað ekki
	   vegna þess að dependencie er PySide)
	2. Sækja þessa skrá fyrir PySide: https://pypi.python.org/packages/3.4/P/PySide/PySide-1.2.2-cp34-none-win_amd64.whl#md5=f02e4b44109cc1d0db980a44484f6f90
	3. Opna möppuna þar sem pyside .whl skráin er vistuð í cmd og keyra:
	   pip install nafn-á-pyside-whl.whl
	4. Til að sækja þemað: pip install qdarkstyle

Mac:
	Slá eftirfarandi inn í terminal: 
	1. brew install pyside --with-python3
	2. pip3 install qdarkstyle

Linux:
	1. Opna package manager, sækja python3-pyside pakkann
	2. Sækja þemað: pip3 install qdarkstyle


-------------------- Keyra forritið án þema (t.d. fyrir Python 3.5) --------------------
1. Kommenta út línur 2, 102 og 302 í kóða. (Komment fyrir aftan segir: "For dark theme")
2. Good to go!
