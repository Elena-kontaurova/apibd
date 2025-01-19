function updateNews() {
    const form = document.getElementById('neForm');
    const newId = form.id.value;
    console.log('New Id', newId);
    if (!newId) {
        alert('Пожалуйста, введите ID пользователя')
        return;
    }
    const data = {
        heading: form.heading.value,
        content: form.content.value,
        author: form.author.value,
        data: form.data.value
    };

    fetch(`http://127.0.0.1:8000/news/${newId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при обновлении данных');
            }
            return response.json();
        })
        .then(data => {
            alert('Данные успешно обновлены');
        })
        .catch((error) => {
            console.error('Произошка ошибка:', error);
            alert('Не удалось обновить данные')
        });
}

function newDel() {
    const form = document.getElementById('nForm')
    const nId = form.id.value
    fetch(`http://127.0.0.1:8000/del_news/${nId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            return response.json
        })
        .then(data => {
            alert('Записть успешно удалена')
        })
}