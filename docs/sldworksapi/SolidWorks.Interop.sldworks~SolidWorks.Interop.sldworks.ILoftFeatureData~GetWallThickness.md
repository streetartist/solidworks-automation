# GetWallThickness Method (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness`

Gets the wall thickness in the specified direction for this loft feature.
Gets the wall thickness in the specified direction for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

```

Dim instance As ILoftFeatureData
Dim Forward As System.Boolean
Dim value As System.Double
 
value = instance.GetWallThickness(Forward)
```

```

System.double GetWallThickness( 
   System.bool Forward
)
```

```

System.double GetWallThickness( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True for forward direction, false for reverse

#### Return Value

Wall thickness

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.md)  
[ILoftFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness.md)  
[ILoftFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.md)
