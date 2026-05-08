# GetFontUseDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseDimension`

Gets whether the tolerance font is the same size as the dimension font.
Gets whether the tolerance font is the same size as the dimension font.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFontUseDimension() As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim value As System.Boolean
 
value = instance.GetFontUseDimension()
```

```

System.bool GetFontUseDimension()
```

```

System.bool GetFontUseDimension(); 
```

#### Return Value

True if the tolerance font is the same size as the dimension font, false if not

Remarks

To get other tolerance font information, use [IDimensionTolerance::GetFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseScale.md),  
[IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md), and [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md).

To set the tolerance font information, use [IDimensionTolerance::SetFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont.md).

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFitFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFitFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md), [IDimensionTolerance::GetFitFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md), and [IDimensionTolerance::SetFitFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
