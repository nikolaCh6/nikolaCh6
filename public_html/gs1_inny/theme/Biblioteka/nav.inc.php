<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); }?>
  <!-- Nagłówek strony: menu, logo, breadcrumbs itp. -->
  <div class="container-fluid pr-0 pl-0">
    <nav class="navbar fixed-top navbar-expand-xl navbar-dark bg-dark mx-auto">

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="fas fa-university fa-2x"></i>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mx-auto">
            <?php // print_r(return_i18n_menu_data(return_page_slug(), 0, 0, I18N_SHOW_NORMAL)); ?>
            <?php get_i18n_navigation(return_page_slug(), 0, 0, I18N_SHOW_NORMAL, $component='bs_menu'); ?>
          </ul>

          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-danger my-2 my-sm-0 rounded" type="submit">Search</button>
          </form>
        </div>
    </nav>
  </div>