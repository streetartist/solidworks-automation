# GetFirstCenterLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine`

Gets the first centerline in this view.
Gets the first centerline in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstCenterLine() As Centerline
```

```

Dim instance As IView
Dim value As Centerline
 
value = instance.GetFirstCenterLine()
```

```

Centerline GetFirstCenterLine()
```

```

Centerline^ GetFirstCenterLine(); 
```

#### Return Value

First [centerline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md)

Example

[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)  
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)  
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCenterLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineSketch.md)  
[ICenterline::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetNext.md)  
[IView::GetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.md)  
[IView::IGetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterLines.md)
