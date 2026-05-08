# DeleteView Method (ITaskpaneView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DeleteView`

Removes the application-level tab from the Task Pane view.
Removes the application-level tab from the Task Pane view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteView() As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim value As System.Boolean
 
value = instance.DeleteView()
```

```

System.bool DeleteView()
```

```

System.bool DeleteView(); 
```

#### Return Value

True if tab is removed, false if not

Example

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)
