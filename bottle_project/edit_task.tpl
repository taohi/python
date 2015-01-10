<html>
<body bgcolor="#d0d0d0">
<p>Edit task with ID={{no}}</p>
<form action="/edit/{{no}}" method="GET">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>
</br>
<input type="submit" name="save" value="save">
</form>
</body>
</html>
