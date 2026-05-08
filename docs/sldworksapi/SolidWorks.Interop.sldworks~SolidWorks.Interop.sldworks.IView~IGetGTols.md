# IGetGTols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols`

Gets all of the geometric tolerances on this drawing view.
Gets all of the geometric tolerances on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetGTols( _
   ByVal NumGTol As System.Integer _
) As Gtol
```

```

Dim instance As IView
Dim NumGTol As System.Integer
Dim value As Gtol
 
value = instance.IGetGTols(NumGTol)
```

```

Gtol IGetGTols( 
   System.int NumGTol
)
```

```

Gtol^ IGetGTols( 
   System.int NumGTol
) 
```

#### Parameters

*NumGTol*
:   Total number of geometric tolerances on this drawing view.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [geometric tolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of geometric tolerances all at once instead of calling [IView::GetFirstGTOL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstGTOL.md) and then repeatedly calling [IGtol::GetNextGTOL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetNextGTOL.md) to obtain the remaining geometric tolerances in the drawing view.

Before calling this method, call [IView::GetGTolCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTolCount.md) to get the value for numGTol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.md)
