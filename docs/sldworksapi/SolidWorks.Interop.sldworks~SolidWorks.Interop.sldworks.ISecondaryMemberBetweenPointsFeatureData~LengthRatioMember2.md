# LengthRatioMember2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~LengthRatioMember2`

Gets and sets the length ratio offset from the end of the second member of the primary structure system member pair.
Gets and sets the length ratio offset from the end of the second member of the primary structure system member pair.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LengthRatioMember2 As System.Double
```

```

Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Double
 
instance.LengthRatioMember2 = value
 
value = instance.LengthRatioMember2
```

```

System.double LengthRatioMember2 {get; set;}
```

```

property System.double LengthRatioMember2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= Length ratio offset from the end of the second member <= 1.0

Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.md) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType\_LengthRatio.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md)  
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.md)
