# SetNetBlendDirectionData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData`

Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature.
Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetNetBlendDirectionData( _
   ByVal Direction As System.Short, _
   ByVal InfluenceType As System.Short, _
   ByVal TrimCurves As System.Short, _
   ByVal BlendClosed As System.Boolean, _
   ByVal SplitSurfaces As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Direction As System.Short
Dim InfluenceType As System.Short
Dim TrimCurves As System.Short
Dim BlendClosed As System.Boolean
Dim SplitSurfaces As System.Boolean
Dim value As Feature
 
value = instance.SetNetBlendDirectionData(Direction, InfluenceType, TrimCurves, BlendClosed, SplitSurfaces)
```

```

Feature SetNetBlendDirectionData( 
   System.short Direction,
   System.short InfluenceType,
   System.short TrimCurves,
   System.bool BlendClosed,
   System.bool SplitSurfaces
)
```

```

Feature^ SetNetBlendDirectionData( 
   System.short Direction,
   System.short InfluenceType,
   System.short TrimCurves,
   System.bool BlendClosed,
   System.bool SplitSurfaces
) 
```

#### Parameters

*Direction*
:   - 0 = Direction 1
    - 1 = Direction 2

*InfluenceType*
:   - 0 = Global
    - 1 = To Next Curve
    - 2 = To Next Sharp
    - 3 = To Next Edge

*TrimCurves*
:   - 0 = False to trim curves
    - 1 = True to trim curves

*BlendClosed*
:   True closes this boundary feature or boundary surface feature, false leaves this boundary feature or boundary surface feature open

*SplitSurfaces*
:   Not used

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Insert Boundary Surface Feature (VBA)](Insert_Boundary_Surface_Feature_Example_VB.htm)  
[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)  
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)  
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertNetBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.md)  
[IFeatureManager::SetNetBlendCurveData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.md)
