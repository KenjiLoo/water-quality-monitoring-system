<?php include_once ("controller.php"); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Change Password</title>
        <link rel="stylesheet" href="styles.css">
        <script src="main.js"></script>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <section class="login-header">
        <body style="display: flex; text-align: center"></body>
    </section>
    <div id="container">
        <div class="center">

        
        <div id="line"></div>
        <form action="newPassword.php" method="POST" autocomplete="off">
            <?php
            if ($errors > 0) {
                foreach ($errors as $displayErrors) {
            ?>
                    <i style ='color: red'><?php echo $displayErrors; ?></style>
            <?php
                }
            }
            ?>
            <h1>Enter your new password<h1>
            <div class="txt_field">
                <input type="password" name="password" required>
                <label>New password</label>
            </div>
            <div class="txt_field">
                <input type="password" name="confirmPassword" required>
                <label>Confirm your new password</label>
            </div>
            
            <input type="submit" name="changePassword" value="Save">
        </form>
    </div>
    </div>
</body>
</html>