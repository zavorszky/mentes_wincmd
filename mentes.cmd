@echo off
rem -- chcp 65001

rem --
rem -- Felhaszn l s:
rem --   MENTES.CMD log_file_path_and_name
rem --

setlocal

rem -- Ha nincs megadva .log file n‚v, akkor a napl¢ file az
rem -- aktu lis k”nyvt rba kerl ‚s a neve "mentes.log" lesz,
if "%1"=="" (
    set z9logfilename=mentes.log
) else (
    set z9logfilename=%1
)

echo . 
echo . Ment‚s WinCmd (v2.0)
echo . --------------------
echo . K‚rem csatlakoztassa a pendrive-ot az I: meghajt¢hoz!
echo . 
echo . A folytat shoz nyomjon egy (Enter)-t,
echo . vagy (Ctrl-C)-vel megszak¡thatja az ind¡t st.
echo .
pause > nul
echo .
echo . A ment‚s elindult...

if not exist %z9logfilename% echo "create %z9logfilename%" > %z9logfilename%
call mentes_mag.cmd >> %z9logfilename%

@echo off
echo .
echo . A ment‚s k‚sz.
echo . Az ablak bez r s hoz nyomjon egy (Enter)-t.
pause > nul

endlocal
