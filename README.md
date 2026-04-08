\# ✦ StellarAI



A machine learning web application that classifies cosmic objects — Stars, Galaxies, and Quasars —  

using real telescope data from NASA's Sloan Digital Sky Survey (SDSS DR17).



Built with Python, scikit-learn, and Django



\---



\## 💡 About the Project



Astronomers use telescopes to capture light readings from millions of cosmic objects. Classifying  

what each object actually is — a star, a distant galaxy, or a quasar — is a classic problem  

in astrophysics that machine learning handles extremely well.



StellarAI takes the 8 key measurements captured by a telescope and predicts the class of the  

object in real time using a trained RandomForestClassifier model with \~98% accuracy.



\---



\## ⚙️ Tech Stack



| Layer        | Technology                            |

|--------------|---------------------------------------|

| ML Model     | scikit-learn (RandomForestClassifier) |

| Backend      | Python, Django                        |

| Data         | NASA SDSS DR17 (Kaggle, 100K rows)    |

| Frontend     | HTML, Bootstrap 5, Space Grotesk font |

| Model Export | Joblib                                |

| Database     | SQLite (default, not actively used)   |



\---



\## 🔭 What It Classifies



| Class      | Description                                                                 |

|------------|-----------------------------------------------------------------------------|

| ⭐ STAR    | Hot plasma balls powered by nuclear fusion; very low redshift               |

| 🌌 GALAXY  | Massive systems of billions of stars; moderate redshift                     |

| 💫 QUASAR  | Supermassive black hole-powered objects; extremely high redshift (QSO)      |



\---



\## 🧠 Input Features



The model uses 8 features derived from SDSS telescope observations:



| Feature    | Description                                              |

|------------|----------------------------------------------------------|

| `alpha`    | Right Ascension angle (sky coordinate)                   |

| `delta`    | Declination angle (sky coordinate)                       |

| `u`        | Ultraviolet filter brightness                            |

| `g`        | Green filter brightness                                  |

| `r`        | Red filter brightness                                    |

| `i`        | Near-infrared filter brightness                          |

| `z`        | Infrared filter brightness                               |

| `redshift` | How fast the object is moving away from Earth (key feature) |



\---



\## 🗂️ Project Structure



\---



\## 🚀 Running Locally



```bash

\# Clone the repo

git clone https://github.com/DevjeetMandal/stellarai.git

cd stellarai



\# Install dependencies

pip install django scikit-learn numpy joblib



\# Place your trained model file

\# → Put StellarModel.joblib inside the ml\_model/ folder



\# Apply migrations

python manage.py migrate



\# Start the server

python manage.py runserver

```



Then open `http://127.0.0.1:8000/` in your browser.



\---



\## 🔁 How It Works



1\. User enters 8 telescope readings on the Classifier page

2\. The view validates all inputs and builds a NumPy feature array

3\. The pre-trained `StellarModel.joblib` model runs `predict()` on the array

4\. The numeric output (0, 1, 2) is mapped to GALAXY, QSO, or STAR

5\. The result is rendered back on the same page



\---



\## 📊 Model Info



\- \*\*Dataset:\*\* SDSS DR17 via Kaggle — 100,000 real cosmic observations  

\- \*\*Algorithm:\*\* RandomForestClassifier (scikit-learn)  

\- \*\*Accuracy:\*\* \~98% on test set  

\- \*\*Model file:\*\* Exported with `joblib` as `StellarModel.joblib`



\---



\## 👤 Author



\*\*Devjeet Mandal\*\*  

IMCA Final Year   

\[GitHub](https://github.com/DevjeetMandal) • \[LinkedIn](www.linkedin.com/in/devjeetmandal76577)

