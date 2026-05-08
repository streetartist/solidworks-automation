# InsertConvertToSheetMetal2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConvertToSheetMetal2`

Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature.
Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertConvertToSheetMetal2( _
   ByVal Thickness As System.Double, _
   ByVal ReverseThickDir As System.Boolean, _
   ByVal FindBends As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal Gap As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefRatio As System.Double, _
   ByVal OverlapType As System.Integer, _
   ByVal OverlapRatio As System.Double, _
   ByVal KeepBody As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim ReverseThickDir As System.Boolean
Dim FindBends As System.Boolean
Dim Radius As System.Double
Dim Gap As System.Double
Dim ReliefType As System.Integer
Dim ReliefRatio As System.Double
Dim OverlapType As System.Integer
Dim OverlapRatio As System.Double
Dim KeepBody As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertConvertToSheetMetal2(Thickness, ReverseThickDir, FindBends, Radius, Gap, ReliefType, ReliefRatio, OverlapType, OverlapRatio, KeepBody)
```

```

System.bool InsertConvertToSheetMetal2( 
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio,
   System.int OverlapType,
   System.double OverlapRatio,
   System.bool KeepBody
)
```

```

System.bool InsertConvertToSheetMetal2( 
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio,
   System.int OverlapType,
   System.double OverlapRatio,
   System.bool KeepBody
) 
```

#### Parameters

*Thickness*
:   Sheet thickness

*ReverseThickDir*
:   True to reverse the direction of the sheet thickness, false to not

*FindBends*
:   True to find pre-made bends and part thickness, false to not

*Radius*
:   Radius for the bends

*Gap*
:   Gap for all rips

*ReliefType*
:   Relief type as defined by [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

*ReliefRatio*
:   Relief ratio

*OverlapType*
:   Overlap type for all rips

    - 1=Open butt
    - 2=Overlap
    - 3=Underlap

*OverlapRatio*
:   Overlap ratio for all rips

*KeepBody*
:   True to keep bodies, false to not

#### Return Value

True if a Convert-Solid sheet metal feature is created, false if not

Remarks

Read the SOLIDWORKS Help to learn more about converting to sheet metal.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
