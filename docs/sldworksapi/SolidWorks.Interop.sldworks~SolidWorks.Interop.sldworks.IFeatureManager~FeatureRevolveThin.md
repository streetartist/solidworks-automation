# FeatureRevolveThin Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin`

Obsolete. Superseded by IFeatureManager::FeatureRevolve2.
Obsolete. Superseded by [IFeatureManager::FeatureRevolve2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureRevolveThin( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThinDir As System.Integer, _
   ByVal Merge As System.Boolean, _
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
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature
 
value = instance.FeatureRevolveThin(Angle, ReverseDir, Angle2, RevType, Thickness1, Thickness2, ReverseThinDir, Merge, UseFeatScope, UseAutoSelect)
```

```

Feature FeatureRevolveThin( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

```

Feature^ FeatureRevolveThin( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge,
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
:   Wall thickness (ReverseThinDir = 2 uses (Thickness1)/2 for each direction)

*Thickness2*
:   Wall thickness; use only ReverseThinDir=2

*ReverseThinDir*
:   Type and direction as defined in [swThinWallType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

*Merge*
:   True to merge the results in a multibody part, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

The ReverseDir argument has no effect if a mid-plane revolution is specified.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

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
