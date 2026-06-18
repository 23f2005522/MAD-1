from jinja2 import Template

data = [1, 2, 3, 4, 5]

temp = """
                {%- for item in data %}
                    {{ item }}
                {%- endfor %}
                
        """

t = Template(temp)

print(t.render(data=data))
