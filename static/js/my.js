// function showAuthors(year) {
//     // Make an AJAX call to retrieve the authors for the selected year
//     $.ajax({
//       url: '/get_authors',
//       type: 'POST',
//       data: {year: year},
//       success: function(data) {
//         // Display the authors in the 'author-list' div
//         var authorList = document.getElementById('author-list');
//         authorList.innerHTML = '';
  
//         // Create a list of authors and add them to the 'author-list' div
//         var authors = JSON.parse(data);
//         var authorListHTML = '<ul>';
//         for (var i = 0; i < authors.length; i++) {
//           authorListHTML += '<li>' + authors[i] + '</li>';
//         }
//         authorListHTML += '</ul>';
//         authorList.innerHTML = authorListHTML;
//       }
//     });
//   }

  
// //   function showAuthors(year) {
// //     // Fetch the data from the JSON file
// //     fetch('authors_by_year.json')
// //       .then(response => response.json())
// //       .then(data => {
// //         // Find the data for the selected year
// //         const yearData = data.find(d => d.year === year);
// //         // Display the total number of authors for the selected year
// //         const authorCount = yearData ? yearData.num_authors : 0;
// //         document.getElementById('author-total').textContent = authorCount;
// //       })
// //       .catch(error => {
// //         console.error('Error fetching data:', error);
// //       });
// //   }

function showAuthors(year) {
  // make an HTTP GET request to the /articles route with the selected year as a query parameter
  fetch(`/articles?year=${year}`)
    .then(response => response.json())
    .then(data => {
      // clear the existing list of articles
      const articleList = document.querySelector('#articles');
      articleList.innerHTML = '';

      // add the new list of articles to the DOM
      data.titles.forEach(title => {
        const articleItem = document.createElement('li');
        articleItem.textContent = title;
        articleList.appendChild(articleItem);
      });
    });
}

window.onload = function() {
  var username = "{{ username }}"; // Replace with the actual username

  // Create the login button
  var loginButton = document.createElement("a");
  loginButton.className = "nav-link";
  loginButton.textContent = "Login";
  loginButton.href = "/login"; // Update with the appropriate login route in your Flask application

  // Replace the login link with the login button
  var loginLogout = document.getElementById("loginLogout");
  loginLogout.innerHTML = "";
  loginLogout.appendChild(loginButton);

  // Check if the username is available
  if (username) {
      // Create the username element
      var usernameElement = document.createElement("a");
      usernameElement.className = "nav-link";
      usernameElement.textContent = "User " + username;
     
      usernameElement.href = "#"; // Update with the appropriate URL or remove the href attribute

      // Create the logout button
      var logoutButton = document.createElement("a");
      logoutButton.className = "nav-link";
      logoutButton.textContent = "Logout";
      logoutButton.href = "/logout"; // Update with the appropriate logout route in your Flask application

      // Replace the login button with the username and logout button
      loginLogout.innerHTML = "";
      loginLogout.appendChild(usernameElement);
      loginLogout.appendChild(logoutButton);

      // Add click event listener to the logout button
      logoutButton.addEventListener("click", function(event) {
          event.preventDefault();
          // Clear any user session data or perform other logout tasks
      alert("Logout Successfully"+username)
     
          // Redirect to the main index page without preserving history
          window.location.replace("/login"); // Update with the appropriate URL of your main index page
      });
  }
};
 

document.addEventListener("DOMContentLoaded", function() {
  const flashMessage = "{{ get_flashed_messages()|join('|') }}";
  if (flashMessage) {
      alert(flashMessage);
  }
});
  
