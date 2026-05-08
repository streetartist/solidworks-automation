# InsertSheetMetal3dBend Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetal3dBend`

Inserts a 3D bend in sheet metal part.
Inserts a 3D bend in sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetal3dBend( _
   ByVal Angle As System.Double, _
   ByVal BUseDefaultRadius As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal BendPos As System.Short, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim BUseDefaultRadius As System.Boolean
Dim Radius As System.Double
Dim FlipDir As System.Boolean
Dim BendPos As System.Short
Dim PCBA As CustomBendAllowance
Dim value As Feature
 
value = instance.InsertSheetMetal3dBend(Angle, BUseDefaultRadius, Radius, FlipDir, BendPos, PCBA)
```

```

Feature InsertSheetMetal3dBend( 
   System.double Angle,
   System.bool BUseDefaultRadius,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos,
   CustomBendAllowance PCBA
)
```

```

Feature^ InsertSheetMetal3dBend( 
   System.double Angle,
   System.bool BUseDefaultRadius,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos,
   CustomBendAllowance^ PCBA
) 
```

#### Parameters

*Angle*
:   Angle of the bend in radians

*BUseDefaultRadius*
:   True to use the default radius, false to use the value specified in radius

*Radius*
:   Value for the radius of the bend if bUseDefaultRadius is false

*FlipDir*
:   True to flip the bend direction, false to not

*BendPos*
:   Bend position:

    - 0 = bend centerline
    - 1 = material inside
    - 2 = material outside
    - 3 = bend outside

*PCBA*
:   |  |  |
    | --- | --- |
    | **If...** | **Then...** |
    | non-NULL | Pointer to [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object for which required values have been set |
    | NULL | Parent bend's bend allowance is used |

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md)
