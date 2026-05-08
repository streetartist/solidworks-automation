# BreakCornerType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType`

Gets or sets the type of break corner for the Flat-Pattern feature.
Gets or sets the type of break corner for the Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BreakCornerType As System.Integer
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Integer
 
instance.BreakCornerType = value
 
value = instance.BreakCornerType
```

```

System.int BreakCornerType {get; set;}
```

```

property System.int BreakCornerType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of break corner as defined in [swBreakCornerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::GetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.md)  
[IFlatPatternFeatureData::SetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners.md)  
[IFlatPatternFeatureData::BreakCornerRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.md)
