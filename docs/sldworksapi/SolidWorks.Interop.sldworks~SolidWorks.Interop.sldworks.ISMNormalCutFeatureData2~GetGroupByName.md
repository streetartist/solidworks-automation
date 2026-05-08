# GetGroupByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupByName`

Gets the specified face group.
Gets the specified face group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGroupByName( _
   ByVal GroupName As System.String _
) As System.Object
```

```

Dim instance As ISMNormalCutFeatureData2
Dim GroupName As System.String
Dim value As System.Object
 
value = instance.GetGroupByName(GroupName)
```

```

System.object GetGroupByName( 
   System.string GroupName
)
```

```

System.Object^ GetGroupByName( 
   System.String^ GroupName
) 
```

#### Parameters

*GroupName*
:   Name of face group to retrieve

#### Return Value

[ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.md)

Remarks

Use [ISMNormalCutFeatureData2::GetGroupNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupNames.md) to populate GroupName.

Example

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
