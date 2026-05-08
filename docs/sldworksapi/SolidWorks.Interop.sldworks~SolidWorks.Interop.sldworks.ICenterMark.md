# ICenterMark Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark`

Allows access to a center mark or center mark set in a drawing view.
Allows access to a center mark or center mark set in a [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICenterMark 
```

```

Dim instance As ICenterMark
```

```

public interface ICenterMark 
```

```

public interface class ICenterMark 
```

Remarks

Center marks are now annotations. Previously, center marks were features.

Use [ICenterMark::GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetAnnotation.md) to access the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) APIs. If you use [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) or [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md) to retrieve center marks, then these values are returned:

- swSelCENTERMARKSSYMS = 100 for the center marks that are annotations
- swSelCENTERMARKS = 28 for the center marks that are features

Both methods retrieve the ICenterMark object.

|  |  |
| --- | --- |
| **To...** | **Use...** |
| Traverse center marks that are annotations | [IView::GetFirstAnnotation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md), [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md) or [IView::GetFirstCenterMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.md), and [ICenterMark::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.md) |
| Retrieve center marks that are features | [IView::GetCenterMarkCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md) and [IView::GetCenterMarks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md) |

Center marks are displayed using the document's default display attribute settings. If you want the setting to be local to this symbol, then set the [ICenterMark::UseDocDisplaySettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~UseDocDisplaySettings.md) property to false and modify the [ICenterMark::ShowLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ShowLines.md), [ICenterMark::Size](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Size.md), and [ICenterMark::CenterLineFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~CenterLineFont.md) properties as needed.

A center mark set is a linear or circular pattern.

Example

[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)  
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)  
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)  
[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)  
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)  
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.md)
