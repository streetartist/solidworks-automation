# FeatureFillet5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureFillet5`

Obsolete. Superseded by IFeatureManager::FeatureFillet.
Obsolete. Superseded by [IFeatureManager::FeatureFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFillet5( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim Radii As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim value As System.Integer
 
value = instance.FeatureFillet5(Options, R1, Ftyp, OverflowType, Radii, SetBackDistances, PointRadiusArray)
```

```

System.int FeatureFillet5( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.object Radii,
   System.object SetBackDistances,
   System.object PointRadiusArray
)
```

```

System.int FeatureFillet5( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.Object^ Radii,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray
) 
```

#### Parameters

*Options*

*R1*

*Ftyp*

*OverflowType*

*Radii*

*SetBackDistances*

*PointRadiusArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
