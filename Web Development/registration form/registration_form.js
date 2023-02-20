const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const name = document.querySelector('input[name="name"]').value;
  const email = document.querySelector('input[name="email"]').value;
  const password = document.querySelector('input[name="password"]').value;
  console.log(`Name: ${name}, Email: ${email}, Password: ${password}`);
});
