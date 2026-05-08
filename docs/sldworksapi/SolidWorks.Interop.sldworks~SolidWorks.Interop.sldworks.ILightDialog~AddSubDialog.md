# AddSubDialog Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog~AddSubDialog`

Adds a sub-dialog to the lighting dialog.
Adds a sub-dialog to the lighting dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSubDialog( _
   ByVal Page As System.Integer _
) As System.Boolean
```

```

Dim instance As ILightDialog
Dim Page As System.Integer
Dim value As System.Boolean
 
value = instance.AddSubDialog(Page)
```

```

System.bool AddSubDialog( 
   System.int Page
)
```

```

System.bool AddSubDialog( 
   System.int Page
) 
```

#### Parameters

*Page*
:   Pointer to a CDialog object cast to a long

#### Return Value

True if the dialog was successfully added, false if not

Remarks

Currently only one sub-dialog can be added to each dialog.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILightDialog Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog.md)  
[ILightDialog Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog_members.md)
