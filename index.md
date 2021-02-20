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

Basic setup of OEA:
{% include youtubePlayer.html id="7QnRPHK1vXg" %}
