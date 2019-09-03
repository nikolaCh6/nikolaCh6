<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); }?>

<?php include("header.inc.php"); ?>

<body id="<?php get_page_slug(); ?>">

  <!-- brak java scriptu -->
  <noscript>
    Do pełnej funkcjonalności strony potrzebujesz włączonej obsługi skryptów.
    Tu znajdziesz <a href="https://www.enable-javascript.com/pl/" target="_blank">
    instrukcje, które pozwolą Ci włączyć skrypty w Twojej przeglądarce</a>.
  </noscript>

  <?php include("nav.inc.php"); ?>

  <script>
    var $buoop = {notify:{e:-6,f:-4,o:-4,s:-2,c:-4},insecure:true,api:5};
    function $buo_f(){
      var e = document.createElement("script");
      e.src = "http://browser-update.org/update.min.js";
      document.body.appendChild(e);
    };
    try {document.addEventListener("DOMContentLoaded", $buo_f,false)}
    catch(e){window.attachEvent("onload", $buo_f)}
  </script>

  <!-- Treść główna -->

  <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel" style="margin-top: 100px;">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="w-100" src="<?php get_theme_url(); ?>/img/banner.png" alt="First slide">
      </div>

      <div class="carousel-item">
        <img class="w-100" src="<?php get_theme_url(); ?>/img/banner2.jpg" alt="Second slide">
      </div>

    </div>
  </div>

  <div class="container mt-4 mb-4">
    <div class="row">
      <div class="col-12">
        <h1><?php get_page_title(); ?></h1>
      </div>

    <div class="col-10">
    	<?php get_page_content(); ?>
		</div>

      <div class="col-8" style="background-color: rgb(68, 68, 68); color: white;">
        <h2>Do korzystania z Wypożyczalni i Czytelni Szkolnej zapraszamy codziennie w godzinach:</h2>
        <ol type="1">
          <li>poniedziałek - 7:30 - 14:30</li>
          <li>wtorek -  7:30 - 14:30</li>
          <li>środa - 7:30 - 14:30</li>
          <li>czwartek - 7:30 - 14:30</li>
          <li>piątek - 7:30 - 14:00</li>
        </ol>
      </div>

      <div class="col-4 text-danger">
        <h3>Gorąco polecamy:</h3>
        <ul>
          <li><a href="">Spotkania z Poezją</a></li>
          <li><a href="">Różne barwy poezji</a></li>
          <li><a href="http://confraternitas.pl/images/skura/">Wiersze Józefa Skury</a></li>
          <li><a href="http://lo1.sandomierz.pl">LO I Collegium Gostomianum</a></li>
          <li><a href="">Confraternitas Gostomianum</a></li>
          <li><a href="">Collegium w obiektywie</a></li>
          <li><a href="http://literat.ug.edu.pl/books.htm">Wirtualna biblioteka</a></li>
          <li><a href="">Nasi Darczyńcy</a></li>
          <li><a href="">Czytając</a></li>
          <li><a href="">Spójnia</a></li>
          <li><a href="http://biblioteki-szkolne.blogspot.com">Biblioteki Szkolne Online</a></li>
          <li><a href="">Biuletyn Informacyjny Żołnierzy AK</a></li>
        </ul>
      </div>
    </div>
  </div>

<?php include("footer.inc.php"); ?>

  <!-- jQuery library -->
  <script src="<?php get_theme_url(); ?>/js/jquery-3.3.1.min.js"></script>
  <!-- Bootstrap JavaScript and Popper JS (https://popper.js.org) -->
  <script src="<?php get_theme_url(); ?>/js/bootstrap.bundle.min.js"></script>
  <!-- MDB core JavaScript -->
  <script type="text/javascript" src="<?php get_theme_url(); ?>/js/mdb.min.js"></script>

  <!-- Szybkość karuzeli -->
  <script type="text/javascript">
    $('.carousel').carousel({
      interval: 4000
    })
  </script>

</body>
</html>