# GetNext Method (ICenterLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetNext`

Gets the next centerline in this drawing view.
Gets the next centerline in this [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNext() As Centerline
```

```

Dim instance As ICenterLine
Dim value As Centerline
 
value = instance.GetNext()
```

```

Centerline GetNext()
```

```

Centerline^ GetNext(); 
```

#### Return Value

Next [centerline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md) in this drawing view

Example

[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)  
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)  
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md)  
[ICenterLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine_members.md)  
[IView::GetFirstCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.md)
