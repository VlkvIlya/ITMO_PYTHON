function updateImportant(el) {
    let noteDiv = el.parentElement.querySelector('div:first-child')
    if (el.checked) {
        noteDiv.classList.add('important-note')
    } else {
        noteDiv.classList.remove('important-note')
    }

    fetch('/important/' + el.value, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'important': el.checked})
    })
}


function addNote() {
    let noteName = document.getElementById('note_name').value
    if (!noteName.trim()) return
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'note_name': noteName, 'important': false})
    }).then(() => {
        location.reload()
    })
}


function clearNotes() {
    fetch('/clear', {
        method: 'delete'
    }).then(() => {
        location.reload()
    })
}