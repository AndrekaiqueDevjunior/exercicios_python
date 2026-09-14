#Requires AutoHotkey v2.0
#SingleInstance Force

global strumScheduled := false

AutoStrum() {
    global strumScheduled

    if !strumScheduled {
        strumScheduled := true
        SetTimer StrumNow, -12
    }
}

StrumNow() {
    global strumScheduled

    Send "{Space down}"
    Sleep 5
    Send "{Space up}"

    strumScheduled := false
}


; VERDE
$a::{
    Send "{1 down}"
    AutoStrum()
}

$a up::{
    Send "{1 up}"
}


; VERMELHO
$s::{
    Send "{2 down}"
    AutoStrum()
}

$s up::{
    Send "{2 up}"
}


; AMARELO
$d::{
    Send "{3 down}"
    AutoStrum()
}

$d up::{
    Send "{3 up}"
}


; AZUL
$f::{
    Send "{4 down}"
    AutoStrum()
}

$f up::{
    Send "{4 up}"
}


; LARANJA
$g::{
    Send "{5 down}"
    AutoStrum()
}

$g up::{
    Send "{5 up}"
}