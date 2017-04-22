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
Users will then attach sections to compose the minisite.  
**Currently, the Home Page is created by default. There is not any way to remove it.**
`ds.sections["Home"].pages["Home"]` exists by default.  
  
**To add sections**, the API follows this syntax :
`ds.add_section("Section 1")` A section can have any name.  
Applying the `add_section` method to a Dashboard instance will create a new section.
  
**To add a page** to a given section, the API is similar :
`ds.sections["x"].add_page("y")` Here the `add_page` method is used. A page can also have any name.
To add a second page to this same section : `ds.sections["x"].add_page("z")`

**Special Case : **  
Users can decide to make a single-page section. In this case, SuperSight require to name the page `Page 1`:
`ds.sections["Section 1"].add_page("Page 1")` In this particular case `"Page 1"` is invisible since no dropdown is displayed for this section.
  
To populate pages with plots and data tables, a similar API is used. 


## Customization

