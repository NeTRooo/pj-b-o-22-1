function open_burger(x){
    if (x=='burger'){
        if (document.getElementById(x).classList.contains('burger_hidden')){
            document.getElementById(x).classList.remove('burger_hidden');
            document.getElementById('open1').classList.add('open-svg');
            // document.getElementById('open1').src="/static/main_page/img/open_after.png";
        }
        else{
            document.getElementById(x).classList.add('burger_hidden');
            document.getElementById('open1').classList.remove('open-svg');
            // document.getElementById('open1').src="/static/main_page/img/open.png";
        }
    }
};