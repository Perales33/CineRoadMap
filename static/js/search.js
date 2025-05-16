$(document).ready(function() 
{
    // Maneja el evento de entrada en el campo de búsqueda
    $('#search').on('input', function() 
    {
        let query = $(this).val(); // Obtiene el valor del campo de búsqueda
        
        // Realiza una solicitud GET al servidor para buscar recetas
        $.getJSON('/search', { query: query }, function(data) 
        {
            let list = $('#movie-list'); // Selecciona el elemento de la lista de recetas
            list.empty(); // Vacía la lista antes de llenarla con los resultados de la búsqueda

            // Verifica si hay resultados en la respuesta del servidor
            if (data.length) 
                {
                // Recorre cada receta en los resultados y añade un ítem a la lista
                data.forEach(movie => 
                    {
                    list.append(`<li class="list-group-item">
                        <a href="/movie/${movie.title}">
                            <h5>${movie.title}</h5>
                        </a>
                    </li>`);
                });
            } else {
                // Si no hay resultados, muestra un mensaje de "No se encontraron recetas"
                list.append('<li class="list-group-item">No se encontraron películas</li>');
            }
        });
    });
});

