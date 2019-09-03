<?php
//$nazwa oznacza zmienną
// aray() zwraca tablicę
$pages = array(
    'witam' => 'Witamy',
    'baza' => 'Baza',
    'formularz' => 'Formularz',
    'login' => 'Zaloguj'
);

function get_menu($id) {
    blobal $pages;
    foreach ($pages as $p => $t) {
        echo'
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="?id='.$p.'">'.$t.'</a>
            </li>';
    }
}

function get_page_content($id) {
    if (file_exists($id.'.html'))
        include($id.'.html');
    else
        echo '<p>Brak strony!</p>'
}
?>
