// document.addEventListener('DOMContentLoaded', () => {
//     const input = document.getElementById('search-input');
//     const suggestionsContainer = document.getElementById('suggestions-container');
//     const searchButton = document.getElementById('search-button');

//     input.addEventListener('input', async () => {
//         const query = input.value;
//         if (query.length >= 3) { // Check if query length is 3 or more
//             searchButton.disabled = false; // Enable search button
//             try {
//                 const response = await fetch(`http://localhost:8000/search?query=${encodeURIComponent(query)}`);
//                 if (!response.ok) {
//                     console.error('Failed to fetch suggestions:', response.statusText);
//                     return;
//                 }
//                 const suggestions = await response.json();

//                 // Clear previous suggestions
//                 suggestionsContainer.innerHTML = '';

//                 if (suggestions.length === 0) {
//                     // Show nothing
//                     suggestionsContainer.style.display = 'none';
//                 } else {
//                     // Show only the top 4 suggestions
//                     suggestions.slice(0, 4).forEach(suggestion => {
//                         const div = document.createElement('div');
//                         div.className = 'suggestion-item';
//                         div.textContent = suggestion;
//                         div.addEventListener('click', () => {
//                             input.value = suggestion;
//                             suggestionsContainer.style.display = 'none';
//                         });
//                         suggestionsContainer.appendChild(div);
//                     });
//                     // Show suggestions container
//                     suggestionsContainer.style.display = 'block';
//                 }
//             } catch (error) {
//                 console.error('Error fetching suggestions:', error);
//             }
//         } else {
//             searchButton.disabled = true; // Disable search button
//             suggestionsContainer.style.display = 'none';
//         }
//     });
// });


document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('search-input');
    const suggestionsContainer = document.getElementById('suggestions-container');
    const searchButton = document.getElementById('search-button');

    input.addEventListener('input', async () => {
        const query = input.value;
        if (query.length >= 3) { // Check if query length is 3 or more
            searchButton.disabled = false; // Enable search button
            try {
                const response = await fetch(`http://localhost:8000/search?query=${encodeURIComponent(query)}`);
                if (!response.ok) {
                    console.error('Failed to fetch suggestions:', response.statusText);
                    return;
                }
                const suggestions = await response.json();

                // Clear previous suggestions
                suggestionsContainer.innerHTML = '';

                if (suggestions.length === 0) {
                    // Show nothing
                    suggestionsContainer.style.display = 'none';
                } else {
                    // Show only the top 4 suggestions
                    suggestions.slice(0, 4).forEach(suggestion => {
                        const div = document.createElement('div');
                        div.className = 'suggestion-item';
                        div.textContent = suggestion;
                        div.addEventListener('click', () => {
                            input.value = suggestion;
                            suggestionsContainer.style.display = 'none';
                        });
                        suggestionsContainer.appendChild(div);
                    });
                    // Show suggestions container
                    suggestionsContainer.style.display = 'block';
                }
            } catch (error) {
                console.error('Error fetching suggestions:', error);
            }
        } else {
            searchButton.disabled = true; // Disable search button
            suggestionsContainer.style.display = 'none';
        }
    });
});