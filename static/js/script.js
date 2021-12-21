const filterForm = document.getElementById('filter')
const filterInput = filterForm.querySelector('input')
const matchTable = document.getElementById('matches')

filterInput.addEventListener('input', async e => {
    let res = await fetch('/users/filter', {
        method : 'POST',
        body : new FormData(filterForm)
    })
    res = await res.json()
    matchTable.innerHTML = ''
    for(let user of res){
        const tr = document.createElement('tr')
        tr.innerHTML = `
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.created_at}</td>
            <td>${user.updated_at}</td>
            `
        matchTable.append(tr)
    }
})