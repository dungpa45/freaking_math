$(document).ready(function () {
    let context = { err: 0 };
    let diem = 0;

    const renderQuiz = () => {
        let rnum1 = Math.floor((Math.random() * 25) + 1);
        let rnum2 = Math.floor((Math.random() * 25) + 1);
        let op = getOperator();

        context.err = Math.floor(Math.random() * 5) + (-2);
        let err1 = [0, 10];
        let err2 = [0, 0.1];
        
        if ($('#level').attr('level') === 'EASY') {
            context.err = Math.floor(Math.random() * 5) + (-2);
        } else if ($('#level').attr('level') === 'NORMAL') {
            rnum1 = Math.floor((Math.random() * 50) - 25);
            rnum2 = Math.floor((Math.random() * 50) - 25);
            context.err = (op === '*') ? err1[Math.floor(Math.random() * err1.length)] : (op === '/') ? err2[Math.floor(Math.random() * err2.length)] : Math.floor(Math.random() * 5) + (-2);
        } else if ($('#level').attr('level') === 'HARD') {
            rnum1 = Math.floor((Math.random() * 200) - 100);
            rnum2 = Math.floor((Math.random() * 200) - 100);
            context.err = (op === '/') ? err2[Math.floor(Math.random() * err2.length)] : err1[Math.floor(Math.random() * err1.length)];
        }
        
        let result = evaluate(rnum1, rnum2, op) + context.err;

        $('#num1').text(rnum1);
        $('#num2').text(rnum2);
        $('#operator').text(op);
        $('#answer').text(result);
        $('#point').text(diem);
    }

    const getOperator = () => {
        let operators = ['+', '-', '*', '/'];
        return operators[Math.floor(Math.random() * operators.length)];
    }

    const evaluate = (a, b, op) => {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
        }
    }

    const startTimer = (duration, display) => {
        let timer = duration, seconds;
        let interval = setInterval(function () {
            seconds = parseInt(timer % 60, 10);
            display.text(seconds < 10 ? "0" + seconds : seconds);

            if (--timer < 0) {
                clearInterval(interval);
                $('#save_point').val(diem);
                $('#btn_submit').click();
            }
        }, 1000);
    }

    const countdown = () => {
        startTimer(10, $('#time'));
    }

    window.nextQuestion = (isTrue) => {
        if ((isTrue && context.err === 0) || (!isTrue && context.err !== 0)) {
            diem++;
            renderQuiz();
            countdown();
        } else {
            $('#save_point').val(diem);
            $('#btn_submit').click();
        }
    }

    renderQuiz();
    countdown();
});
