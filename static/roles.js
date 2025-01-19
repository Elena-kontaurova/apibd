function updateRoles() {
    const form = document.getElementById('rolForm');

    const rolId = form.id.value;
    console.log("Roles ID:", rolId);
    if (!rolId) {
        alert("Пожалуйста, введите ID");
        return;
    }

    const data = {
        name: form.name.value
    };

    fetch(`http://127.0.0.1:8000/roles/${rolId}`, {
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

function delRol() {
    const form = document.getElementById('roForm')
    const roId = form.id.value;
    fetch(`http://127.0.0.1:8000/del_roles/${roId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            alert('Запись успешно удалена')
        })
}