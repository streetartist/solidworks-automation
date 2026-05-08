# InsertSheetMetalHem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2`

Inserts a hem of the specified relief type at the selected edges of the current sheet metal part.
Inserts a hem of the specified relief type at the selected edges of the current sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalHem2( _
   ByVal Type As System.Integer, _
   ByVal Position As System.Integer, _
   ByVal Reverse As System.Boolean, _
   ByVal DLength As System.Double, _
   ByVal DGap As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal DRad As System.Double, _
   ByVal DMiterGap As System.Double, _
   ByVal PCBA As CustomBendAllowance, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefTearTypes As System.Integer, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Position As System.Integer
Dim Reverse As System.Boolean
Dim DLength As System.Double
Dim DGap As System.Double
Dim DAngle As System.Double
Dim DRad As System.Double
Dim DMiterGap As System.Double
Dim PCBA As CustomBendAllowance
Dim UseDefaultRelief As System.Boolean
Dim ReliefType As System.Integer
Dim ReliefTearTypes As System.Integer
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim value As Feature
 
value = instance.InsertSheetMetalHem2(Type, Position, Reverse, DLength, DGap, DAngle, DRad, DMiterGap, PCBA, UseDefaultRelief, ReliefType, ReliefTearTypes, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth)
```

```

Feature InsertSheetMetalHem2( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.int ReliefTearTypes,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

```

Feature^ InsertSheetMetalHem2( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance^ PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.int ReliefTearTypes,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
) 
```

#### Parameters

*Type*
:   Type as defined in [swHemTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemTypes_e.html)

*Position*
:   Position as defined in [swHemPositionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemPositionTypes_e.html)

*Reverse*
:   True reverses the direction, false does not

*DLength*
:   Hem length; valid only for open or closed hems

*DGap*
:   Gap distance; valid only for open hems

*DAngle*
:   Hem angle; valid only for tear-drop or rolled hems

*DRad*
:   Hem radius; valid only for tear-drop or rolled hems

*DMiterGap*
:   Hem miter gap

*PCBA*
:   |  |  |
    | --- | --- |
    | **If...** | **Then...** |
    | non-NULL | Pointer to [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object for which required values have been set |
    | NULL | Parent bend's bend allowance is used |

*UseDefaultRelief*
:   True to use the default relief, false to use the relief specified by ReliefType

*ReliefType*
:   Type of relief as defined in [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid only if UseDefaultRelief is false

*ReliefTearTypes*
:   Type of relief tear as defined in  [swReliefTearTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReliefTearTypes_e.html); valid only when:

    - UseDefaultRelief is false

        - and -

    - ReliefType is [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefTear

*UseReliefRatio*
:   True to use ReliefRatio, false to use ReliefWidth/ReliefDepth; valid only when:

    - UseDefaultRelief is false

        - and -

    - ReliefType is either [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular

*ReliefRatio*
:   Relief ratio; valid only when:

    - UseDefaultRelief is false

        - and -

    - UseReliefRatio is true

        - and -

    - ReliefType is either [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular

*ReliefWidth*
:   Width of the relief; valid only when:

    - UseDefaultRelief is false

        - and -

    - UseReliefRatio is false

        - and -

    - ReliefType is either [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular

*ReliefDepth*
:   Depth of the relief; valid only when:

    - UseDefaultRelief is false

        - and -

    - UseReliefRatio is false

        - and -

    - ReliefType is either [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method:

1. Call [IFeatureManager::CreateCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCustomBendAllowance.md) to create an instance of ICustomBendAllowance.
2. Initialize the CustomBendAllowance object.
3. Assign PCBA to the initialized CustomBendAllowance object.
4. Select one or more edges in the sheet metal model to which to add the specified hem.

Example

[Insert Sheet Metal Hem (VBA)](Insert_Sheet_Metal_Hem_Example_VB.htm)  
[Insert Sheet Metal Hem (VB.NET)](Insert_Sheet_Metal_Hem_Example_VBNET.htm)  
[Insert Sheet Metal Hem (C#)](Insert_Sheet_Metal_Hem_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
