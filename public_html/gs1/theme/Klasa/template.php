<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<?php include("header.inc.php"); ?>
<body id="<?php get_page_slug(); ?>">
<?php include("nav.inc.php"); ?>

<main role="main" class="container">
  <div class="row">
    <div class="col-sm-8">
      <h1><?php get_page_title(); ?></h1>
      <?php get_page_content(); ?>
    </div>
    <div class="col-sm-4">
      <?php get_component('sidebar'); ?>
    </div>
  </div>
</main><!-- /.container -->

<?php include("footer.inc.php"); ?>

	<script src="<?php get_theme_url(); ?>/js/jquery.min.js"></script>
	<script src="<?php get_theme_url(); ?>/js/popper.min.js"></script>
	<script src="<?php get_theme_url(); ?>/js/bootstrap.min.js"></script>
</body>
</html>
