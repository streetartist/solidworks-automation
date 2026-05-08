# GetTaskpaneViewWnd Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWnd`

Obsolete. Superseded by ITaskpaneView::GetTaskpaneViewWndx64.
Obsolete. Superseded by [ITaskpaneView::GetTaskpaneViewWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTaskpaneViewWnd() As System.Integer
```

```

Dim instance As ITaskpaneView
Dim value As System.Integer
 
value = instance.GetTaskpaneViewWnd()
```

```

System.int GetTaskpaneViewWnd()
```

```

System.int GetTaskpaneViewWnd(); 
```

#### Return Value

CWnd object pointer

Remarks

This method gets a Task Pane view window object pointer for 32-bit MFC applications only.

Because this method is valid only for 32-bit applications, it is now obsolete.

To insert a Task Pane view window, create your Task Pane view window and pass its handle to SOLIDWORKS using [ITaskpaneView::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)
