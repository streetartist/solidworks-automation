# ThinFeatureType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType`

Gets or sets the type of thin feature for this boundary feature.
Gets or sets the type of thin feature for this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThinFeatureType As System.Integer
```

```

Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer
 
instance.ThinFeatureType = value
 
value = instance.ThinFeatureType
```

```

System.int ThinFeatureType {get; set;}
```

```

property System.int ThinFeatureType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of thin feature as defined in [swThinWallType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

Remarks

Before calling this property, call [IBoundaryBossFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.md) to determine if the boundary feature is a thin feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::ThinFeatureReversed Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.md)  
[IBoundaryBossFeatureData::ThinFeatureThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.md)
