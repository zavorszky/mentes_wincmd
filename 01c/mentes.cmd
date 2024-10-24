@echo off
rem -- chcp 65001
chcp 852

rem --
rem -- Felhaszn l s:
rem --   MENTES.CMD log_file_path_and_name [-KIKAPCS]
rem --

setlocal

if "%1"=="" goto c_nincs_param

if /i "%1"=="-KIKAPCS" goto c_az_elso_param_kikapcs

if "%2"=="" goto c_mentes

if /i "%2"=="-KIKAPCS" goto c_mentes

goto c_a_masodik_param_nem_kikapcs

:c_mentes
echo . 
echo . Ment‚s WinCmd (v01c)
echo . --------------------
echo . Napl¢  llom ny: %1
if /i "%2"=="-KIKAPCS" (
    echo . Kikapcsol s ment‚s ut n: Igen
) else (
    echo . Kikapcsol s ment‚s ut n: Nem
)
echo .
echo . K‚rem csatlakoztassa a pendrive-ot az I: meghajt¢hoz!
echo . 
echo . A folytat shoz nyomjon egy (Enter)-t,
echo . vagy (Ctrl-C)-vel megszak¡thatja az ind¡t st.
echo .
pause > nul
echo .
echo . A ment‚s elindult...

if not exist %1 echo "create %1" > %1

if 1==1 call mentes_mag.cmd >> %1

echo .
echo . A ment‚s k‚sz.

if /i "%2"=="-KIKAPCS" (
    echo .
    echo . Indul a kikapcsol s...
    rem -- shutdown /s /f /p /d p:0:0 /c "Ment‚s  s le ll¡t s"
)

goto c_vege_es_pause

rem --
rem --

:c_nincs_param
echo .
echo . Hib s ind¡t s! Nincs megadva param‚ter.
goto c_segitseg

:c_az_elso_param_kikapcs
echo .
echo . Hib s ind¡t s! Az els‹ param‚ter nem lehet a -KIKAPCS.
goto c_segitseg

:c_a_masodik_param_nem_kikapcs
echo .
echo . Hib s ind¡t s! A m sodik param‚ter csak -KIKAPCS lehet vagy hi nyozhat.
goto c_segitseg

:c_segitseg
echo .
echo . H¡v s:
echo .   MENTES.CMD log_file_path_and_name [-KIKAPCS]

:c_vege_es_pause

echo .
echo . A folytat shoz nyomjon egy (Enter)-t
pause > nul

:c_vege

endlocal
