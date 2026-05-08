# DeleteGroupByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~DeleteGroupByName`

Deletes the specified face group.
Deletes the specified face group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteGroupByName( _
   ByVal GroupName As System.String _
) As System.Boolean
```

```

Dim instance As ISMNormalCutFeatureData2
Dim GroupName As System.String
Dim value As System.Boolean
 
value = instance.DeleteGroupByName(GroupName)
```

```

System.bool DeleteGroupByName( 
   System.string GroupName
)
```

```

System.bool DeleteGroupByName( 
   System.String^ GroupName
) 
```

#### Parameters

*GroupName*
:   Name of face group to delete

#### Return Value

True if deletion successful, false if not

Remarks

Use [ISMNormalCutFeatureData2::GetGroupNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupNames.md) to populate GroupName.

You cannot delete a group, if it is the only group that exists.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
