<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<nav class="navbar navbar-expand-md navbar-dark bg-dark">
  <a class="navbar-brand" href="<?php get_site_url(); ?>"><?php get_site_name(); ?></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsExampleDefault">
    <ul class="navbar-nav mx-auto">
      <?php //print_r(return_i18n_menu_data(return_page_slug(), 0, 0, I18N_SHOW_NORMAL)); ?>
      <?php get_i18n_navigation(return_page_slug(), 0, 1, I18N_SHOW_MENU, $component='bs_menu'); ?>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Szukaj" aria-label="Szukaj">
      <button class="btn btn-secondary my-2 my-sm-0" type="submit">Szukaj</button>
    </form>
  </div>
</nav>
