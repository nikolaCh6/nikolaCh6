<?php

$pages = array(
    'witam' => 'Witamy',
    'baza' => 'Baza',
    'formularz' => 'Formularz',
    'login' => 'Logowanie'
);

function get_menu($id) {
    global $pages;
    foreach ($pages as $p => $t) {
        echo '
            <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="?id='.$p.'">'.$t.'</a>
            </li>';
    }
}

function get_page_content($id) {
    if (file_exists($id.'.html'))
        include($id.'.html');
    else
        echo '<p>Brak takiej strony!</p>';
}

function get_koms() {
    global $kom;
    // foreach ($tb as $k) echo '<p>'.$k.'</p>';
    foreach ($kom as $k) echo '<p class="lead">'.$k.'</p>';
}

function clrtxt(&$el, $maxdl=30) {
    if (is_array($el)) {
        return array_map('clrtxt', $el);
    } else {
        $el = trim($el);
        $el = substr($el, 0, $maxdl);
        if (get_magic_quotes_gpc()) $el = stripslashes($el);
        $el = htmlspecialchars($el, ENT_QUOTES);
        return $el;
    }
}

?>
