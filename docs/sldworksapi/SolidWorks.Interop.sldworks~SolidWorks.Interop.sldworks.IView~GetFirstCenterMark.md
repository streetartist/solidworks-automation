# GetFirstCenterMark Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark`

Obsolete. Superseded by IView::GetFirstCenterMark2.
Obsolete. Superseded by [IView::GetFirstCenterMark2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstCenterMark() As CenterMark
```

```

Dim instance As IView
Dim value As CenterMark
 
value = instance.GetFirstCenterMark()
```

```

CenterMark GetFirstCenterMark()
```

```

CenterMark^ GetFirstCenterMark(); 
```

#### Return Value

First [center mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterMarkCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.md)  
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.md)  
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.md)  
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.md)  
[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.md)  
[ICenterMark::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.md)
