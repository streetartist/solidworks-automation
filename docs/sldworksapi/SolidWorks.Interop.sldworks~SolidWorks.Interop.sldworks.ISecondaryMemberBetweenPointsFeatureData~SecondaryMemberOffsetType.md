# SecondaryMemberOffsetType Property (ISecondaryMemberBetweenPointsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType`

Gets and sets the offset type of this secondary structure system member.
Gets and sets the offset type of this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SecondaryMemberOffsetType As System.Integer
```

```

Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Integer
 
instance.SecondaryMemberOffsetType = value
 
value = instance.SecondaryMemberOffsetType
```

```

System.int SecondaryMemberOffsetType {get; set;}
```

```

property System.int SecondaryMemberOffsetType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Offset type as defined by [swSecondaryMemberBetweenPointsDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html)

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md)  
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.md)
