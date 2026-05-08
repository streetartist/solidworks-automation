# InsertSheetMetalMiterFlange Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalMiterFlange`

Inserts a meter flange in a sheet metal part.
Inserts a meter flange in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalMiterFlange( _
   ByVal UseDefaultRadius As System.Boolean, _
   ByVal GlobalRadius As System.Double, _
   ByVal RipGap As System.Double, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal TrimSideBends As System.Boolean, _
   ByVal FlangePos As System.Integer, _
   ByVal OffsetDist1 As System.Double, _
   ByVal OffsetDist2 As System.Double, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

```

Dim instance As IFeatureManager
Dim UseDefaultRadius As System.Boolean
Dim GlobalRadius As System.Double
Dim RipGap As System.Double
Dim UseDefaultRelief As System.Boolean
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim ReliefType As System.Integer
Dim TrimSideBends As System.Boolean
Dim FlangePos As System.Integer
Dim OffsetDist1 As System.Double
Dim OffsetDist2 As System.Double
Dim PCBA As CustomBendAllowance
Dim value As Feature
 
value = instance.InsertSheetMetalMiterFlange(UseDefaultRadius, GlobalRadius, RipGap, UseDefaultRelief, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth, ReliefType, TrimSideBends, FlangePos, OffsetDist1, OffsetDist2, PCBA)
```

```

Feature InsertSheetMetalMiterFlange( 
   System.bool UseDefaultRadius,
   System.double GlobalRadius,
   System.double RipGap,
   System.bool UseDefaultRelief,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.int ReliefType,
   System.bool TrimSideBends,
   System.int FlangePos,
   System.double OffsetDist1,
   System.double OffsetDist2,
   CustomBendAllowance PCBA
)
```

```

Feature^ InsertSheetMetalMiterFlange( 
   System.bool UseDefaultRadius,
   System.double GlobalRadius,
   System.double RipGap,
   System.bool UseDefaultRelief,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.int ReliefType,
   System.bool TrimSideBends,
   System.int FlangePos,
   System.double OffsetDist1,
   System.double OffsetDist2,
   CustomBendAllowance^ PCBA
) 
```

#### Parameters

*UseDefaultRadius*
:   True to use default bend radius, false to use GlobalRadius

*GlobalRadius*
:   Global bend radius

*RipGap*
:   Rip-gap distance

*UseDefaultRelief*
:   True to use parent bend's ratio, false to not

*UseReliefRatio*
:   True to use custom relief ratio, false to not

*ReliefRatio*
:   If useReliefRatio is True, then specify relief ratio

*ReliefWidth*
:   If UseReliefRatio is True and ReliefType is swSheetMetalReliefRectangular or swSheetMetalReliefObround, then specify relief depth

*ReliefDepth*
:   If UseReliefRatio is True and ReliefType is swSheetMetalReliefRectangular or swSheetMetalReliefObround, then specify relief depth

*ReliefType*
:   Relief type as defined by [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid selections:

    - swSheetMetalRelievObround
    - swSheetMetalReliefRectangular
    - swSheetMetalReliefTear

*TrimSideBends*
:   True to trim side bends, false to not

*FlangePos*
:   Flange position as defined by [swFlangePositionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html); valid selections:

    - swFlangePositionTypeMaterialInside
    - swFlangePositionTypeMaterialOutside
    - swFlangePositionTypeBendOutside

*OffsetDist1*
:   Starting offset distance if partial flange

*OffsetDist2*
:   Ending offset distance if partial flange

*PCBA*
:   |  |  |
    | --- | --- |
    | **If...** | **Then...** |
    | non-NULL | Pointer to [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object for which required values have been set |
    | NULL | Parent bend's bend allowance is used |

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object or NULL

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
