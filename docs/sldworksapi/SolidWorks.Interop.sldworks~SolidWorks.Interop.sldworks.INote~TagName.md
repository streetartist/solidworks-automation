# TagName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TagName`

Gets or sets the tag name for this note.
Gets or sets the tag name for this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TagName As System.String
```

```

Dim instance As INote
Dim value As System.String
 
instance.TagName = value
 
value = instance.TagName
```

```

System.string TagName {get; set;}
```

```

property System.String^ TagName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Tag name

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
