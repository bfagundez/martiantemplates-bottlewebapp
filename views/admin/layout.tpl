<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<!-- Set the viewport width to device width for mobile -->
		<meta name="viewport" content="width=device-width" />
		<title>Martiantools webapp template</title>
		
		<!-- CSS Files -->
		%include partials/css_partial get_url=get_url
		
		<!-- JS Files -->
		%include partials/js_partial get_url=get_url
		
	</head>

	<body>
		<!-- Header -->
		%include admin/partials/header.tpl
		<!-- Page content -->
		%include
		<!-- Footer -->
		%include admin/partials/footer.tpl
	</body>
</html>