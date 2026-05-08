# MemberPointParametersType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType`

Gets or sets the point parameter used to create this secondary structure system up-to member.
Gets or sets the point parameter used to create this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MemberPointParametersType As System.Integer
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Integer
 
instance.MemberPointParametersType = value
 
value = instance.MemberPointParametersType
```

```

System.int MemberPointParametersType {get; set;}
```

```

property System.int MemberPointParametersType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Point parameter as defined by [swSecondaryMemberUpToMembersMemberPointParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html)

Remarks

The setter of this method is valid only during creation. As in the user interface, you cannot change the member point parameters type after the secondary structure system member is created.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
