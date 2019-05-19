---
layout: post
title: 'Species Popularity vs Age: interactive visualization'
date: 2016-03-03 12:00:25.000000000 -08:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Articles
tags:
- data visualization
meta:
  _edit_last: '14'
  _social_notify: '1'
  _at_widget: '1'
  _social_broadcast_content: 'a:1:{s:7:"twitter";a:1:{i:403645425;s:97:"New interactive
    visualization: Species Popularity vs Age: http://www.adjectivespecies.com/?p=2680";}}'
  _social_broadcast_meta: a:1:{s:7:"twitter";a:1:{i:403645425;a:0:{}}}
  _social_aggregation_next_run: '1457032562'
  _social_broadcasted_ids: 'a:1:{s:7:"twitter";a:1:{i:403645425;a:1:{i:705468043657281536;a:3:{s:7:"message";s:3272:"eyJjcmVhdGVkX2F0IjoiVGh1IE1hciAwMyAxOTowMTowMyArMDAwMCAyMDE2IiwiaWQiOiI3MDU0NjgwNDM2NTcyODE1MzYiLCJpZF9zdHIiOiI3MDU0NjgwNDM2NTcyODE1MzYiLCJ0ZXh0IjoiTmV3IGludGVyYWN0aXZlIHZpc3VhbGl6YXRpb246IFNwZWNpZXMgUG9wdWxhcml0eSB2cyBBZ2U6IGh0dHBzOlwvXC90LmNvXC9hcDlwcERQSW82Iiwic291cmNlIjoiPGEgaHJlZj1cImh0dHBzOlwvXC9zb3ByZXN0by5tYWlsY2hpbXAuY29tXCIgcmVsPVwibm9mb2xsb3dcIj5Tb2NpYWwgUHJveHkgYnkgTWFpbGNoaW1wPFwvYT4iLCJ0cnVuY2F0ZWQiOmZhbHNlLCJpbl9yZXBseV90b19zdGF0dXNfaWQiOm51bGwsImluX3JlcGx5X3RvX3N0YXR1c19pZF9zdHIiOm51bGwsImluX3JlcGx5X3RvX3VzZXJfaWQiOm51bGwsImluX3JlcGx5X3RvX3VzZXJfaWRfc3RyIjpudWxsLCJpbl9yZXBseV90b19zY3JlZW5fbmFtZSI6bnVsbCwidXNlciI6eyJpZCI6IjQwMzY0NTQyNSIsImlkX3N0ciI6IjQwMzY0NTQyNSIsIm5hbWUiOiJbYWRqZWN0aXZlXVtzcGVjaWVzXSIsInNjcmVlbl9uYW1lIjoiYWRqc3BlY2llcyIsImxvY2F0aW9uIjoiIiwiZGVzY3JpcHRpb24iOiJFeHBsb3JpbmcgdGhlIGZ1cnJ5IHdvcmxkIGZyb20gdGhlIGluc2lkZSBvdXQuIiwidXJsIjoiaHR0cDpcL1wvdC5jb1wvWlloOVdtTFUwbiIsImVudGl0aWVzIjp7InVybCI6eyJ1cmxzIjpbeyJ1cmwiOiJodHRwOlwvXC90LmNvXC9aWWg5V21MVTBuIiwiZXhwYW5kZWRfdXJsIjoiaHR0cDpcL1wvYWRqZWN0aXZlc3BlY2llcy5jb20iLCJkaXNwbGF5X3VybCI6ImFkamVjdGl2ZXNwZWNpZXMuY29tIiwiaW5kaWNlcyI6WzAsMjJdfV19LCJkZXNjcmlwdGlvbiI6eyJ1cmxzIjpbXX19LCJwcm90ZWN0ZWQiOmZhbHNlLCJmb2xsb3dlcnNfY291bnQiOjE1MzUsImZyaWVuZHNfY291bnQiOjM3OSwibGlzdGVkX2NvdW50IjoyNywiY3JlYXRlZF9hdCI6IldlZCBOb3YgMDIgMTk6NTc6MzggKzAwMDAgMjAxMSIsImZhdm91cml0ZXNfY291bnQiOjM5MywidXRjX29mZnNldCI6LTI4ODAwLCJ0aW1lX3pvbmUiOiJQYWNpZmljIFRpbWUgKFVTICYgQ2FuYWRhKSIsImdlb19lbmFibGVkIjpmYWxzZSwidmVyaWZpZWQiOmZhbHNlLCJzdGF0dXNlc19jb3VudCI6MzAxMywibGFuZyI6ImVuIiwiY29udHJpYnV0b3JzX2VuYWJsZWQiOmZhbHNlLCJpc190cmFuc2xhdG9yIjpmYWxzZSwiaXNfdHJhbnNsYXRpb25fZW5hYmxlZCI6ZmFsc2UsInByb2ZpbGVfYmFja2dyb3VuZF9jb2xvciI6IkMwREVFRCIsInByb2ZpbGVfYmFja2dyb3VuZF9pbWFnZV91cmwiOiJodHRwOlwvXC9hYnMudHdpbWcuY29tXC9pbWFnZXNcL3RoZW1lc1wvdGhlbWUxXC9iZy5wbmciLCJwcm9maWxlX2JhY2tncm91bmRfaW1hZ2VfdXJsX2h0dHBzIjoiaHR0cHM6XC9cL2Ficy50d2ltZy5jb21cL2ltYWdlc1wvdGhlbWVzXC90aGVtZTFcL2JnLnBuZyIsInByb2ZpbGVfYmFja2dyb3VuZF90aWxlIjpmYWxzZSwicHJvZmlsZV9pbWFnZV91cmwiOiJodHRwOlwvXC9wYnMudHdpbWcuY29tXC9wcm9maWxlX2ltYWdlc1wvNDE2MzMxNDA2MjEwMzgzODcyXC9HMlhYRzljel9ub3JtYWwucG5nIiwicHJvZmlsZV9pbWFnZV91cmxfaHR0cHMiOiJodHRwczpcL1wvcGJzLnR3aW1nLmNvbVwvcHJvZmlsZV9pbWFnZXNcLzQxNjMzMTQwNjIxMDM4Mzg3MlwvRzJYWEc5Y3pfbm9ybWFsLnBuZyIsInByb2ZpbGVfbGlua19jb2xvciI6IjAwODRCNCIsInByb2ZpbGVfc2lkZWJhcl9ib3JkZXJfY29sb3IiOiJDMERFRUQiLCJwcm9maWxlX3NpZGViYXJfZmlsbF9jb2xvciI6IkRERUVGNiIsInByb2ZpbGVfdGV4dF9jb2xvciI6IjMzMzMzMyIsInByb2ZpbGVfdXNlX2JhY2tncm91bmRfaW1hZ2UiOnRydWUsImhhc19leHRlbmRlZF9wcm9maWxlIjpmYWxzZSwiZGVmYXVsdF9wcm9maWxlIjp0cnVlLCJkZWZhdWx0X3Byb2ZpbGVfaW1hZ2UiOmZhbHNlLCJmb2xsb3dpbmciOmZhbHNlLCJmb2xsb3dfcmVxdWVzdF9zZW50IjpmYWxzZSwibm90aWZpY2F0aW9ucyI6ZmFsc2V9LCJnZW8iOm51bGwsImNvb3JkaW5hdGVzIjpudWxsLCJwbGFjZSI6bnVsbCwiY29udHJpYnV0b3JzIjpudWxsLCJpc19xdW90ZV9zdGF0dXMiOmZhbHNlLCJyZXR3ZWV0X2NvdW50IjowLCJmYXZvcml0ZV9jb3VudCI6MCwiZW50aXRpZXMiOnsiaGFzaHRhZ3MiOltdLCJzeW1ib2xzIjpbXSwidXNlcl9tZW50aW9ucyI6W10sInVybHMiOlt7InVybCI6Imh0dHBzOlwvXC90LmNvXC9hcDlwcERQSW82IiwiZXhwYW5kZWRfdXJsIjoiaHR0cDpcL1wvd3d3LmFkamVjdGl2ZXNwZWNpZXMuY29tXC8/cD0yNjgwIiwiZGlzcGxheV91cmwiOiJhZGplY3RpdmVzcGVjaWVzLmNvbVwvP3A9MjY4MCIsImluZGljZXMiOls1OCw4MV19XX0sImZhdm9yaXRlZCI6ZmFsc2UsInJldHdlZXRlZCI6ZmFsc2UsInBvc3NpYmx5X3NlbnNpdGl2ZSI6ZmFsc2UsImxhbmciOiJlbiJ9";s:4:"urls";a:2:{i:0;s:95:"http://www.adjectivespecies.com/2016/03/03/species-popularity-vs-age-interactive-visualization/";i:1;s:39:"http://www.adjectivespecies.com/?p=2680";}s:7:"account";O:8:"stdClass":1:{s:4:"user";O:8:"stdClass":38:{s:2:"id";s:9:"403645425";s:6:"id_str";s:9:"403645425";s:4:"name";s:20:"[adjective][species]";s:11:"screen_name";s:10:"adjspecies";s:8:"location";s:0:"";s:3:"url";s:27:"http://adjectivespecies.com";s:11:"description";s:46:"Exploring
    the furry world from the inside out.";s:9:"protected";s:1:"0";s:15:"followers_count";s:3:"561";s:13:"friends_count";s:3:"350";s:12:"listed_count";s:1:"6";s:10:"created_at";s:30:"Wed
    Nov 02 19:57:38 +0000 2011";s:16:"favourites_count";s:2:"11";s:10:"utc_offset";s:6:"-28800";s:9:"time_zone";s:30:"Pacific
    Time (US &amp; Canada)";s:11:"geo_enabled";s:1:"0";s:8:"verified";s:1:"0";s:14:"statuses_count";s:4:"1944";s:4:"lang";s:2:"en";s:6:"status";a:10:{s:10:"created_at";s:30:"Sun
    Feb 17 15:21:53 +0000 2013";s:2:"id";s:18:"303162359898312705";s:6:"id_str";s:18:"303162359898312705";s:4:"text";s:49:"New
    Post: Birds of a Feather http://t.co/Y61Z4Ht6";s:6:"source";s:9:"TweetDeck";s:9:"truncated";s:1:"0";s:13:"retweet_count";s:1:"2";s:9:"favorited";s:1:"0";s:9:"retweeted";s:1:"0";s:18:"possibly_sensitive";s:1:"0";}s:20:"contributors_enabled";s:1:"0";s:13:"is_translator";s:1:"0";s:24:"profile_background_color";s:6:"C0DEED";s:28:"profile_background_image_url";s:47:"http://a0.twimg.com/images/themes/theme1/bg.png";s:34:"profile_background_image_url_https";s:49:"https://si0.twimg.com/images/themes/theme1/bg.png";s:23:"profile_background_tile";s:1:"0";s:17:"profile_image_url";s:71:"http://a0.twimg.com/profile_images/1647343758/adjspecies-ico_normal.png";s:23:"profile_image_url_https";s:73:"https://si0.twimg.com/profile_images/1647343758/adjspecies-ico_normal.png";s:18:"profile_link_color";s:6:"0084B4";s:28:"profile_sidebar_border_color";s:6:"C0DEED";s:26:"profile_sidebar_fill_color";s:6:"DDEEF6";s:18:"profile_text_color";s:6:"333333";s:28:"profile_use_background_image";s:1:"1";s:15:"default_profile";s:1:"1";s:21:"default_profile_image";s:1:"0";s:9:"following";s:1:"0";s:19:"follow_request_sent";s:1:"0";s:13:"notifications";s:1:"0";}}}}}}'
author:
  login: GuestPost
  email: submit@adjectivespecies.com
  display_name: GuestPost
  first_name: Guest
  last_name: Poster
---
<p><a href="http://vis.adjectivespecies.com/species-age/">Click here for our interactive species popularity vs age visualization</a>.</p>
<p><em>Visualization by Ruxley. Species and age data taken from the 2015 Furry Survey. click through for the interactive version.</em></p>
<p><a href="http://vis.adjectivespecies.com/species-age/" rel="attachment wp-att-2681"><img class="aligncenter size-full wp-image-2681" src="{{ site.baseurl }}/assets/Screen-Shot-2016-03-03-at-18.54.04.png" alt="Screen Shot of the [a][s] species popularity vs age vis" width="869" height="567" /></a></p>



