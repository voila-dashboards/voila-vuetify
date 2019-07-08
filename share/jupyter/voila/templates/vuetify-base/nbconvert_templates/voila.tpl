<!DOCTYPE html>
<html>
    <head>
        <script src="{{resources.base_url}}voila/static/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
    </head>

    <body data-base-url="{{resources.base_url}}voila/">
        {% include "app.html" %}
    </body>

    <script id="jupyter-config-data" type="application/json">
        {
          "baseUrl": "{{resources.base_url}}",
          "kernelId": "{{resources.kernel_id}}"
        }
    </script>

    <script>
        requirejs.config({
            baseUrl: '{{resources.base_url}}voila',
            waitSeconds: 3000,
            {% for ext in resources.nbextensions if ext == 'jupyter-vuetify/extension'-%}
            map: {
                '*': {
                    'jupyter-vuetify': 'nbextensions/jupyter-vuetify'
                },
            },
            paths: {
                vue: '{{resources.base_url}}voila/static/deps/index'
            }
            {% endfor %}
        });
        requirejs([
            {% for ext in resources.nbextensions if ext != 'jupyter-vuetify/extension'-%}
                "{{resources.base_url}}voila/nbextensions/{{ ext }}.js",
            {% endfor %}
        ]);
        {% include "util.js" %}
    </script>
</html>

