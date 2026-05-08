# CornerTreatment Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTreatment`

Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature.
Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CornerTreatment As System.Boolean
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean
 
instance.CornerTreatment = value
 
value = instance.CornerTreatment
```

```

System.bool CornerTreatment {get; set;}
```

```

property System.bool CornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply smooth edges, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.md)
