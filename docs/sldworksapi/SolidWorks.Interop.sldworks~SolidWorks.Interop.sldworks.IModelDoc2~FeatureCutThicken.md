# FeatureCutThicken Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCutThicken`

Obsolete. Superseded by IFeatureManager::FeatureCutThicken.
Obsolete. Superseded by [IFeatureManager::FeatureCutThicken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThicken.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureCutThicken( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
 
instance.FeatureCutThicken(Thickness, Direction, FaceIndex)
```

```

void FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
)
```

```

void FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
) 
```

#### Parameters

*Thickness*

*Direction*

*FaceIndex*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
