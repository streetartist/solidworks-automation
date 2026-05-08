# SetMemberPairs Method (ISecondaryMemberSupportPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~SetMemberPairs`

Sets the primary structure system members that pair together to create this secondary structure system member.
Sets the primary structure system members that pair together to create this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMemberPairs( _
   ByVal Pairs As System.Object _
) As System.Boolean
```

```

Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim Pairs As System.Object
Dim value As System.Boolean
 
value = instance.SetMemberPairs(Pairs)
```

```

System.bool SetMemberPairs( 
   System.object Pairs
)
```

```

System.bool SetMemberPairs( 
   System.Object^ Pairs
) 
```

#### Parameters

*Pairs*
:   Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)s

#### Return Value

True if member pairs successfully set, false if not

Remarks

During editing, the array can contain only two objects.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.md)  
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.md)
