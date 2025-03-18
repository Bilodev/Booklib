# Booklib
Questo progetto ha lo scopo di facilitare l'organizzazione della lettura fornendo la possibilità di salvare una lista di libri che l'utente ha letto, sta leggendo o ha intenzione di leggere in futuro; tutto questo con la possibilità di avere due modalità di visualizzazione una minimale e una completa con immagini.
## Panoramica Applicazione

### Minimal View

#### Home Page 
![Booklib Home](booklib_home_minimal.png)

#### Ricerca (Home Page) 
![Booklib Research](book_search_minimal.png)

### Complete View

#### Home Page 
![Booklib Home](booklib_home_complete.png)

#### Ricerca (Home Page)
![Booklib Research](book_search_complete.png)

### Visualizzazione di un libro
![Book Focus](book_focus.png)

### Riconoscimento Utente
<center>

![Signup](signup.png)
<br>

![Login](login.png)
</center>


## Tecnologie Utilizzate

<center> <h2> Backend </h2> </center>
<div style="text-align: center;">
    <img src="https://www.svgrepo.com/show/376344/python.svg" alt="Python" style="width:200px; display:inline-block; margin: 10px;"/> 
    <img src="https://logowik.com/content/uploads/images/mysql8604.logowik.com.webp" alt="MySQL" style="width:180px; height: 140px;display:inline-block; margin: 10px;"/> 
    <img src="https://logowik.com/content/uploads/images/google-play-books.jpg" alt="Google Play Books" style="width:200px; display:inline-block; margin: 10px;"/>
    <img src="https://icon.icepanel.io/Technology/png-shadow-512/Flask.png" alt="Flask" style="width:140px; display:inline-block; margin: 10px;"/>
</div>
<br>

**Python** è il linguaggio di programmazione scelto per il backend grazie alla sua semplicità e versatilità. Permette di sviluppare rapidamente funzionalità robuste e scalabili.

**MySQL** è un sistema di gestione di database relazionali utilizzato per memorizzare le informazioni sui libri. È affidabile e performante, ideale per gestire grandi quantità di dati.

**L'API di Google Books** viene utilizzata per recuperare informazioni dettagliate sui libri, come la copertina, l'autore, e la descrizione, migliorando così l'esperienza dell'utente.

**Flask** è un micro-framework web per Python. È leggero e modulare, permettendo agli sviluppatori di scegliere le componenti da integrare. Perfetto per creare applicazioni web rapide e performanti.

<center> <h2> Frontend </h2> </center>
<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Vitejs-logo.svg" alt="Vite" style="width:100px; height: 120px; display:inline-block; margin: 10px;"/> 
    <img src="https://logosandtypes.com/wp-content/uploads/2020/11/svelte.svg" alt="Svelte" style="width:200px; height: 120px; display:inline-block; margin: 10px;"/> 
</div>
<br>

**Vite** è un tool di build di nuova generazione che offre un ambiente di sviluppo rapido e snello. Permette di sviluppare applicazioni web moderne con una configurazione minima.

**Svelte** è un framework JavaScript per la creazione di interfacce utente. A differenza di altri framework, Svelte compila il codice in JavaScript altamente ottimizzato durante la build, migliorando le prestazioni runtime.

<center> <h2> System </h2> </center>
<div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Bash_Logo_Colored.svg" alt="Bash" style="width:200px; height: 120px; display:inline-block; margin: 10px;"/> 
</div>
<br>

**Bash** è una shell Unix e un linguaggio di scripting che consente di automatizzare diverse operazioni di sistema. Viene utilizzato per gestire script di deploy e automazione delle operazioni server-side.

## Schema del database
![](users_table.png)
![](books_table.png)

## Flusso di Lavoro
<center>

### Avvio
<img src="start.png" alt="Signup" style="width:700px; height: 400px; display:inline-block;"/> 

L'utente per utilizzare l'applicazione esegue un file con estensione .bash che avvia, automaticamente, l'applicazione nella sua interezza e apre una finestra nel browser per la visualizzazione delle pagine 

### Signup
<img src="signup_stream.png" alt="signup" style="width:700px; height: 350px; display:inline-block; margin: 10px;"/> 

### Login
<img src="login_stream.png" alt="login" style="width: 700px; height: 350px; display:inline-block; margin: 10px;"/> 

### Home Page
<img src="home_stream.png" alt="home" style="width:700px; height: 350px; display:inline-block; margin: 10px;"/> 

### Ricerca (in home page)
<img src="search_stream.png" alt="search" style="width:700px; height: 300px; display:inline-block; margin: 10px;"/> 

### Pagina Libro Singolo
<img src="book_page_stream.png" alt="book_page" style="width:700px; height: 300px; display:inline-block; margin: 10px;"/> 

### Aggiunta o Rimozione di un Libro alla Lista 
<img src="add_remove_stream.png" alt="add_remove" style="width:700px; height: 150px; display:inline-block; margin: 10px;"/> 

### Modifica Stato di un Libro
<img src="update_stream.png" alt="update" style="width:700px; height: 150px; display:inline-block; margin: 10px;"/> 
</center>

## Altre Informazioni

![Tree](tree.png)
[Zip Del Progetto](https://drive.google.com/file/d/1M6sZ6NiGEbhuaiqp1JWpYVrFQJNUfYZW/view?usp=sharing)