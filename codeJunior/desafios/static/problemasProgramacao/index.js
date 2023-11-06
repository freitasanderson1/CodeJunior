const textarea = document.querySelector('[name="codigo"]')
const editorEl = document.querySelector('.editor');
const editor = window.ace.edit(editorEl);
editor.setTheme(`ace/theme/dracula`);
editor.session.setMode(`ace/mode/python`);
editor.setFontSize(18)
editor.on('change', data => {
  console.log('edited result', data);
  textarea.value = (editor.getSession().getValue());
});

const formSubmeterDesafio = document.querySelector('#formSubmeterDesafio')
const containerLoadingButton = document.querySelector('#containerLoadingButton')

async function submeterDesafioAPI(url, formElement) {
  addLoad(containerLoadingButton)

  const crf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value

  const data = new URLSearchParams();
  for (const pair of new FormData(formElement)) {
      data.append(pair[0], pair[1]);
  }
  const response = await fetch(url, { 
    method: 'post',
    processData: false,
    headers: {
      "Conten-Type": "application/json",
      "X-CSRFToken": crf_token
    },
    body: data
  });
  const responseJson = await response.json()

  if (response.status === 500) {
    throw new Error(data)
  }

  setTimeout(() => {
    removeLoad(containerLoadingButton)
  }, 500)

}

function addLoad(element) {
  element.innerHTML = `
    <div class="containerCarregamento d-flex justify-content-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  `
}

formSubmeterDesafio.addEventListener('submit', (evt) => {
  evt.preventDefault()

  const problema = formSubmeterDesafio.elements.problema.value
  const pessoa = formSubmeterDesafio.elements.pessoa.value
  const codigo = formSubmeterDesafio.elements.codigo.value

  const url = new URL(formSubmeterDesafio.action)
  problema && url.searchParams.append('problema', problema)
  pessoa && url.searchParams.append('pessoa', pessoa)
  codigo && url.searchParams.append('codigo', codigo)

  submeterDesafioAPI(url, formSubmeterDesafio)
})