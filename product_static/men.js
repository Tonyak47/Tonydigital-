const hamburger = document.getElementById('hamburger');

const navMenu = document.getElementById('navMenu');

hamburger .addEventListener('click', () => { navMenu.classList.toggle('open');});

const roles = ["Graphic Designer", "Web Designer", "Web Developer", "Gamer", "Student"];
const keyframeText = document.querySelector('.keyframe-text');

let roleIndex = 0;
function typeEffect() {
    const currentText = roles[roleIndex];
    let charIndex = 0;

    function typeChar() {
        if (charIndex < currentText.length) {
            keyframeText.textContent += currentText[charIndex];
            charIndex++;
            setTimeout(typeChar, 500); // Speed of typing
        } else {
            setTimeout(() => deleteEffect(currentText), 3000); // Wait before deleting
        }
    }

    typeChar();
}

function deleteEffect(text) {
    let charIndex = text.length;

    function deleteChar() {
        if (charIndex > 0) {
            keyframeText.textContent = text.substring(0, charIndex - 1);
            charIndex--;
            setTimeout(deleteChar, 100); // Speed of deleting
        } else {
            roleIndex = (roleIndex + 1) % roles.length;
            setTimeout(typeEffect, 500); // Wait before typing the next role
        }
    }

    deleteChar();
}

typeEffect(); // Start the typing effect

