# GetCenterMarks Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks`

Gets all of the center marks that are features in the view.
Gets all of the center marks that are features in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCenterMarks() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetCenterMarks()
```

```

System.object GetCenterMarks()
```

```

System.Object^ GetCenterMarks(); 
```

#### Return Value

[Centermarks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) that are features in this view

Remarks

Center marks are now annotations. Previously, center marks were features. This method returns an empty array for center marks that are annotations; thus, this method is only valid for center marks that are features. See [ICenterMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) for details.

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarkCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md)  
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.md)  
[IView::GetFirstCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.md)  
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.md)  
[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.md)  
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.md)
