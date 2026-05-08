# FeatureRevolve Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve`

Obsolete. Superseded by IFeatureManager::FeatureRevolve2.
Obsolete. Superseded by [IFeatureManager::FeatureRevolve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureRevolve( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSel As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Options As System.Integer
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSel As System.Boolean
Dim value As Feature
 
value = instance.FeatureRevolve(Angle, ReverseDir, Angle2, RevType, Options, Merge, UseFeatScope, UseAutoSel)
```

```

Feature FeatureRevolve( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSel
)
```

```

Feature^ FeatureRevolve( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSel
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
:   Type of revolution as defined in [swRevolveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html)

*Options*
:   Additional control as defined in [swRevolveOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveOptions_e.html)

*Merge*
:   True to merge the results in a multibody part, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSel*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies or components the feature affects (see **Remarks**)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

To select an axis for a revolve feature, first call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark set to 4. When UseAutoSel is false, the user must select the bodies  or components that the feature will affect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.md)  
[IFeatureManager::FeatureRevolveThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.md)  
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.md)
