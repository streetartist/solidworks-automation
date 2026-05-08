# SecondaryMemberOffsetType Property (ISecondaryMemberUpToMembersFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType`

Gets or sets the distance from end type for this secondary structure system up-to member.
Gets or sets the distance from end type for this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SecondaryMemberOffsetType As System.Integer
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
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

Distance from end type as defined by [swSecondaryMemberUpToMembersDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html)

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
