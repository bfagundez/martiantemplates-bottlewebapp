%rebase admin/layout get_url=get_url, user=user
<div class="container">
	% if user is not None:
	<form action="/admin/user/save" class="form-horizontal" method="post">
		
		<legend>Edit user</legend>
  
		<div class="control-group">
	  	  	<label class="control-label" for="user_name">Username</label>
	  	  	<div class="controls">
				<input type="text" name="user_name" placeholder="username" value="{{user.user_name}}" id="user_name">
			</div>
		</div>
		
		<div class="control-group">
	  	  	<label class="control-label" for="email_address">Email</label>
	  	  	<div class="controls">
				<input type="text" name="email_address" placeholder="email@domain.com" value="{{user.email_address}}" id="email_address">
			</div>
		</div>
	  	
		<div class="control-group">
	  	  	<label class="control-label" for="password">Password</label>
	  	  	<div class="controls">
				<input type="password" name="password"  value="" id="password">
				
			</div>
		</div>
		
		<input type="hidden" name="user_id"  value="{{user.user_id}}" id="user_id">
		
		<div class="control-group">
			<div class="controls">
				<button type="submit" class="btn btn-primary">Save</button>
				<button class="btn ">Cancel</button>
			</div>
		</div>
		
	</form>
	
	% else:
	<form action="/admin/user/save" class="form-horizontal" method="post">
		
		<legend>New user</legend>
  
		<div class="control-group">
	  	  	<label class="control-label" for="user_name">Username</label>
	  	  	<div class="controls">
				<input type="text" name="user_name" placeholder="username" value="" id="user_name">
			</div>
		</div>
		
		<div class="control-group">
	  	  	<label class="control-label" for="email_address">Email</label>
	  	  	<div class="controls">
				<input type="text" name="email_address" placeholder="email@domain.com" value="" id="email_address">
			</div>
		</div>
	  	
		<div class="control-group">
	  	  	<label class="control-label" for="password">Password</label>
	  	  	<div class="controls">
				<input type="password" name="password"  value="" id="password">
				
			</div>
		</div>
		
		<div class="control-group">
			<div class="controls">
				<button type="submit" class="btn btn-primary">Save</button>
				<button class="btn ">Cancel</button>
			</div>
		</div>
		
	</form>
	%end
</div>
