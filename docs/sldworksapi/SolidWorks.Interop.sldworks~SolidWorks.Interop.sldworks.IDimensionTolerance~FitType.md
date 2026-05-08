# FitType Property (IDimensionTolerance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType`

Gets or sets the fit type for this dimension fit tolerance.
Gets or sets the fit type for this dimension fit tolerance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FitType As System.Integer
```

```

Dim instance As IDimensionTolerance
Dim value As System.Integer
 
instance.FitType = value
 
value = instance.FitType
```

```

System.int FitType {get; set;}
```

```

property System.int FitType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fit type as defined in [swFitType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFitType_e.html)

Remarks

This property is only available when the [type of tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md) is [swTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html):

- swTolFIT,
- swTolFITTOLONLY, or
- swTolFITWITHTOL.

Example

[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)  
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)  
[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)  
[IDimensionTolerance::GetFitFontHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md)  
[IDimensionTolerance::GetFitFontScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md)  
[IDimensionTolerance::GetFitFontUseDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md)  
[IDimensionTolerance::GetFitFontUseScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md)  
[IDimensionTolerance::GetHoleFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.md)  
[IDimensionTolerance::GetShaftFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.md)  
[IDimensionTolerance::SetFitFont Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.md)  
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.md)  
[IDimensionTolerance::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.md)
