function open_burger(x){
    if (x=='burger'){
        if (document.getElementById(x).classList.contains('burger_hidden')){
            document.getElementById(x).classList.remove('burger_hidden');
            // document.getElementById(x).classList.remove('burger_hidden');
            document.getElementById('open1').classList.add('open-svg');
        }
        else{
            document.getElementById(x).classList.add('burger_hidden');
            document.getElementById('open1').classList.remove('open-svg');
        }
    }
};