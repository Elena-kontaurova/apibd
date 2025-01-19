function updateComment() {
    const form = document.getElementById('comForm');
    const comId = form.id.value;
    console.log('Comment Id', comId);
    if (!comId) {
        alert('Пожалуйста, введите ID');
        return;
    }
    const data = {
        news: form.news.value,
        author: form.author.value,
        content: form.content.value,
        data: form.data.value
    };
    fetch(`http://127.0.0.1:8000/comment/${comId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при обновлении данных');
            }
            return response.json();
        })
        .then(data => {
            alert('Данные успешно обновлены')
        })
        .catch((error) => {
            console.error('Произошла ошибка:', error);
            alert('Не удалось обновить данные');
        });
}

function comDel() {
    const form = document.getElementById('coForm')
    const coId = form.id.value
    fetch(`http://127.0.0.1:8000/del_comment/${coId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            return response.json
        })
        .then(data => {
            alert('Запись успешно удалена')
        })
}