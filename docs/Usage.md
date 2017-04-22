# Usage
## API usage

### The Plot_gatherer object

SuperSight collects plots and, at render time, it saves these in dedicated folders.
To make this process easier, SuperSight comes with a Plot_gatherer object :

```Python
from supersight import Plots_gatherer
plots = Plots_gatherer()
```

Once the user has instanciated this object, he can use it to save plots for later use using the `add_plot` method:

```Python
import matplotlib.pyplot as plt

graph = plt.figure()
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black');

buf = io.BytesIO()
plt.savefig(buf, format='svg')
plots.add_plot("first graph", buf)
```

The three last lines above are necessary to save the plot. A Plot_gatherer instance behaves like a dictionnary. On the last line our plot is assigned to a name (`"first graph"`in this case).

Hence two plots cannot have the same name.  
Users can save as many plots as they want the limitation being the memory.

### The Dashboard object
#### Instanciation
The Dashboard object represents the highest level of the report. It is the container of all other objects.  

Other objects are :

 - Sections which appear in the navbar. They contain pages
 - Pages which appear in a dropdown when a section is clicked
 - Elements (plots and data tables) which are displayed on a page according to the Bootstrap grid system.

Below a Dashboard object is instanciated as ds :

```Python
from supersight import Dashboard
ds = Dashboard()
```

Currently, you should instanciate this object without any parameters. In the future, it will be possible to change some default behaviors though.  
Next, some attributes should be changed to get rid of default values. Below is an extract of the module :
```Python
self.name = "New Dashboard"
self.title = "Super Sight is self hostable dashboard to properly report your work"
self.display = "Welcome to <b>Super Sight !</b>"
self.display_message = """Super Sight generates a multipage dashboard from a Matplotlib 
plots collection. It helps data scientists and business analysts reporting their work in a 
methodical and structured manner. It is lightweight, hackable, written in Python and you can host 
its static output anywhere (local network, AWS S3 ...)."""
self.nav_bar_right_side = "Custom information here"
self.footer = "&copy; SuperSight 2017
```
Hence users can do :
```Python
ds.name = "custom name" 
ds.title = "custom sentence to be used as title"
ds.display = "Big Display"
...
```
#### Sections

Users will then attach sections to compose the minisite.  
**Currently, the Home Page is created by default. There is not any way to remove it.**
`ds.sections["Home"].pages["Home"]` exists by default.  
  
**To add sections**, the API follows this syntax :
`ds.add_section("Section 1")` A section can have any name.  
Applying the `add_section` method to a Dashboard instance will create a new section.
  
#### Pages

**To add a page** to a given section, the API is similar :
`ds.sections["x"].add_page("y")` Here the `add_page` method is used. A page can also have any name.
To add a second page to this same section : `ds.sections["x"].add_page("z")`

**Special Case : **  
Users can decide to make a single-page section. In this case, SuperSight require to name the page `Page 1`:
`ds.sections["Section 1"].add_page("Page 1")` In this particular case `"Page 1"` is invisible since no dropdown is displayed for this section.
  
#### Plots

To populate pages with plots and data tables, a similar API is used. 
To add a plot already saved in the plot gatherer :  
```Python
ds.sections["x"].pages["z"].add_element(name = "plot 1", 
                                        plot_object = plots.get_plot("saved plot"))
```
We just added a plot to the page z in the section x.  

It is worth noting that a name is specified for an element. This name will be used to save a file in the folder dedicated to the section x.  
**Hence, two plots cannot have the same name within the same section even though they are displayed on two different pages. Sections isolate completely elements because files are are stored in different folders while pages divide elements only in the HTML output**.  
  
#### Data Tables

To add a data table, the following method should be used :
```Python
ds.sections["x"].pages["z"].add_element(name = "pivot table")
ds.sections["x"].pages["z"].elements["pivot table"].add_table(df2)
```
Currently, to add a data table, a second line is necessary. df2 is a Pandas.Dataframe object. 

#### Page Layout

I users wish to change how plots and data tables are displayed on a page, they can modify the layout thanks to this command :  
```Python
ds.sections["x"].pages["z"].layout = [(8, 4), (6,6), (12,), (12,)]
```
the layout parameter wait a list of tuples. Each tuple reprensents one line. The length of the tuple is the number of elements on the row.
According to Bootstrap grid system, a line should be equal to twelve. In SuperSight, the default layout is :  
`[(6, 6), (6, 6), (6, 6)]`  

#### Headings and Comments

To enrich a plot or a data table, SuperSight allows to add Headings and Comments.
Users could specify Headings and Comments within the `add_element` method :  
```Python
ds.sections["x"].pages["z"].add_element(name = "info", heading = "Heading", 
                                        plot_object = plots.get_plot("saved plot"),  
                                        comment_below = "A comment below the element", 
                                        comment_above = "A comment above the element")
```  
Users could also add comments after an element is added via these methods :  
```Python
ds.sections["x"].pages["z"].elements["info"].add_comment_above("A comment below the element")
ds.sections["x"].pages["z"].elements["info"].add_comment_below("A comment above the element")
ds.sections["x"].pages["z"].elements["info"].add_heading("Heading")
```  
Finally, it is possible to display math in comments using MathJax :  
```Python
com = """You can also use MathJax : $x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$"""
ds.sections["x"].pages["z"].elements["info"].add_comment_below(com)
```
The mathematical expression is surrounded by `$`.
  
#### The render method

To generate the output, call the `render` method on the Dashboard object :  
`ds.render()`

## Customization

To customize the template, users can clone the template folder [here](https://github.com/CamilleMo/SuperSight/tree/master/supersight/default_template), and make changes in `index.html` or in CSS files. Once the template is customized, call the `render method` specifying the path of the new template folder :  
`ds.render(template='customized_template')`  
Here the complete folder `'customized_template'` is in the current directory.
