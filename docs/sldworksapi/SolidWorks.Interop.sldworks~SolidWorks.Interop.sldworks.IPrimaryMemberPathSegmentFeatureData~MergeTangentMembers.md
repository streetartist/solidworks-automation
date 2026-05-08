# MergeTangentMembers Property (IPrimaryMemberPathSegmentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~MergeTangentMembers`

Gets and sets whether to merge tangential members.
Gets and sets whether to merge tangential members.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MergeTangentMembers As System.Boolean
```

```

Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim value As System.Boolean
 
instance.MergeTangentMembers = value
 
value = instance.MergeTangentMembers
```

```

System.bool MergeTangentMembers {get; set;}
```

```

property System.bool MergeTangentMembers {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge tangential members, false to not

Remarks

This property is valid only when creating the structure system path segment member.

Example

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md)  
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.md)
