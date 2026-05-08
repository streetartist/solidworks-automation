# InsertConvertToSheetMetal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConvertToSheetMetal`

Obsolete. Superseded by IFeatureManager::InsertConvertToSheetMetal2.
Obsolete. Superseded by [IFeatureManager::InsertConvertToSheetMetal2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConvertToSheetMetal2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertConvertToSheetMetal( _
   ByVal Thickness As System.Double, _
   ByVal ReverseThickDir As System.Boolean, _
   ByVal FindBends As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal Gap As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefRatio As System.Double _
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
Dim value As System.Boolean
 
value = instance.InsertConvertToSheetMetal(Thickness, ReverseThickDir, FindBends, Radius, Gap, ReliefType, ReliefRatio)
```

```

System.bool InsertConvertToSheetMetal( 
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio
)
```

```

System.bool InsertConvertToSheetMetal( 
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio
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

#### Return Value

True if a Convert-Solid sheet metal feature is created, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
