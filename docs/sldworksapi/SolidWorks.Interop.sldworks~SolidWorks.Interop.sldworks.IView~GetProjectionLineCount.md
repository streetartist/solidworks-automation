# GetProjectionLineCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount`

Gets the number of projection lines (arrows) in this drawing view.
Gets the number of projection lines (arrows) in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProjectionLineCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetProjectionLineCount()
```

```

System.int GetProjectionLineCount()
```

```

System.int GetProjectionLineCount(); 
```

#### Return Value

Number of projection lines in this drawing view

Remarks

This method only works for base drawing views; it does not work for projected or auxiliary views.

Call this method before [IView::IGetProjectionLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.md)  
[IView::GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.md)  
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.md)  
[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.md)
