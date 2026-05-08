# InsertSheetMetalHem Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalHem2.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalHem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalHem( _
   ByVal Type As System.Integer, _
   ByVal Position As System.Integer, _
   ByVal Reverse As System.Boolean, _
   ByVal DLength As System.Double, _
   ByVal DGap As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal DRad As System.Double, _
   ByVal DMiterGap As System.Double, _
   ByVal PCBA As CustomBendAllowance _
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
Dim value As Feature
 
value = instance.InsertSheetMetalHem(Type, Position, Reverse, DLength, DGap, DAngle, DRad, DMiterGap, PCBA)
```

```

Feature InsertSheetMetalHem( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance PCBA
)
```

```

Feature^ InsertSheetMetalHem( 
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance^ PCBA
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

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
