# SetLabel Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetLabel`

Sets the label for this datum tag.
Sets the label for this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

```

Dim instance As IDatumTag
Dim Label As System.String
Dim value As System.Boolean
 
value = instance.SetLabel(Label)
```

```

System.bool SetLabel( 
   System.string Label
)
```

```

System.bool SetLabel( 
   System.String^ Label
) 
```

#### Parameters

*Label*
:   Text string

#### Return Value

True if the label was successfully set, false if not

Remarks

The label can consist of up to two characters. If the specified label is more than two characters long, SOLIDWORKS does not change the symbol and returns false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLabel.md)
