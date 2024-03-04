# Belajar-Analisis-Data-Dengan-Python
![](https://github.com/Nadblqss/Submission_Bangkit/blob/main/Dashboard/streamlit.png)

Anda dapat melihat dashboard saya melalui [link ini](https://submissionbangkit.streamlit.app/)

# Cara Menjalankan Dashboard pada personal Env
1. Salin repository
```
git clone https://github.com/Nadblqss/Submission_Bangkit.git
```
2. Seting env pada anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

```
3. Pindah direktori ke `submission_bangkit/dashboard`
```
cd 'submission_bangkit/dashboard'
```
4. Run streamlit
```
streamlit run dashboard.py
```