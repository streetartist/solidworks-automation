# IGetCenterMarks Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks`

Gets all of the center marks that are features in the view.
Gets all of the center marks that are features in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCenterMarks( _
   ByVal Count As System.Integer _
) As CenterMark
```

```

Dim instance As IView
Dim Count As System.Integer
Dim value As CenterMark
 
value = instance.IGetCenterMarks(Count)
```

```

CenterMark IGetCenterMarks( 
   System.int Count
)
```

```

CenterMark^ IGetCenterMarks( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of center marks that are features in the view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [centermarks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) that are features in this view
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetCenterMarkCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md) to get the value for Count.

Center marks are now annotations. Previously, center marks were features. This method returns an empty array for center marks that are annotations; thus, this method is only valid for center marks that are features. See [ICenterMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.md)  
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md)  
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.md)  
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.md)
