$(document).ready(function() {
    // Maneja el evento de entrada en el campo de búsqueda
    $('#searchActors').on('input', function() {
        let query = $(this).val(); // Obtiene el valor del campo de búsqueda
        
        // Realiza una solicitud GET al servidor para buscar actores
        $.getJSON('/searchActors', { query: query }, function(data) {
            let list = $('#actor-list'); // Selecciona el elemento de la lista de actores
            list.empty(); // Vacía la lista antes de llenarla con los resultados de la búsqueda

            // Verifica si hay resultados en la respuesta del servidor
            if (data.length) {
                // Recorre cada actor en los resultados y añade un ítem a la lista
                data.forEach(actor => {
                    list.append(`<li class="list-group-item">
                        <a href="/actor/${actor.actor_name}">
                            <h5>${actor.actor_name}</h5> <!-- Nombre del actor -->
                        </a>
                    </li>`);
                });
            } else {
                // Si no hay resultados, muestra un mensaje de "No se encontraron actores"
                list.append('<li class="list-group-item">No se encontraron actores</li>');
            }
        });
    });
});
