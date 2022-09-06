function hw_date(date, actual){
    var el = document.getElementById('right_bottom'),
        classList = 'classList' in el;
    for (var i = 0; i < el.children.length; i++) {
        var child = el.children[i];
        if (child.tagName == 'DIV') {
            if (classList) {
                child.classList.add('hidden');
            } else {
                child.className += ' hidden'
            }
        }
    }
    document.getElementById(actual).classList.remove('hidden');
};