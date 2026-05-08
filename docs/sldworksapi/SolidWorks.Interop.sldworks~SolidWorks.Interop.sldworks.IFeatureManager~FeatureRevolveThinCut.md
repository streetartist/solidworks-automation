# FeatureRevolveThinCut Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut`

Obsolete. Superseded by IFeatureManager::FeatureRevolve2.
Obsolete. Superseded by [IFeatureManager::FeatureRevolve2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureRevolveThinCut( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThinDir As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ReverseThinDir As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.FeatureRevolveThinCut(Angle, ReverseDir, Angle2, RevType, Thickness1, Thickness2, ReverseThinDir, UseFeatScope, UseAutoSelect)
```

```

Feature FeatureRevolveThinCut( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ FeatureRevolveThinCut( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
) 
```

#### Parameters

*Angle*
:   Angle of revolution in radians

*ReverseDir*
:   True reverses the angle direction, false does not

*Angle2*
:   Angle of revolution in radians

*RevType*
:   Type of revolution as defined in [swRevolveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html) (see **Remarks**)

*Thickness1*
:   Wall thickness1 (ReverseThinDir = 2 uses (thickness1)/2 for each direction)

*Thickness2*
:   Wall thickness 2 (only used when reverseThinDir= 3)

*ReverseThinDir*
:   Type and direction as defined in [swThinWallType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all  
    bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

A constant thickness is given to the profile when revolving.

The ReverseDir argument has no effect if a mid-plane revolution is specified.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FeatureRevolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.md)  
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.md)  
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.md)  
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)
