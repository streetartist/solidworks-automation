# GetFirstCenterMark2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark2`

Gets the first center mark in the view.
Gets the first center mark in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstCenterMark2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstCenterMark2()
```

```

System.object GetFirstCenterMark2()
```

```

System.Object^ GetFirstCenterMark2(); 
```

#### Return Value

First [center mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)

Remarks

This method obsoletes IView::GetFirstCenterMark by supporting inactive sheets.

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)  
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)  
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)  
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarkCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md)  
[IView::GetCenterMarkInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.md)  
[IView::GetCenterMarks Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md)  
[ICenterMark::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.md)
