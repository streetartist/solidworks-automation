# SetNetBlendCurveData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData`

Sets the data for a curve for this boundary feature or boundary surface feature.
Sets the data for a curve for this boundary feature or boundary surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetNetBlendCurveData( _
   ByVal Direction As System.Short, _
   ByVal CurveIndex As System.Short, _
   ByVal TangentType As System.Short, _
   ByVal SignedDraftAngle As System.Double, _
   ByVal SignedTangentLength As System.Double, _
   ByVal TangentLengthApplyAll As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Direction As System.Short
Dim CurveIndex As System.Short
Dim TangentType As System.Short
Dim SignedDraftAngle As System.Double
Dim SignedTangentLength As System.Double
Dim TangentLengthApplyAll As System.Boolean
Dim value As Feature
 
value = instance.SetNetBlendCurveData(Direction, CurveIndex, TangentType, SignedDraftAngle, SignedTangentLength, TangentLengthApplyAll)
```

```

Feature SetNetBlendCurveData( 
   System.short Direction,
   System.short CurveIndex,
   System.short TangentType,
   System.double SignedDraftAngle,
   System.double SignedTangentLength,
   System.bool TangentLengthApplyAll
)
```

```

Feature^ SetNetBlendCurveData( 
   System.short Direction,
   System.short CurveIndex,
   System.short TangentType,
   System.double SignedDraftAngle,
   System.double SignedTangentLength,
   System.bool TangentLengthApplyAll
) 
```

#### Parameters

*Direction*
:   - 0 = Direction 1
    - 1 = Direction 2

*CurveIndex*
:   Index of curve in the specified direction

*TangentType*
:   Type of tangency as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

*SignedDraftAngle*
:   Draft angle

*SignedTangentLength*
:   Tangent length

*TangentLengthApplyAll*
:   True if the tangent length applies to all curves, false if not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

You must use this method to set the data for each curve in a boundary feature or boundary surface feature.

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
[IFeatureManager::SetNetBlendDirectionData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.md)
