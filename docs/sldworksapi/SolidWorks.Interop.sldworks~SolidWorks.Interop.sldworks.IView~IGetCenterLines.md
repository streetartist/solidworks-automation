# IGetCenterLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterLines`

Gets all of the centerlines on this drawing view.
Gets all of the centerlines on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCenterLines( _
   ByVal NumCenterLine As System.Integer _
) As Centerline
```

```

Dim instance As IView
Dim NumCenterLine As System.Integer
Dim value As Centerline
 
value = instance.IGetCenterLines(NumCenterLine)
```

```

Centerline IGetCenterLines( 
   System.int NumCenterLine
)
```

```

Centerline^ IGetCenterLines( 
   System.int NumCenterLine
) 
```

#### Parameters

*NumCenterLine*
:   Total number of centerlines on this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [centerlines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of centerlines all at once instead of calling [IView::GetFirstCenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.md) and then repeatedly calling [ICenterLine::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetNext.md) to obtain the remaining centerlines on the drawing view.

Before calling this method, call [IView::GetCenterLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineCount.md) to get the value for numCenterLine.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.md)
