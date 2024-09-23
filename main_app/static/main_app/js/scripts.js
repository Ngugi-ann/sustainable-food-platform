document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contactForm');
    const message = document.getElementById('message');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Simple form validation (checks if fields are empty)
        const name = form.querySelector('input[name="name"]');
        const email = form.querySelector('input[name="email"]');
        const messageField = form.querySelector('textarea[name="message"]');

        if (name.value.trim() === '' || email.value.trim() === '' || messageField.value.trim() === '') {
            message.textContent = "Please fill in all fields.";
            message.style.color = 'red';
            return;
        }

        // Display the thank-you message
        message.textContent = "Thank you for contacting us!";
        message.style.color = 'green';

        // Clear form fields after submission
        name.value = '';
        email.value = '';
        messageField.value = '';

        // Animate the thank-you message
        message.style.opacity = 1;
        setTimeout(function () {
            message.style.transition = 'opacity 2s';
            message.style.opacity = 0;
        }, 3000); // Fades out after 3 seconds
    });
});


