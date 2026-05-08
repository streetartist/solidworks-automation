# SetCursor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetCursor`

Sets the cursor after a selection is made in the SOLIDWORKS graphics area.
Sets the cursor after a selection is made in the SOLIDWORKS graphics area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCursor( _
   ByVal Mode As System.Integer _
) 
```

```

Dim instance As IPropertyManagerPage2
Dim Mode As System.Integer
 
instance.SetCursor(Mode)
```

```

void SetCursor( 
   System.int Mode
)
```

```

void SetCursor( 
   System.int Mode
) 
```

#### Parameters

*Mode*
:   Cursor as defined by [swPropertyManagerPageCursors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageCursors_e.html)

Remarks

Calling this method in [IPropertyManagerPage2Hander8::OnSelectionboxListChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxListChanged.md) enables the right-mouse button and cursor and allows an interactive user to:

- move to the next selection box on the PropertyManager page
- okay and close a PropertyManager page

after making a selection in the SOLIDWORKS graphics area.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
