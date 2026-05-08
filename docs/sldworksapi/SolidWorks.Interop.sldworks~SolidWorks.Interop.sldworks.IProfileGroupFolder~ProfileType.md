# ProfileType Property (IProfileGroupFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileType`

Gets the profile type for this member profile group.
Gets the profile type for this member profile group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ProfileType As System.String
```

```

Dim instance As IProfileGroupFolder
Dim value As System.String
 
value = instance.ProfileType
```

```

System.string ProfileType {get;}
```

```

property System.String^ ProfileType {
   System.String^ get();
}
```

#### Property Value

Weldment profile type as defined in a weldment profile

Remarks

This property:

- is valid only if a [IProfileGroupFolder::ProfileStandard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileStandard.md) is set.
- may be overridden by [IStructureSystemMemberProfile::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileType.md) for individual members.

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (\*.**sldlfp**) from *install\_dir*\**lang**\*lang\_name*\**weldment profiles  
  -** or -
- custom weldment profile (\*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.md)  
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.md)
