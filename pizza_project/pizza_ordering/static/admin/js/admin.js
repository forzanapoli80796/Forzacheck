document.addEventListener("DOMContentLoaded", function () {
    const tableContainer = document.querySelector('.model-terminalinventory .results');

    if (tableContainer) {
        // Add event listener for keyboard arrow keys
        document.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowRight') {
                // Scroll table right
                tableContainer.scrollBy({ left: 50, behavior: 'smooth' });
            } else if (event.key === 'ArrowLeft') {
                // Scroll table left
                tableContainer.scrollBy({ left: -50, behavior: 'smooth' });
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const lunchShiftTable = document.querySelector('.model-kitchenlate .results');

    if (lunchShiftTable) {
        // Add event listener for keyboard arrow keys
        document.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowRight') {
                // Scroll table right
                lunchShiftTable.scrollBy({ left: 50, behavior: 'smooth' });
            } else if (event.key === 'ArrowLeft') {
                // Scroll table left
                lunchShiftTable.scrollBy({ left: -50, behavior: 'smooth' });
            }
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const lateShiftTable = document.querySelector('.model-kitchenlatetask .results');

    if (lateShiftTable) {
        // Add event listener for keyboard arrow keys
        document.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowRight') {
                // Scroll table right
                lateShiftTable.scrollBy({ left: 50, behavior: 'smooth' });
            } else if (event.key === 'ArrowLeft') {
                // Scroll table left
                lateShiftTable.scrollBy({ left: -50, behavior: 'smooth' });
            }
        });
    }
});
