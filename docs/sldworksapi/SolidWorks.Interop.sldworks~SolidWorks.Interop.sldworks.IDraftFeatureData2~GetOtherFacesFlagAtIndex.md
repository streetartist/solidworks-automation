# GetOtherFacesFlagAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetOtherFacesFlagAtIndex`

Gets the value of the Other Face option at the specified index.
Gets the value of the **Other Face** option at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOtherFacesFlagAtIndex( _
   ByVal Index As System.Short _
) As System.Boolean
```

```

Dim instance As IDraftFeatureData2
Dim Index As System.Short
Dim value As System.Boolean
 
value = instance.GetOtherFacesFlagAtIndex(Index)
```

```

System.bool GetOtherFacesFlagAtIndex( 
   System.short Index
)
```

```

System.bool GetOtherFacesFlagAtIndex( 
   System.short Index
) 
```

#### Parameters

*Index*
:   Number indicating a segment of the parting line

#### Return Value

True to specify a different draft direction for each segment of the parting line, false to not

Permissions

| Permission | Description |
| --- | --- |
| **[New Item]** |  |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::SetOtherFacesFlagAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~SetOtherFacesFlagAtIndex.md)
