document.addEventListener("DOMContentLoaded", () => {
    fetchPosts();
});

async function fetchPosts() {
    const container = document.getElementById("posts-container");
    
    try {
        // Docelowo: fetch('http://localhost:8000/api/posts')
        // Na razie pokazuję przykładowe posty, gdyby API było wyłączone
        const mockData = [
            { id: 1, title: "Testowy Wykop - Zrobiony przez AI!", author: "koxum", votes: 42 },
            { id: 2, title: "Gdzie są moje plusy?", author: "Maniek", votes: 12 }
        ];

        // Wyczyszczenie napisu "Ładowanie wpisów..."
        container.innerHTML = "";

        mockData.forEach(post => {
            const postHTML = `
                <article class="post">
                    <div class="vote-section">
                        <button class="btn-vote">▲</button>
                        <span class="vote-count">${post.votes}</span>
                        <button class="btn-vote">▼</button>
                    </div>
                    <div class="post-content">
                        <h3>${post.title}</h3>
                        <div class="post-meta">
                            Dodane przez <span class="author">@${post.author}</span> • przed chwilą
                        </div>
                    </div>
                </article>
            `;
            container.insertAdjacentHTML('beforeend', postHTML);
        });

    } catch (error) {
        container.innerHTML = "<p>Błąd ładowania wpisów z serwera.</p>";
        console.error("Błąd:", error);
    }
}
