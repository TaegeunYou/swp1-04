html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                a = <input type="number" name="a">
            </p>
            <p>
                b = <input type="number" name="b">
            </p>
            <p>
                <input type="submit">
            </p>
        </form>
        <p>
            a: %(a)s</br>
            b: %(b)s</br>
            sum: %(sum)s</br>
            multiplication: %(multiplication)s</br>
        </p>
    </body>
</html>
"""
