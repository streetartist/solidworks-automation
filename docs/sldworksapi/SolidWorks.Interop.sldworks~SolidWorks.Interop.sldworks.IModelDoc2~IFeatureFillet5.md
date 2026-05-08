# IFeatureFillet5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureFillet5`

Obsolete. Superseded by IFeatureManager::FeatureCut.
Obsolete. Superseded by [IFeatureManager::FeatureCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureFillet5( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointRadiusArray As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim PointCount As System.Integer
Dim PointRadiusArray As System.Double
Dim value As System.Integer
 
value = instance.IFeatureFillet5(Options, R1, Ftyp, OverflowType, NRadii, Radii, SetbackDistCount, SetBackDistances, PointCount, PointRadiusArray)
```

```

System.int IFeatureFillet5( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii,
   System.int SetbackDistCount,
   ref System.double SetBackDistances,
   System.int PointCount,
   ref System.double PointRadiusArray
)
```

```

System.int IFeatureFillet5( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii,
   System.int SetbackDistCount,
   System.double% SetBackDistances,
   System.int PointCount,
   System.double% PointRadiusArray
) 
```

#### Parameters

*Options*

*R1*

*Ftyp*
:   v

*OverflowType*
:   v

*NRadii*
:   v

*Radii*
:   v

*SetbackDistCount*
:   v

*SetBackDistances*
:   v

*PointCount*
:   v

*PointRadiusArray*
:   v

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
