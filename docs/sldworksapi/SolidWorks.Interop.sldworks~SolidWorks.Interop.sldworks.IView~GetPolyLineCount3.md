# GetPolyLineCount3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount3`

Obsolete. Superseded by IView::GetPolyLineCount5.
Obsolete. Superseded by [IView::GetPolyLineCount5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPolyLineCount3( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim PointCount As System.Integer
Dim value As System.Integer
 
value = instance.GetPolyLineCount3(PointCount)
```

```

System.int GetPolyLineCount3( 
   out System.int PointCount
)
```

```

System.int GetPolyLineCount3( 
   [Out] System.int PointCount
) 
```

#### Parameters

*PointCount*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
