function validarFecha() {
    var fechaForm = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    ///////////////////////////////////////
    var ano = fechaForm.slice(0, 4);
    var mes = fechaForm.slice(5, 7);
    var dia = fechaForm.slice(8, 10);
    ///////////////////////////////////////
    var fechaMia = new Date(ano, (mes - 1), dia);
    ///////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("Fecha de nacimiento incorrecto");
        return false;
    }



    return true;
}

function validarNombre() {
    var nom = document.getElementById("txtNombre").value;
    var largo = nom.trim().length;
    if (largo >= 3 && largo <= 80) {
        return true;
    } else {
        
        return false;
    }
}

function validarApellido() {
    var nom = document.getElementById("txtApellido").value;
    var largo = nom.trim().length;
    if (largo >= 3 && largo <= 80) {
        return true;
    } else {
        return false;
    }
}

function validarNombreP() {
    var nom = document.getElementById("txtNombre").value;
    var largo = nom.trim().length;
    if (largo >= 3 && largo <= 120) {
        return true;
    } else {
        
        return false;

    }
}

function descripcion() {
    var des = document.getElementById("txtDescripcion").value;
    var largo = des.trim().length;
    if (des != "") {
        if (largo >= 3 && largo <= 200) {
            return true;
        } else {
            return false;
        }
    } else {
        true
    }
}


function validarTodo() {
    var resp;
    resp = validarNombre();
    if (resp == false) {
        alert("el nombre debe tener entre 3 a 80 caracteres")
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        return false;
    }

}

//menu
var li = document.getElementById('li');
document.getElementById('menu').addEventListener('click', function () {
    li.classList.toggle("menudos")
})

var glide = new Glide('#cli', {
    type: 'carousel',
    perView: 3,
    focusAt: 'center',

    breakpoints: {
        972: {
            perView: 2
        },
        600: {
            perView: 1
        }
    }
})

glide.mount()