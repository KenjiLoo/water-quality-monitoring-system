<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="with=device-width, initial-scale=1.0">
    <title>SEGP 9A_Monitor</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js"></script>
  </head>

  <body>
    <section class="sub-header">
    <nav>
        <a href="mainpage.html"> <img src="images/frontpagelogo.png"></a>
        <div class="nav-links" id="navLinks">
            <i class="fa fa-times" onclick="hideMenu()"></i>
            <ul>
                    <li><a href="mainpage.html">HOME</a></li>
                    <li><a href="intro.html">INTRODUCTION</a></li>
                    <li><a href="library.php">LIBRARY</a></li>
                    <li><a href="monitor.html">MONITOR</a></li>
                    <li><a href="index.php">LOGOUT</a></li>
                
            </ul>
        </div>
        <i class="fa fa-bars" onclick="showMenu()"></i>
      </nav>
      <h1>Results</h1>
    </section>

    <!-------- Monitor content------->
<?php
  /* Database connection settings */
  $host = 'localhost';
  $user = 'root';
  $pass = '';
  $db = 'hfyql1ju_csv_db_7';
  $mysqli = new mysqli($host,$user,$pass,$db) or die($mysqli->error);

  $interval_val = '';
  $diff_perentage = '';
  $considered_dirty = '';

  //query to get data from the table
  $sql = "SELECT * FROM `graph_info` ";
  $result = mysqli_query($mysqli, $sql);

  //loop through the returned data
  while ($row = mysqli_fetch_array($result)) {

    $interval_val = $interval_val . '"'. $row['interval_val'].'",';
    $diff_perentage = $diff_perentage . '"'. $row['diff_perentage'] .'",';
    $considered_dirty = $considered_dirty . '"'. $row['considered_dirty'] .'",';
  }

  $interval_val = trim($interval_val,",");
  $diff_perentage = trim($diff_perentage,",");
  $considered_dirty = trim($considered_dirty,",");
?>

  <style>     
      body{
        text-align: center;
      }

      .graph-container {
        margin: 25px 30px;
        color: #E8E9EB;
        background: #222;
        border: #555652 1px solid;
        padding: 20px;
      }
      
  </style>  

      <div class="graph-container">
      <div class="chartjs-size-monitor" style="position: absolute; inset: 0px; overflow: hidden; pointer-events: none; visibility: hidden; z-index: -1;"><div class="chartjs-size-monitor-expand" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;pointer-events:none;visibility:hidden;z-index:-1;"><div style="position:absolute;width:1000000px;height:1000000px;left:0;top:0"></div></div><div class="chartjs-size-monitor-shrink" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;pointer-events:none;visibility:hidden;z-index:-1;"><div style="position:absolute;width:200%;height:200%;left:0; top:0"></div></div></div>
      <h1>Water Quality Data</h1>       
      <canvas id="chart" style="width: 100%; height: 65vh; background: rgb(34, 34, 34); border: 1px solid rgb(85, 86, 82); margin-top: 10px; display: block;" width="1112" height="1924" class="chartjs-render-monitor"></canvas>

      <script>
        var ctx = document.getElementById("chart").getContext('2d');
          var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [0,10,20,30,40,50],
                datasets: 
                [{
                    label: 'Diff_Percentage',
                    data: [<?php echo $diff_perentage; ?>],
                    backgroundColor: 'transparent',
                    borderColor:'rgba(255,99,132)',
                    borderWidth: 3
                },

                {
                  label: 'Considered_Dirty',
                    data: [<?php echo $considered_dirty; ?>],
                    backgroundColor: 'transparent',
                    borderColor:'rgba(0,255,255)',
                    borderWidth: 3  
                }]
            },
         
            options: {
                scales: {scales:{yAxes: [{beginAtZero: false}], xAxes: [{autoskip: true, maxTicketsLimit: 20}]}},
                tooltips:{mode: 'index'},
                legend:{display: true, position: 'top', labels: {fontColor: 'rgb(255,255,255)', fontSize: 16}}
            }
        });
      </script>
      </div>  

    <!-----------Javascript for Toggle Menu------->
        <script>
          var navLinks = document.getElementById("navLinks");
          function showMenu(){
              navLinks.style.right = "0";
          }
          function hideMenu(){
              navLinks.style.right = "-200px";
          }
      </script>

        <!-----------Notification------->
<?php
    include("functions.php");
?>

   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item dropdown">
            <a class="nav-link" href="http://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Notifications 

                <?php
                $query = "SELECT * from `results`";
                if(count(fetchAll($query))>0){
                ?>
                <span class="badge badge-light"><?php echo count(fetchAll($query)); ?></span>
              <?php
                }
                    ?>
              </a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
                <?php
                $query = "SELECT * from `results` order by `date` DESC";
                 if(count(fetchAll($query))>0){
                     foreach(fetchAll($query) as $i){
                ?>
              <a style ="
                         <?php
                            if($i['difference_percentage'] < 50){
                                echo "font-weight:bold;";
                            }
                         ?>
                         " class="dropdown-item" href="view.php?id=<?php echo $i['id'] ?>">
                <small><i><?php echo date('F j, Y, g:i a',strtotime($i['date'])) ?></i></small><br/>
                  <?php 
                  
                if($i['difference_percentage'] < 50){
                    echo '<i style="color:red;">
      Warning! Water is considered dirty!</i> ';
                
                }else if($i['difference_percentage' > 50]){"Water is clean.";

                }
                  
                  ?>
                </a>
              <div class="dropdown-divider"></div>
                <?php
                     }
                 }else{
                     echo "No Records yet.";
                 }
                     ?>
            </div>
          </li>
        </ul>
     
      
      
      </div>
    </nav>

    <main role="main" class="container">

   

    </main><!-- /.container -->

      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
    <!------Footer------>

    <section class="footer">
      <h4>About Us</h4>
      <div class="icons">
          <i class="fa fa-facebook"></i>
          <i class="fa fa-twitter"></i>
          <i class="fa fa-instagram"></i>
          <i class="fa fa-snapchat"></i>
          <i class="fa fa-youtube"></i>
      </div>
  </section>
    </body>
</html>