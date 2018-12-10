from django.conf.urls import url
from . import views
urlpatterns = [

	# Page Paths

# - - = - = + = + = - = - - #

	# Allowed when Logged Out

# - - = - = + = + = - = - - #
	# home
	url(r'^$',views.index),

# - - = - = + = + = - = - - #
	# signup page
	url(r'^signup$',views.signup),

	# signup form submit
	url(r'^signup/submit$',views.signup_submit),

# - - = - = + = + = - = - - #
	# login page
	url(r'^login$',views.login),

	# login form submit
	url(r'^login/submit$',views.login_submit),


# - - = - = + = + = - = - - #


	# logout form submit
	url(r'^logout$',views.logout),


# - - = - = + = + = - = - - #

	# Required Logged in

# - - = - = + = + = - = - - #
	# my dashboard
	url(r'^user$',views.my_dashboard),

# - - = - = + = + = - = - - #
	# a user with id:u_id dashboard (with private/public filter applied)
	url(r'^user/(?P<u_id>\d+)$',views.dashboard),

	# send friend request to user with id:u_id
	url(r'^user/(?P<u_id>\d+)/friend$',views.friend_request),

	# accept friend request from user with id:u_id
	url(r'^user/(?P<u_id>\d+)/accept$',views.friend_request_accept),

	# decline friend request from user with id:u_id
	url(r'^user/(?P<u_id>\d+)/decline$',views.friend_request_decline),

	# unfriend user with id:u_id
	url(r'^user/(?P<u_id>\d+)/unfriend$',views.unfriend),

# - - = - = + = + = - = - - #
	# a group with id:g_id dashboard (with private/public filter applied)
	url(r'^group/(?P<g_id>\d+)$',views.group),

	# send an invitation to join group with id:g_id to user with id:u_id
	url(r'^group/(?P<g_id>\d+)/invite/(?P<u_id>\d+)$',views.group_invite),

	# cancel an invitation to join group with id:g_id to user with id:u_id
	url(r'^group/(?P<g_id>\d+)/cancel_invite/(?P<u_id>\d+)$',views.group_cancel_invite),

	# accept an invitation to join group with id:g_id
	url(r'^group/(?P<g_id>\d+)/accept$',views.group_accept_invite),

	# decline an invitation to join group with id:g_id
	url(r'^group/(?P<g_id>\d+)/decline$',views.group_decline_invite),

	# send an application to join group with id:g_id
	url(r'^group/(?P<g_id>\d+)/apply$',views.group_apply),

	# cancel an application to join group with id:g_id
	url(r'^group/(?P<g_id>\d+)/cancel_apply$',views.group_cancel_apply),

	# accept an application to join group with id:g_id from user with id:u_id
	url(r'^group/(?P<g_id>\d+)/accept/(?P<u_id>\d+)$',views.group_accept_application),

	# decline an application to join group with id:g_id from user with id:u_id
	url(r'^group/(?P<g_id>\d+)/decline/(?P<u_id>\d+)$',views.group_decline_application),

# - - = - = + = + = - = - - #
	# a event with id:e_id dashboard (with private/public filter applied)
	url(r'^event/(?P<e_id>\d+)$',views.event),

	# send an invitation to join event with id:e_id to user with id:u_id
	url(r'^event/(?P<e_id>\d+)/invite/(?P<u_id>\d+)$',views.event_invite),

	# cancel an invitation to join event with id:e_id to user with id:u_id
	url(r'^event/(?P<e_id>\d+)/cancel_invite/(?P<u_id>\d+)$',views.event_cancel_invite),

	# accept an invitation to join event with id:e_id with a might attend marker
	url(r'^event/(?P<e_id>\d+)/accept_might$',views.event_accept_might_invite),

	# accept an invitation to join event with id:e_id with a will attend marker
	url(r'^event/(?P<e_id>\d+)/accept_will$',views.event_accept_will_invite),

	# decline an invitation to join event with id:e_id
	url(r'^event/(?P<e_id>\d+)/decline$',views.event_decline_invite),

# - - = - = + = + = - = - - #
	# new group
	url(r'^new/group$',views.new_group),

	# new group form submit
	url(r'^new/group/submit$',views.new_group_submit),

# - - = - = + = + = - = - - #
	# new event
	url(r'^new/event$',views.new_event),

	# new event form submit
	url(r'^new/event/submit$',views.new_event_submit),

# - - = - = + = + = - = - - #
	# search box page (possibly just in nav)
	url(r'^search$',views.search),

	# search submit
	url(r'^search/submit$',views.search_submit),

# - - = - = + = + = - = - - #
	# search users result page
	url(r'^search/user/(?P<name_like>\d+)$',views.search_user),

# - - = - = + = + = - = - - #
	# search groups result page
	url(r'^search/group/(?P<name_like>\d+)$',views.search_group),

# - - = - = + = + = - = - - #
	# search events result page
	url(r'^search/event/(?P<name_like>\d+)$',views.search_events),

# - - = - = + = + = - = - - #
	# search locations result page
	url(r'^search/location/(?P<near_address>\d+)$',views.search_location),

# - - = - = + = + = - = - - #
	# location with name:place_name and coordinates:long,lat,zed page
	url(r'^location/(?P<place_name>\d+)/(?P<long>[0-9\.]+)/(?P<lat>[0-9\.]+)/(?P<zed>[0-9\.]+)$',views.location),

	# location submit to current location lookup
	url(r'^location/(?P<place_name>\d+)/(?P<long>[0-9\.]+)/(?P<lat>[0-9\.]+)/(?P<zed>[0-9\.]+)/submit$',views.location_submit),

	# Required Ownership

	# edit my dashboard
	url(r'^edit/user$',views.edit_dashboard),

	# edit group with id:g_id dashboard (only accessible by owner redirects with flash otherwise)
	url(r'^edit/group/(?P<g_id>\d+)$',views.edit_group),

	# edit event with id:e_id dashboard (with private/public filter applied)
	url(r'^edit/event/(?P<e_id>\d+)$',views.edit_event),

]

