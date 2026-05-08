# ShowView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~ShowView`

Activates the application-level tab of the Task Pane view and makes the view visible.
Activates the application-level tab of the Task Pane view and makes the view visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowView() As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim value As System.Boolean
 
value = instance.ShowView()
```

```

System.bool ShowView()
```

```

System.bool ShowView(); 
```

#### Return Value

True if application-level tab of the Task Pane view is visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::HideView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~HideView.md)
