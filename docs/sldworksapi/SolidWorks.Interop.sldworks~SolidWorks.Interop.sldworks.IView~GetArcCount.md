# GetArcCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcCount`

Gets the number of arcs in this view.
Gets the number of arcs in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetArcCount()
```

```

System.int GetArcCount()
```

```

System.int GetArcCount(); 
```

#### Return Value

Number of arcs

Remarks

Call this method before [IView::GetArcs4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4.md) to determine the size of the array for that method.

Example

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetArcs4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4.md)
