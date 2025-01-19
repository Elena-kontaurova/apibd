function updateUser() {
    const form = document.getElementById('userForm');

    const userId = form.id.value;
    console.log("User ID:", userId);
    if (!userId) {
        alert("Пожалуйста, введите ID пользователя");
        return;
    }

    const data = {
        role_id: parseInt(form.role_id.value),
        username: form.username.value,
        password: form.password.value
    };

    fetch(`http://127.0.0.1:8000/users/${userId}`, {
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
            alert('Данные успешно обновлены!');
        })
        .catch((error) => {
            console.error('Произошла ошибка:', error);
            alert('Не удалось обновить данные');
        });
}

function delUser() {
    const form = document.getElementById('usForm');
    const userId = form.id.value;
    fetch(`http://127.0.0.1:8000/del_users/${userId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            alert('Запись успешно удалена');
        })
}