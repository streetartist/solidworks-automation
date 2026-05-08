# SetExitConfirmationCursor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetExitConfirmationCursor`

Obsolete. Superseded by IPropertyManagerPage2::SetCursor.
Obsolete. Superseded by [IPropertyManagerPage2::SetCursor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetCursor.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetExitConfirmationCursor( _
   ByVal Enable As System.Boolean _
) 
```

```

Dim instance As IPropertyManagerPage2
Dim Enable As System.Boolean
 
instance.SetExitConfirmationCursor(Enable)
```

```

void SetExitConfirmationCursor( 
   System.bool Enable
)
```

```

void SetExitConfirmationCursor( 
   System.bool Enable
) 
```

#### Parameters

*Enable*
:   True to enable OK cursor, false to not (see **Remarks**)

Remarks

This method should only be used if your PropertyManager page has selection lists. For example, this cursor is displayed in the SOLIDWORKS user-interface when selecting one or more edges to fillet.

After enabling this cursor, you most likely should not disable it; instead, you should let SOLIDWORKS determine when to disable it. SOLIDWORKS disables this cursor when the cursor has moved even just a bit and replaces it with the cursor appropriate for the operation in progress.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
