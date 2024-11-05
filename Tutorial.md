# flet-tutorial
This repor is for all the Flet tutorials in order to learn this framework.

## Installation 

pip install flet

flet --version

## Create new project

flet create \<App Name\>

This creates a project with the following template:
```
\<App Name\>
|
|->tutorial
    |
    |->asset
        |
        |->icon.png
    .gitignore
    main.py //this is the main file for running the programm
    README.md
    requirements.txt
```

## Running the app

```
flet run //Runs the main.py at cerntain directory
```

If you need to provide a different path to the file, use the following command:

```
flet run [script]
```

To run as an app:
```
flet run --web [script]
```
or to run in a fixed port:
```
flet run --web --port 8000 app.py
```


## Flet controls

User interface is made of Controls (aka widgets). To make controls visible to a user they must be added to a Page or inside other controls. Page is the top-most control. Nesting controls into each other could be represented as a tree with Page as a root.

To display control on a page add it to controls list of a Page and call page.update() to send page changes to a browser or desktop client.

You can modify control properties and the UI will be updated on the next page.update().

Some controls are "container" controls (like Page) which could contain other controls. For example, Row control allows arranging other controls in a row one-by-one, or TextField and ElevatedButton next to it.

page.update() is smart enough to send only the changes made since its last call, so you can add a couple of new controls to the page, remove some of them, change other controls' properties and then call page.update() to do a batched update.

Some controls, like buttons, could have event handlers reacting on a user input, for example ElevatedButton.on_click
```
Flet implements imperative UI model where you "manually" build application UI with stateful controls and then mutate it by updating control properties. Flutter implements declarative model where UI is automatically re-built on application data changes. Managing application state in modern frontend applications is inherently complex task and Flet's "old-school" approach could be more attractive to programmers without frontend experience.
```
### visible property
Every control has visible property which is true by default - control is rendered on the page. Setting visible to false completely prevents control (and all its children if any) from rendering on a page canvas. Hidden controls cannot be focused or selected with a keyboard or mouse and they do not emit any events.

### disabled property
Every control has disabled property which is false by default - control and all its children are enabled. disabled property is mostly used with data entry controls like TextField, Dropdown, Checkbox, buttons. However, disabled could be set to a parent control and its value will be propagated down to all children recursively.


*Buttons*:Button is the most essential input control which generates click event when pressed

Flet provides a number of controls for building forms: TextField, Checkbox, Dropdown, ElevatedButton.

## Custom controls
Via inheritance it can be modified the style and behaviour of any control. See customcontrols.py for demos

**Composite custom controls** inherit from container controls such as Column, Row, Stack or even View to combine multiple Flet controls. The example below is a Task control that can be used in a To-Do app.

## Life-cycle methods
Custom controls provide life-cycle "hook" methods that you may need to use for different use cases in your app.

**build()** method is called when the control is being created and assigned its self.page.

Override build() method if you need to implement logic that cannot be executed in control's constructor because it requires access to the self.page. For example, choose the right icon depending on self.page.platform for your adaptive app.

**did_mount()** method is called after the control is added to the page and assigned transient uid.

Override did_mount() method if you need to implement logic that needs to be executed after the control was added to the page, for example Weather widget which calls Open Weather API every minute to update itself with the new weather conditions.


**will_unmount()** method is called before the control is removed from the page.

Override will_unmount() method to execute clean-up code.

**before_update()** method is called every time when the control is being updated.

Make sure not to call update() method within before_update().

## Custom control has is_isolated property which defaults to False.

If you set is_isolated to True, your control will be isolated from outside layout, i.e. when update() method is called for the parent control, the control itself will be updated but any changes to the controls' children are not included into the update digest. Isolated controls should call self.update() to push its changes to a Flet page.

As a best practice, any custom control that calls self.update() inside its class methods should be isolated.