function showCategory(category) {
    const portfolioGrid = document.getElementById('portfolio-grid');
    portfolioGrid.innerHTML = ''; // Clear the current grid

    for (let i = 1; i <= 25; i++) {
        const img = document.createElement('img');
        img.src = `images/${category}/image${i}.jpg`; // Adjust the image path and name as necessary
        img.alt = `Image ${i}`;
        portfolioGrid.appendChild(img);
    }
}

// Show the first category by default  32113
document.addEventListener('DOMContentLoaded', () => {
    showCategory('category1');
});
