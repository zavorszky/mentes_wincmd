# Mentés Win10 batch script-tel

## A probléma

Az előző (00a, 01a, 01b, 01c) verziók a forrás könyvtárak halmazát tömörítették<br>
és mentették. Mindíg az összes könyvtárat. Ez egyre hosszabb ideig tart, ahogy<br>
növekszik a könyvtárak száma és mérete. Ez a aprobléma. Az lenne jó, ha egy teljes<br>
mentés után csak a változásokat mentenénk. Ennek egy régi és elegáns módja, ha a<br>
tömörítő a file-ok archív bitjét figyeli és mentéskör törli, ugyanis a Windows<br>
a file-ok módosításakor az archív bitet érvényesre állítja.

## Megoldás

### Tömörítő

7z.exe<br>
Önmagában nem jó mert nem kezeli a forrás file-ok archive bit-jét.

A Windows XCOPY és a 7z.exe kombinálásával megoldható a probléma.

1. Teljes mentés .../00000000_000000_0/...

2. Változások mentése .../ééééhhnn_ooppmm_1/...

...

#### Tömörítés
7z.exe 

## Verzió
01d

## Fejlesztő
zavorszky@yahoo.com
