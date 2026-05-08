# ProfileAlignmentObjectType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObjectType`

Gets the type of profile alignment entity.
Gets the type of profile alignment entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ProfileAlignmentObjectType As System.Integer
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer
 
value = instance.ProfileAlignmentObjectType
```

```

System.int ProfileAlignmentObjectType {get;}
```

```

property System.int ProfileAlignmentObjectType {
   System.int get();
}
```

#### Property Value

Profile alignment object type as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelDATUMPLANES
- swSelDATUMAXES
- swSelDATUMLINES
- swSelFACES
- swSelEDGES
- swSelSKETCHSEGS
- swSelSURFACEBODIES

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
