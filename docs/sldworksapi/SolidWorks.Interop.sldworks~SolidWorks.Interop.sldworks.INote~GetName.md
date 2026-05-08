# GetName Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetName`

Gets the name of this note.
Gets the name of this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetName() As System.String
```

```

Dim instance As INote
Dim value As System.String
 
value = instance.GetName()
```

```

System.string GetName()
```

```

System.String^ GetName(); 
```

#### Return Value

Name of the note

Remarks

This method returns an empty string if the note is part of a block.

Example

[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)  
[Get Note By Name (VBA)](Get_Note_By_Name_Example_VB.htm)  
[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)  
[Set Note Name (VBA)](Set_Note_Name_Example.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetName.md)
