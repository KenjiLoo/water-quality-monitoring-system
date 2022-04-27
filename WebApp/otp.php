<?php include_once ("controller.php"); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>OTP Verification Page</title>
        <link rel="stylesheet" href="styles.css">
        <script src="main.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <section class="login-header">
        <body style="display: flex; text-align: center">
            <div style="padding: 5em;">
                <img src="images/frontpagelogo.png">
            </div>
        </body>
    </section>
    <div class="center">
        <h2>Sign Up</h2>
        <div id="line"></div>
        <form action="otp.php" method="POST" autocomplete="off">
            <?php
            if(isset($_SESSION['message'])){
                ?>
                <div id="alert"><?php echo $_SESSION['message']; ?></div>
                <?php
            }
            ?>

            <?php
            if($errors > 0){
                foreach($errors AS $displayErrors){
                ?>
                <div id="alert"><?php echo $displayErrors; ?></div>
                <?php
                }
            }
            ?>      
            <input type="number" name="otp" placeholder="Verification Code" required><br>
            <input type="submit" name="verify" value="Verify">
        </form>
    </div>
</body>
</html>