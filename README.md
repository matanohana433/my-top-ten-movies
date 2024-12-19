# 🎥 My Top Ten Movies

## 🌟 Overview

The **My Top Ten Movies** application is a Flask-based web application that allows users to manage their personal movie database. Users can add movies using The Movie Database (TMDb) API, rate and review their favorite movies, and delete entries. The app dynamically ranks movies based on user ratings.

---

## 🛠 Features
* **Movie Management**: Add, rate, review, and delete movies.
* **Dynamic Ranking**: Automatically ranks movies based on user ratings.
* **Search Integration**: Uses TMDb API to search and add movies.
* **Responsive Design**: Leverages Flask-Bootstrap and custom styles for a user-friendly interface.

---

## 📂 Project Structure

    .
    ├── app.py                 # Main Flask application
    ├── templates/             # HTML templates
    │   ├── base.html          # Base layout template
    │   ├── index.html         # Homepage displaying all movies
    │   ├── add.html           # Form to add movies
    │   ├── edit.html          # Form to rate and review movies
    │   ├── select.html        # List of search results from TMDb
    ├── static/                # Static assets (CSS, images)
    │   ├── styles.css         # Custom CSS for styling
    ├── requirements.txt       # Project dependencies
    ├── README.md              # Project documentation

---

## 🔧 Setup Guide

**Prerequisites**
* Python 3.x installed.
* TMDb API key and access token.

**Installation**

1. Clone this repository:

    
    git clone https://github.com/matanohana433/my-top-ten-movies.git
    cd my-top-ten-movies
    

2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    
    python -m venv venv
    venv\Scripts\activate
    

**macOS/Linux:**

    
    python3 -m venv venv
    source venv/bin/activate
    

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

   * Create a `.env` file or set variables manually:

    ```plaintext
    API_KEY=your_tmdb_api_key
    ACCESS_TOKEN=your_tmdb_access_token
    ```

5. Initialize the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

*Note: SQLAlchemy is used for database interactions, with migrations managed by Flask-Migrate. By default, the app connects to a local SQLite database, but it can be configured for other databases (e.g., PostgreSQL, MySQL) by modifying the `SQLALCHEMY_DATABASE_URI` in the `app.config`.*

---

## 🚀 Usage

1. **Run the Application**:

    
    python app.py
    

2. **Home Page**:

   - Displays all movies in the database, ranked by ratings.

3. **Add Movies**:

   - Search for movies using the **Add Movie** button.
   - Select the desired movie from TMDb search results.

4. **Rate & Review**:

   - Click **Edit** on a movie to add a rating and review.

5. **Delete Movies**:

   - Remove unwanted movies using the **Delete** button.

---

## 🌟 Key Features

1. **SQLAlchemy ORM**:
   * Abstracts database interactions for efficient and scalable operations.

2. **TMDb Integration**:
   * Fetch movie details like title, release year, description, and poster.

3. **User Ratings & Reviews**:
   * Rate movies out of 10 and add personalized reviews.

4. **Dynamic Rankings**:
   * Automatically updates movie rankings based on ratings.

5. **Custom Styling**:
   * Styled using `styles.css` for a polished, responsive UI.

---

## 🚀 Future Enhancements

1. Add user authentication for personalized movie collections.
2. Implement pagination for large movie databases.
3. Introduce genre-based filtering and sorting options.

---

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** [matanohana433](https://github.com/matanohana433)

---

