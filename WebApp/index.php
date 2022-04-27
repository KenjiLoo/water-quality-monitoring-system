<?php include_once ("controller.php"); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Login Page</title>
        <link rel="stylesheet" href="styles.css">
        <script src="main.js"></script>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    
    <section class="login-header">
        <body style="display: flex; text-align: center">
            <div style="padding: 3em;">
                <img src="images/frontpagelogo.png" style="top:5px;">
            </div>
        </body>
    </section>
    
    <section>
        <div class="center" style="margin-top:5em;">
            <h1>Login</h1>
            <form action="login.php" method="POST" autocomplete="off">
                <?php
                            if(isset($_SESSION["error"])){
                                $error = $_SESSION["error"];
                                echo"<i style='color: red'>$error</i>";
                            } elseif(isset($_SESSION["error2"])){
                                $error2 = $_SESSION["error2"];
                                echo"<i style='color: red'>$error2</i>";
                            } 
                    ?>
            
                <div class="txt_field">
                    <input type="text" id="userName" name="userName" required>
                    <label>Username</label>
                </div>
                <div class="txt_field">
                    <input type="password" id="password" name="password" required>
                    <span>
                        <i class="fa fa-eye" id="eye" onclick="togglePW()" aria-hidden="true"></i>
                    </span>
                    <label>Password</label>
                </div>
                <script>
                    var state = false;
                    function togglePW(){
    
                    if(state){
                        document.getElementById("password").setAttribute("type","password");
                        document.getElementById("eye").style.color='#7a797e';
                        state = false;
                    } else{
                        document.getElementById("password").setAttribute("type","text");
                        document.getElementById("eye").style.color='#5887ef';
                        state = true;
                }
            }
                </script>
                
                <input type="submit" value="login" name="login">
                <div class="signup_link">
                <a href="forgot-passpage.php" id="forgot-passpage">Forgot Your Password?</a>
                </div>
                <div class="signup_link">
                    Not a member? <a href="registrationpage.php">Signup</a>
                </div>
            </form>
         </div>
    </section>

</html>

<?php
    unset($_SESSION["error"]);
    unset($_SESSION["error2"]);
?>