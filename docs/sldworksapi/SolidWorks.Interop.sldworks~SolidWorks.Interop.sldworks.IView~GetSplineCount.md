# GetSplineCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplineCount`

Gets the number of splines in the view.
Gets the number of splines in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineCount( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim PointCount As System.Integer
Dim value As System.Integer
 
value = instance.GetSplineCount(PointCount)
```

```

System.int GetSplineCount( 
   out System.int PointCount
)
```

```

System.int GetSplineCount( 
   [Out] System.int PointCount
) 
```

#### Parameters

*PointCount*
:   Number of doubles (see [IView::GetSplines3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplines3.md) or [IView::IGetSplines3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSplines3.md) Remarks)

#### Return Value

Number of splines in the view

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
