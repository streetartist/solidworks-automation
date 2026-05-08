# GetTaskpaneViewWndx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64`

Gets the Taskpane view window handle.
Gets the Taskpane view window handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTaskpaneViewWndx64() As System.Long
```

```

Dim instance As ITaskpaneView
Dim value As System.Long
 
value = instance.GetTaskpaneViewWndx64()
```

```

System.long GetTaskpaneViewWndx64()
```

```

System.int64 GetTaskpaneViewWndx64(); 
```

#### Return Value

Window handle

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

To insert a Task Pane view window, create your Task Pane view window and pass its handle to SOLIDWORKS using [ITaskpaneView::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)
