# ThicknessRatioForOffset Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ThicknessRatioForOffset`

Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped.
Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThicknessRatioForOffset As System.Double
```

```

Dim instance As IEndCapFeatureData
Dim value As System.Double
 
instance.ThicknessRatioForOffset = value
 
value = instance.ThicknessRatioForOffset
```

```

System.double ThicknessRatioForOffset {get; set;}
```

```

property System.double ThicknessRatioForOffset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Ratio of the thickness

Remarks

[IEndCapFeatureData::UseThicknessRatioForOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset.md) must be set to true for this property to have an effect.

Example

See the [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.md)  
[IEndCapFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Thickness.md)
