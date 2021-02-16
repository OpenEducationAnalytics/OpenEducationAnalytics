## Welcome to OpenEduAnalytics

This site will provide a blog as well as videos with details on the setup and use of OpenEduAnalytics.

### Posts
<ul>
  {% for post in site.posts %}
    <li>
      <a href="/OpenEduAnalytics{{ post.url }}">{{post.date | date: '%B %d, %Y' }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

### Videos

Example video #1:
{% include youtubePlayer.html id="e1HGXxMsLxg" %}

Example video #2:
