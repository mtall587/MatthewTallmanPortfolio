function loadImages(category) {
    fetch(`/get_images?category=${category}`)
        .then(response => response.json())
        .then(images => {
            const gallery = document.getElementById('image-gallery');
            gallery.innerHTML = '';
            images.forEach(image => {
                const img = document.createElement('img');
                img.src = image;
                gallery.appendChild(img);
            });
        })
        .catch(error => console.error('Error loading images:', error));
}
