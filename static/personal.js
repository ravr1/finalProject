document.addEventListener('DOMContentLoaded', () => {
        
    // Change the color of the heading when dropdown changes
    document.querySelector('#color-change').onchange = function() {
        document.querySelector('#hello').style.color = this.value;
    };

});