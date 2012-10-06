%rebase admin/layout get_url=get_url, users=users
<div class="container">
	<!-- Users table -->
	<table id="users_table" class="table table-striped table-bordered table-hover">
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
					<a href="admin/user/{{row.user_id}}" class="btn btn-small">Edit</a>
					<a href="admin/user/delete/{{row.user_id}}" class="btn btn-small btn-danger">Delete</a>
				</td>
			</tr>
			%end
		</tbody>							
	</table>	
	
	<a href="admin/user/new/" class="btn btn-primary">New user</a>
</div>