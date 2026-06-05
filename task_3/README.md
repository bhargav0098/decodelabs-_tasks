# AI Tech Stack Recommender

A Content-Based Filtering recommendation engine built to map user skills to ideal career paths and job roles. This project demonstrates core Artificial Intelligence pattern alignment without relying on collaborative user history data.

## Architecture: Input-Process-Output Model

1. **Ingestion**: Captures raw user skill inputs.
2. **Vector Mapping (TF-IDF)**: Transforms qualitative tech skills into numerical arrays within a shared vocabulary space. Uses Term Frequency-Inverse Document Frequency to appropriately weight highly specific tech skills over generic terms.
3. **Scoring (Cosine Similarity)**: Measures the mathematical angle between the user's preference vector and the job role vectors to determine alignment, ensuring the system is invariant to vector magnitude.
4. **Filtering**: Sorts and truncates the dataset to prevent choice overload, outputting a highly targeted Top-N list.

## Tech Stack

- **Language**: Python
- **Libraries**: Pandas (Data handling), Scikit-learn (TF-IDF Vectorizer, Cosine Similarity math)

## How to Run

1. Clone the repository.
2. Install dependencies: `pip install pandas scikit-learn`
3. Run the engine: `python recommender.py`
4. Input your current skills (e.g., "Python, Machine Learning, SQL") to receive your customized career vector match.

## Future Enhancements

- Implement fallback logic to handle the "User Cold Start" problem using onboarding surveys.
- Integrate with a full-stack dashboard (React/Node.js) for an interactive UI.

<img width="1021" height="411" alt="Screenshot 2026-06-06 003835" src="https://github.com/user-attachments/assets/2c595ce8-1c7d-4594-9517-a48b61d0d351" />
