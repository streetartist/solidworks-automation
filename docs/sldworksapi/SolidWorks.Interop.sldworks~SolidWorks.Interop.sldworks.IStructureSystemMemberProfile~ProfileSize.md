# ProfileSize Property (IStructureSystemMemberProfile)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileSize`

Gets the profile size for this member profile.
Gets the profile size for this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileSize As System.String
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.String
 
instance.ProfileSize = value
 
value = instance.ProfileSize
```

```

System.string ProfileSize {get; set;}
```

```

property System.String^ ProfileSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Weldment profile size as defined in a weldment profile

Remarks

This property:

- is valid only if a [IStructureSystemMemberProfile::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileType.md) is set.
- overrides [IProfileGroupFolder::ProfileSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileSize.md).

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (\*.**sldlfp**) from *install\_dir*\**lang**\*lang\_name*\**weldment profiles  
  -** or -
- custom weldment profile (\*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
