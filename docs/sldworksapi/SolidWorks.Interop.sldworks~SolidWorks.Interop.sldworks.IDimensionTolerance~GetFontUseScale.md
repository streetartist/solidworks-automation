# GetFontUseScale Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseScale`

Gets whether the tolerance font size is scaled based on the dimension font size, or if it is an absolute height value.
Gets whether the tolerance font size is scaled based on the dimension font size, or if it is an absolute height value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFontUseScale() As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim value As System.Boolean
 
value = instance.GetFontUseScale()
```

```

System.bool GetFontUseScale()
```

```

System.bool GetFontUseScale(); 
```

#### Return Value

True if the tolerance font size is scaled based on the dimension font size, false if the tolerance font size is an absolute height value

Remarks

If [IDimensionTolerance::GetFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.md) is true, then the value returned by this  
IDimensionTolerance::GetFontUseScale is True and the value returned by [IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md)  
is 1.0.

To get other tolerance font information, use the [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md).

To set the tolerance font information, use the [IDimensionTolerance::SetFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont.md) method.

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFitFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFitFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md), [IDimensionTolerance::GetFitFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md), and [IDimensionTolerance::SetFitFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
