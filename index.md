---
title: Общественно-политическая газета Лежневского района
layout: default
---

{% assign last_issue = site.issues | reverse | first %}
{% assign posts = site.posts | where: "categories", last_issue.number | where: "categories", last_issue.year %}

<div class="tbl" style="border-bottom: 4px solid #aaa;">
    <div class="raw">
        <dl class="column small">
            <dt><span class="date">{{ last_issue.day }}.{{ last_issue.month }}.{{ last_issue.year }}</span></dt>
            <dd>
                {% assign post = posts[0] %}
                {% include post_preview.html %}
            </dd>
            <dd style="display: none;"></dd>
            <dt><span class="date">{{ last_issue.day }}.{{ last_issue.month }}.{{ last_issue.year }}</span></dt>
            <dd>
                {% assign post = posts[2] %}
                {% include post_preview.html %}
            </dd>
        </dl>
        <div class="column big">
            {% assign post = posts[4] %}
            <h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
            <p>{{ post.excerpt }}</p>
        </div>
    </div>
</div>
<ul class="only_text">
    <li>
        {% assign post = posts[1] %}
        {% include post_preview.html %}
        <p class="date">{{ last_issue.day }}.{{ last_issue.month }}.{{ last_issue.year }}</p>
    </li>
    <li>
        {% assign post = posts[3] %}
        {% include post_preview.html %}
        <p class="date">{{ last_issue.day }}.{{ last_issue.month }}.{{ last_issue.year }}</p>
    </li>
</ul>
