# SetLabel Method (IProjectionArrow)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~SetLabel`

Sets the label for this view's projection arrow.
Sets the label for this view's projection arrow.

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

Dim instance As IProjectionArrow
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
:   Label for this projection arrow

#### Return Value

True if setting the label is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.md)  
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.md)  
[IProjectionArrow::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetLabel.md)
