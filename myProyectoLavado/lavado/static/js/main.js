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
//validaciones formulario de registro
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

function validarUsuario() {
    var usu = document.getElementById("txtUsuario").value;
    var largo = usu.trim().length;
    if (largo >= 8) {
        return true;
    } else {
        return false;
    }
}

function validarContraseña() {
    var con = document.getElementById("txtContraseña").value;
    var largo = con.trim().length;
    if (largo >= 8) {
        return true;
    } else {
        return false;
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
        alert("el apellido debe tener entre 3 a 80 caracteres")
        return false;
    }
    resp = validarUsuario();
    if (resp == false) {
        alert("el nombre de usuario debe tener como mínimo 8 caracteres")
        return false;
    }
    resp = validarContraseña();
    if (resp == false) {
        alert("La contraseña debe tener un mínimo de 8 caracteres")
        return false;
    }


}
//validaciones agregar producto

function validarNombreP() {
    var nom = document.getElementById("txtNombre").value;
    var largo = nom.trim().length;
    if (largo >= 3 && largo <= 120) {
        return true;
    } else {

        return false;
    }
}

function validarDescripcion() {
    var des = document.getElementById("txtDescripcion").value;
    var largo = des.trim().length;
    if (des != 0) {
        if (largo >= 3 && largo <= 200) {
            return true;
        } else {
            return false;
        }
    } else {
        true
    }
}

function validarProducto() {
    var resp;
    resp = validarNombreP();
    if (resp == false) {
        alert("el nombre debe tener entre 3 a 120 caracteres")
        return false;
    }
    resp = validarDescripcion();
    if (resp == false) {
        alert("si desea ingresar una descripción debe tener entre 3 a 200 caracteres")
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

glide.mount();