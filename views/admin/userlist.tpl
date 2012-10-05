%rebase admin/layout get_url=get_url, users=users

	<!-- Users table -->
	<table id="users_table">
		<thead>
			<tr>
				<th>Id</th>
				<th>Username</th>
				<th>Email</th>
				<th>Actions</th>
			</tr>
		</thead>
		<tbody>
			%for row in users:
			<tr>
				<td> {{row.user_id}}</td>
				<td> {{row.user_name}}</td>
				<td> {{row.email_address}}</td>
				<td> 
					<a href="/user/edit/{{row.user_id}}">Edit</a>
					<a href="/user/delete/{{row.user_id}}">Delete</a>
				</td>
			</tr>
			%end
		</tbody>							
	</table>	
	
	<a href="/user/new/">New user</a>
	