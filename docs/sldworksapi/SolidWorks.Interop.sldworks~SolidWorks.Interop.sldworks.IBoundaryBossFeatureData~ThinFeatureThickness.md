# ThinFeatureThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness`

Gets or sets the thickness of this thin feature boundary feature.
Gets or sets the thickness of this thin feature boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThinFeatureThickness( _
   ByVal ThicknessDirection As System.Boolean _
) As System.Double
```

```

Dim instance As IBoundaryBossFeatureData
Dim ThicknessDirection As System.Boolean
Dim value As System.Double
 
instance.ThinFeatureThickness(ThicknessDirection) = value
 
value = instance.ThinFeatureThickness(ThicknessDirection)
```

```

System.double ThinFeatureThickness( 
   System.bool ThicknessDirection
) {get; set;}
```

```

property System.double ThinFeatureThickness {
   System.double get(System.bool ThicknessDirection);
   void set (System.bool ThicknessDirection, System.double value);
}
```

#### Parameters

*ThicknessDirection*
:   Direction of thickness as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

#### Property Value

Thickness of this thin feature boundary feature

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
[IBoundaryBossFeatureData::ThinFeatureType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.md)
