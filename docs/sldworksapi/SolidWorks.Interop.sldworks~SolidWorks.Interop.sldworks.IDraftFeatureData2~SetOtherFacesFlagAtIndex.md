# SetOtherFacesFlagAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~SetOtherFacesFlagAtIndex`

Sets the Other Face option.
Sets the **Other Face** option.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetOtherFacesFlagAtIndex( _
   ByVal Index As System.Short, _
   ByVal Flag As System.Boolean _
) 
```

```

Dim instance As IDraftFeatureData2
Dim Index As System.Short
Dim Flag As System.Boolean
 
instance.SetOtherFacesFlagAtIndex(Index, Flag)
```

```

void SetOtherFacesFlagAtIndex( 
   System.short Index,
   System.bool Flag
)
```

```

void SetOtherFacesFlagAtIndex( 
   System.short Index,
   System.bool Flag
) 
```

#### Parameters

*Index*
:   Number indicating a segment of the parting line

*Flag*
:   True to specify a different draft direction for each segment of the parting line,  
    false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::GetOtherFacesFlagAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetOtherFacesFlagAtIndex.md)
