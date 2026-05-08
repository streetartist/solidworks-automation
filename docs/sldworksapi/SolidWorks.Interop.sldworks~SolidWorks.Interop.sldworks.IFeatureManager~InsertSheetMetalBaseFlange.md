# InsertSheetMetalBaseFlange Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalBaseFlange2.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalBaseFlange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalBaseFlange( _
   ByVal Thickness As System.Double, _
   ByVal ThickenDir As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal ExtrudeDist1 As System.Double, _
   ByVal ExtrudeDist2 As System.Double, _
   ByVal FlipExtruDir As System.Boolean, _
   ByVal EndCondition1 As System.Integer, _
   ByVal EndCondition2 As System.Integer, _
   ByVal DirToUse As System.Integer, _
   ByVal PCBA As CustomBendAllowance, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double, _
   ByVal ReliefRatio As System.Double, _
   ByVal UseReliefRatio As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim ThickenDir As System.Boolean
Dim Radius As System.Double
Dim ExtrudeDist1 As System.Double
Dim ExtrudeDist2 As System.Double
Dim FlipExtruDir As System.Boolean
Dim EndCondition1 As System.Integer
Dim EndCondition2 As System.Integer
Dim DirToUse As System.Integer
Dim PCBA As CustomBendAllowance
Dim UseDefaultRelief As System.Boolean
Dim ReliefType As System.Integer
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim ReliefRatio As System.Double
Dim UseReliefRatio As System.Boolean
Dim value As Feature
 
value = instance.InsertSheetMetalBaseFlange(Thickness, ThickenDir, Radius, ExtrudeDist1, ExtrudeDist2, FlipExtruDir, EndCondition1, EndCondition2, DirToUse, PCBA, UseDefaultRelief, ReliefType, ReliefWidth, ReliefDepth, ReliefRatio, UseReliefRatio)
```

```

Feature InsertSheetMetalBaseFlange( 
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse,
   CustomBendAllowance PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.double ReliefRatio,
   System.bool UseReliefRatio
)
```

```

Feature^ InsertSheetMetalBaseFlange( 
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse,
   CustomBendAllowance^ PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.double ReliefRatio,
   System.bool UseReliefRatio
) 
```

#### Parameters

*Thickness*
:   Wall thickness of the sheet metal feature

*ThickenDir*
:   Direction to thicken the sheet metal

*Radius*
:   Global bend radius to insert at the corners

*ExtrudeDist1*
:   Distance of the sheet metal extrusion for the Direction 1

*ExtrudeDist2*
:   Distance of the sheet metal extrusion for the Direction 2

*FlipExtruDir*
:   True to reverse the direction of the extrude, false to not

*EndCondition1*
:   End condition for first extrude distance

*EndCondition2*
:   End condition for second extrude distance

*DirToUse*
:   End condition type as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*PCBA*
:   Pointer to the [custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object

*UseDefaultRelief*
:   True to use the default relief, false to not

*ReliefType*
:   Relief type as defined in [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

*ReliefWidth*
:   Width of the relief

*ReliefDepth*
:   Depth of the relief

*ReliefRatio*
:   Value for the relief ratio

*UseReliefRatio*
:   True to use the relief ratio, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
