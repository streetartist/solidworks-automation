# TaskPaneIsPinned Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned`

Gets or sets whether the SOLIDWORKS Task Pane is pinned.
Gets or sets whether the SOLIDWORKS Task Pane is pinned.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TaskPaneIsPinned As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.TaskPaneIsPinned = value
 
value = instance.TaskPaneIsPinned
```

```

System.bool TaskPaneIsPinned {get; set;}
```

```

property System.bool TaskPaneIsPinned {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if SOLIDWORKS Task Pane is pinned, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ActivateTaskPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.md)  
[ISldWorks::CreateTaskpaneView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.md)  
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.md)  
[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)
