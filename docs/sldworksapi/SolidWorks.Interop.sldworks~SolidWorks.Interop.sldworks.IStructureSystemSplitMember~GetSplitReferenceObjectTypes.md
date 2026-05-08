# GetSplitReferenceObjectTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~GetSplitReferenceObjectTypes`

Gets the types of split member references.
Gets the types of split member references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplitReferenceObjectTypes() As System.Object
```

```

Dim instance As IStructureSystemSplitMember
Dim value As System.Object
 
value = instance.GetSplitReferenceObjectTypes()
```

```

System.object GetSplitReferenceObjectTypes()
```

```

System.Object^ GetSplitReferenceObjectTypes(); 
```

#### Return Value

Array of types of split member references as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelFACES
- swSelDATUMPLANES
- swSelADVSTRUCTMEMBER

Remarks

This method is valid only if [IStructureSystemSplitMember::MemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.md) is set to [swStructureSplitMemberType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html).swStructureSplitMember\_Reference.

The array returned by this method maps one-to-one and onto with the array returned by [IStructureSystemSplitMember::GetSplitReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~GetSplitReferences.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.md)  
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.md)
