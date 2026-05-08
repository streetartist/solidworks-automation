# IFeatureFillet4 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureFillet4`

Obsolete. Superseded by IFeatureManager::FeatureCut.
Obsolete. Superseded by [IFeatureManager::FeatureCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureFillet4( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal UniformRadius As System.Boolean, _
   ByVal Ftyp As System.Integer, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByVal UseHelpPoint As System.Boolean, _
   ByVal UseTangentHoldLine As System.Boolean, _
   ByVal CornerType As System.Boolean, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim UniformRadius As System.Boolean
Dim Ftyp As System.Integer
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim UseHelpPoint As System.Boolean
Dim UseTangentHoldLine As System.Boolean
Dim CornerType As System.Boolean
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim value As System.Integer
 
value = instance.IFeatureFillet4(R1, Propagate, UniformRadius, Ftyp, VarRadTyp, OverflowType, NRadii, Radii, UseHelpPoint, UseTangentHoldLine, CornerType, SetbackDistCount, SetBackDistances)
```

```

System.int IFeatureFillet4( 
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   ref System.double SetBackDistances
)
```

```

System.int IFeatureFillet4( 
   System.double R1,
   System.bool Propagate,
   System.bool UniformRadius,
   System.int Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii,
   System.bool UseHelpPoint,
   System.bool UseTangentHoldLine,
   System.bool CornerType,
   System.int SetbackDistCount,
   System.double% SetBackDistances
) 
```

#### Parameters

*R1*

*Propagate*

*UniformRadius*

*Ftyp*

*VarRadTyp*

*OverflowType*

*NRadii*

*Radii*

*UseHelpPoint*

*UseTangentHoldLine*

*CornerType*

*SetbackDistCount*

*SetBackDistances*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
