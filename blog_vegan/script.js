document.addEventListener('DOMContentLoaded', () => {
  fetch('posts.json')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('post-container');
      container.innerHTML = '';

      data.forEach(post => {
        const article = document.createElement('article');
        article.className = `post-card ${post.categoria}`;

        article.innerHTML = `
          <a href="${post.link}">
            <img src="${post.imagem}" alt="${post.titulo}" class="post-image" />
          </a>
          <div class="post-content">
            <h2><a href="${post.link}">${post.titulo}</a></h2>
            <p>${post.descricao}</p>
          </div>
        `;

        container.appendChild(article);
      });
    });
});

function filterPosts(category) {
  const posts = document.querySelectorAll('.post-card');
  posts.forEach(post => {
    if (category === 'all' || post.classList.contains(category)) {
      post.style.display = 'block';
    } else {
      post.style.display = 'none';
    }
  });
}
