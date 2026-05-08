# FitDisplayStyle Property (IDimensionTolerance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle`

Gets or sets how this dimension fit tolerance is displayed.
Gets or sets how this dimension fit tolerance is displayed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FitDisplayStyle As System.Integer
```

```

Dim instance As IDimensionTolerance
Dim value As System.Integer
 
instance.FitDisplayStyle = value
 
value = instance.FitDisplayStyle
```

```

System.int FitDisplayStyle {get; set;}
```

```

property System.int FitDisplayStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fit tolerance display style as defined in [swFitTolDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFitTolDisplay_e.html)

Remarks

Use [ICalloutVariable::FitDisplayStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitDisplayStyle.md) for multiple callouts in a display dimension for a hole.

To see the effects of changing the fit tolerance display style, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)  
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.md)  
[IDimensionTolerance::GetFitFontHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md)  
[IDimensionTolerance::GetFitFontScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md)  
[IDimensionTolerance::GetFitFontUseDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md)  
[IDimensionTolerance::GetFitFontUseScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md)  
[IDimensionTolerance::GetHoleFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.md)  
[IDimensionTolerance::GetShaftFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.md)  
[IDimensionTolerance::SetFitFont Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.md)  
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.md)
