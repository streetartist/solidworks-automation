# FeatureBossThicken2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureBossThicken2`

Obsolete. Superseded by IFeatureManager::FeatureBossThicken.
Obsolete. Superseded by [IFeatureManager::FeatureBossThicken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureBossThicken.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureBossThicken2( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer, _
   ByVal FillVolume As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
Dim FillVolume As System.Boolean
 
instance.FeatureBossThicken2(Thickness, Direction, FaceIndex, FillVolume)
```

```

void FeatureBossThicken2( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume
)
```

```

void FeatureBossThicken2( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex,
   System.bool FillVolume
) 
```

#### Parameters

*Thickness*

*Direction*

*FaceIndex*

*FillVolume*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
