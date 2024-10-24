@echo off

set mentes_teszt=N

setlocal

echo .
echo . #####################################################
echo . Alkalmaz s_________: mentes_wincmd
echo . Modul______________: Ment‚s mag (menets_mag.cmd)
echo . Ment‚s teszt (I/N) : %mentes_teszt%
echo .
echo . %date% %time%

rem -- A t”m”r¡t‹ program be ll¡t sa (k”rnyezeti v ltoz¢: set_ffn_7z)

call e:\felhasznalok\dady\sajat_programok\_ini_\set_ffn_7z.cmd

rem -- Kezd‚si id‹ feljegyz‚se

set z9kezdido=%time%

rem -- Ment‚sek

if /I "%mentes_teszt%"=="N" goto c_mentes_kezdete
goto c_mentes_vege

:c_mentes_kezdete

rem -- Egyedi tesztel‚shez 'if'-ek
if 1==1 %ffn_7z% a -r i:\mentes\konyvtarak                      h:\DADY\rend\konyvtarak\
if 1==1 %ffn_7z% a    i:\mentes\rend                            h:\DADY\rend\rend\
if 1==1 %ffn_7z% a -r i:\mentes\sajat_programok\_ini_           e:\felhasznalok\dady\sajat_programok\_ini_\
if 1==1 %ffn_7z% a -r i:\mentes\sajat_programok\mentes          e:\felhasznalok\dady\sajat_programok\mentes\
if 1==1 %ffn_7z% a -r i:\mentes\sajat_programok\python_packages e:\felhasznalok\dady\sajat_programok\python_packages\

:c_mentes_vege

rem -- Befejez‚si id‹ feljegyz‚se

set z9befido=%time%

rem -- T”m”r¡t‚si id‹ kisz m¡t sa, ki¡r sa

rem -- Az id‹pontok (centisec = sz zad m sodperc)-re konvert lva
set /A kezdido_csec=(1%z9kezdido:~0,2%-100)*360000 + (1%z9kezdido:~3,2%-100)*6000 + (1%z9kezdido:~6,2%-100)*100 + (1%z9kezdido:~9,2%-100)
set /A befido_csec=(1%z9befido:~0,2%-100)*360000 + (1%z9befido:~3,2%-100)*6000 + (1%z9befido:~6,2%-100)*100 + (1%z9befido:~9,2%-100)

rem -- V‚grehajt si id‹ kisz m¡t sa sz zad m sodpercben
set /A vegrehajtasido_csec=%befido_csec%-%kezdido_csec%

rem -- A v‚grehajt si id‹ felbont sa ¢r ra, percre, m sodpercre
set /A vegrehajtasido_h=%vegrehajtasido_csec% / 360000
set /A vegrehajtasido_min=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000) / 6000
set /A vegrehajtasido_sec=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000 - %vegrehajtasido_min%*6000) / 100
set /A vegrehajtasido_sec2=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000 - %vegrehajtasido_min%*6000 - %vegrehajtasido_sec%*100)

rem -- Form z s, 0-val kieg‚sz¡t‚s, ha kell
if %vegrehajtasido_h% LSS 10 set vegrehajtasido_h=0%vegrehajtasido_h%
if %vegrehajtasido_min% LSS 10 set vegrehajtasido_min=0%vegrehajtasido_min%
if %vegrehajtasido_sec% LSS 10 set vegrehajtasido_sec=0%vegrehajtasido_sec%
if %vegrehajtasido_sec2% LSS 10 set vegrehajtasido_sec2=0%vegrehajtasido_sec2%

rem -- Ki¡r s
rem -- echo Kezd‚s id‹pontja___: %kezdido_csec% [centisecond]
rem -- echo Befejez‚s id‹pontja: %befido_csec% [centisecond]
rem -- echo V‚grehajt s ideje__: %vegrehajtasido_csec% [centisecond]
echo . Ment‚s kezdete___: %z9kezdido%
echo . Ment‚s befejez‚se: %z9befido%
echo .
echo . Ment‚s/t”m”r¡t‚s-re ford¡tott id‹
echo . %vegrehajtasido_h% h  %vegrehajtasido_min% m  %vegrehajtasido_sec%,%vegrehajtasido_sec2% s

endlocal
