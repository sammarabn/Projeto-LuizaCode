(function (win, doc) {
    'use strict';

    //Verifica se quer mesmo deletar a loja
    if (doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for (let i = 0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function (event) {
                if (confirm('Deseja mesmo apagar esta loja e todos os seus dados?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }

    if (doc.querySelector('.btnDelProd')) {
        let btnDelProd = doc.querySelectorAll('.btnDelProd');
        for (let i = 0; i < btnDelProd.length; i++) {
            btnDelProd[i].addEventListener('click', function (event) {
                if (confirm('Deseja mesmo apagar este produto e todos os seus dados?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }

    if (doc.querySelector('.btnDelCateg')) {
        let btnDelCateg = doc.querySelectorAll('.btnDelCateg');
        for (let i = 0; i < btnDelCateg.length; i++) {
            btnDelCateg[i].addEventListener('click', function (event) {
                if (confirm('Deseja mesmo apagar esta categoria e todos os seus dados?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }
})(window, document);