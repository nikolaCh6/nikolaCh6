<h1>Rejestracja</h1>
<p>Przesłane dane:</p>
<<?php
  print_r($_GET)
  print_r($_POST)
 ?>

 <form name="formularz" id="formularz" method="GET" action="rejestracja.php">
   <table  class="table">
     <tr>
       <td>
         <label for="imie">Imię</label>
       </td>
       <td>
         <input type="text" name="imie" value="" placeholder="Imię">
       </td>
   </tr>
   <tr>
     <td>
       <label for="nazwisko">Nazwisko</label>
     </td>
     <td>
       <input type="text" name="nazwisko" value="" placeholder="Nazwisko">
     </td>
   </tr>
   <tr>
     <td colspan="2">
       <input type="password" name="haslo" value="">
     </td>
   </tr>
 </table>
   <br>

     <!--wybór jednokrotny -->
     <label for="gender">Wybierz płeć:</label><br>
     <input type="radio" name="gender" value="male" checked> Male<br>
     <input type="radio" name="gender" value="female"> Female<br>
     <input type="radio" name="gender" value="other"> Other<br>
     <input type="radio" name="gender" value="other"> Xxx<br>
     <br>

     <!--wielokrotny wybór -->
       <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
       <input type="checkbox" name="vehicle2" value="Car"> I have a car<br>

       <!--lista opcji (multiple)-->
       <select name="cars">
         <option value="1" selected="selected">Volvo</option>
         <option value="2">Saab</option>
         <option value="3">Fiat</option>
         <option value="4">Audi</option>
       </select>
       <br>
       <textarea name="komentarz" rows="4" cols="80"></textarea>
      <br>

     <input type="submit" name="zapisz" value="Zapisz">
     <input type="reset" name="reset" value="Reset">
   </form>
