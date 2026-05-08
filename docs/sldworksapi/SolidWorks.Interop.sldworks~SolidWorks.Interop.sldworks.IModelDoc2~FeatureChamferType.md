# FeatureChamferType Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamferType`

Obsolete. Superseded by IFeatureManager::InsertFeatureChamfer.
Obsolete. Superseded by [IFeatureManager::InsertFeatureChamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureChamfer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureChamferType( _
   ByVal ChamferType As System.Short, _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean, _
   ByVal OtherDist As System.Double, _
   ByVal VertexChamDist1 As System.Double, _
   ByVal VertexChamDist2 As System.Double, _
   ByVal VertexChamDist3 As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim ChamferType As System.Short
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean
Dim OtherDist As System.Double
Dim VertexChamDist1 As System.Double
Dim VertexChamDist2 As System.Double
Dim VertexChamDist3 As System.Double
 
instance.FeatureChamferType(ChamferType, Width, Angle, Flip, OtherDist, VertexChamDist1, VertexChamDist2, VertexChamDist3)
```

```

void FeatureChamferType( 
   System.short ChamferType,
   System.double Width,
   System.double Angle,
   System.bool Flip,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

```

void FeatureChamferType( 
   System.short ChamferType,
   System.double Width,
   System.double Angle,
   System.bool Flip,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
) 
```

#### Parameters

*ChamferType*

*Width*

*Angle*

*Flip*

*OtherDist*

*VertexChamDist1*

*VertexChamDist2*

*VertexChamDist3*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
