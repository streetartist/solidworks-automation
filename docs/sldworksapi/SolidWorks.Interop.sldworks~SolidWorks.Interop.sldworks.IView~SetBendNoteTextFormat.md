# SetBendNoteTextFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetBendNoteTextFormat`

Sets the text format of all bend notes in this drawing view of a sheet metal part.
Sets the text format of all bend notes in this drawing view of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBendNoteTextFormat( _
   ByVal Format As System.String _
) As System.Boolean
```

```

Dim instance As IView
Dim Format As System.String
Dim value As System.Boolean
 
value = instance.SetBendNoteTextFormat(Format)
```

```

System.bool SetBendNoteTextFormat( 
   System.string Format
)
```

```

System.bool SetBendNoteTextFormat( 
   System.String^ Format
) 
```

#### Parameters

*Format*
:   Format in which to display all bend notes in this drawing view of a sheet metal part (see **Remarks**)

#### Return Value

True if format is successfully set, false if not

Remarks

Before calling this method, call [IView::GetBendNoteAttributeString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteAttributeString.md) to specify Format.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat.md)  
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.md)
