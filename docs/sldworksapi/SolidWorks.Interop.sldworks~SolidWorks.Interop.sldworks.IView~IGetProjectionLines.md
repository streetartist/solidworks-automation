# IGetProjectionLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines`

Gets the projection lines (arrows) in this drawing view.
Gets the projection lines (arrows) in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetProjectionLines( _
   ByVal Count As System.Integer _
) As ProjectionArrow
```

```

Dim instance As IView
Dim Count As System.Integer
Dim value As ProjectionArrow
 
value = instance.IGetProjectionLines(Count)
```

```

ProjectionArrow IGetProjectionLines( 
   System.int Count
)
```

```

ProjectionArrow^ IGetProjectionLines( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of projection lines

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [projection lines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

This method only works for base drawing views; it does not work for projected or auxiliary views.

Multiple projection lines can exist in a view. This method returns the interface for each projection line so that an application such as DXF/DWG translation can create the projection lines with the base drawing view rather than creating those lines when cycling through the views and finding a projected or auxiliary view.

Before calling this method, call [IView::GetProjectionLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.md)  
[IView::GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.md)  
[IView::GetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.md)  
[IView::IGetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.md)  
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.md)
