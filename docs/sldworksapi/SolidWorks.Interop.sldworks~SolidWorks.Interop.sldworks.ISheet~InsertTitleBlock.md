# InsertTitleBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertTitleBlock`

Inserts a title block into this drawing sheet.
Inserts a title block into this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTitleBlock( _
   ByVal Notes As System.Object _
) As TitleBlock
```

```

Dim instance As ISheet
Dim Notes As System.Object
Dim value As TitleBlock
 
value = instance.InsertTitleBlock(Notes)
```

```

TitleBlock InsertTitleBlock( 
   System.object Notes
)
```

```

TitleBlock^ InsertTitleBlock( 
   System.Object^ Notes
) 
```

#### Parameters

*Notes*
:   Array of notes or nothing (see **Remarks**)

#### Return Value

[Title block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.md)

Remarks

The Notes parameter can contain one or more more notes or nothing. If the Notes parameter contains a note, or notes, then the note, or notes, is expected to be a Dispatch pointer, or pointers, to the [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object, or objects, to include as part of the title block being created.

Only one title block can exist in a sheet.

Example

[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::TitleBlock Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock.md)
