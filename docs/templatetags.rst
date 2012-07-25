.. _templatetags:


Template Tags
=============

There is a single template tag in this project. It can be used if you want
to display event logs for a particular user::

    {% load eventlog_tags %}
    
    {% user_event_log user as logs %}
    
    {% if logs.count > 0 %}
    <table>
        <thead><tr><th>Timestamp</th><th>Action</th><th>Data</th></tr></thead>
        <tbody>
        {% for log in logs %}
            <tr>
                <td>{{ log.timestamp }}</td>
                <td>{{ log.action }}</td>
                <td><code>{{ log.extra }}</code></td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
    {% endif %}
