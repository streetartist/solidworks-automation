# GetViewHWnd Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd`

Gets the Microsoft window handle for this model view.
Gets the Microsoft window handle for this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewHWnd() As System.Integer
```

```

Dim instance As IModelView
Dim value As System.Integer
 
value = instance.GetViewHWnd()
```

```

System.int GetViewHWnd()
```

```

System.int GetViewHWnd(); 
```

#### Return Value

Microsoft window handle

Remarks

If your application must be x64 compatible, then use [IModelView::GetViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWndx64.md).

Window handles are not unique across computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.md)
