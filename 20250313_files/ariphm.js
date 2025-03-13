/* Позволяет создать случайное число в заданном интервале */
function randint(a, b) {
    return a + Math.round(
        Math.random() * (b - a)
    );
}

function create_question(max_num) {
    let a = randint(1, max_num);
    let b = randint(1, max_num);
    return {
        q: a + ' + ' + b,
        a: a + b
    };
}

var result = '';

function save(filename, data) {
    const blob = new Blob([data], {type: 'text/csv'});
    if(window.navigator.msSaveOrOpenBlob) {
        console.log('я тут');
        window.navigator.msSaveBlob(blob, filename);
    } else {
        const elem = document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = filename;
        elem.innerHTML = 'Meeew!'; 
        document.body.appendChild(elem);
        elem.click();        
        //document.body.removeChild(elem);
    }
}


function save_all() {
    save('result.txt', result)
}

var max_q = 10;

function ask(max_num) {
    max_q -= 1;
    console.log(max_q);
    if (max_q == 0) return;
    let t = create_question(max_num);
    let label = document.createElement('label');
    label.textContent = t.q;
    result += t.q + ' = ';
    document.body.appendChild(label);
    let inp = document.createElement('input');
    document.body.appendChild(inp);
    inp.addEventListener(
        'keyup',
        (event) => {
            if (event.key === 'Enter' || event.keyCode === 13) {
                event.target.disabled = true;
                result += event.target.value + '\n';
                //event.target.setAttribute('disabled', 'disabled');
                ask(max_num);
            }
        }
    );
    inp.focus();
}

function exam() {
    let max_num = 10;
    let res = '';
    //while (max_q > 0) {
        ask(max_num);
        //max_q --;
    //}
}

window.addEventListener(
    'load',
    exam
);