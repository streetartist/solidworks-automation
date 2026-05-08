# SetSplitReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~SetSplitReferences`

Sets the split member references.
Sets the split member references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSplitReferences( _
   ByVal References As System.Object _
) As System.Boolean
```

```

Dim instance As IStructureSystemSplitMember
Dim References As System.Object
Dim value As System.Boolean
 
value = instance.SetSplitReferences(References)
```

```

System.bool SetSplitReferences( 
   System.object References
)
```

```

System.bool SetSplitReferences( 
   System.Object^ References
) 
```

#### Parameters

*References*
:   Array of split member references, e.g.:

    - Face2
    - IRefPlane
    - Member

#### Return Value

True if split member references successfully set, false if not

Remarks

This method is valid only if [IStructureSystemSplitMember::MemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.md) is set to [swStructureSplitMemberType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html).swStructureSplitMember\_Reference.

Example

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.md)  
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.md)
