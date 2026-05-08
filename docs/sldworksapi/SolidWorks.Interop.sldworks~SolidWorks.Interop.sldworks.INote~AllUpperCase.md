# AllUpperCase Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AllUpperCase`

Gets or sets whether the text of this note is all uppercase.
Gets or sets whether the text of this note is all uppercase.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllUpperCase As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.AllUpperCase = value
 
value = instance.AllUpperCase
```

```

System.bool AllUpperCase {get; set;}
```

```

property System.bool AllUpperCase {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the text of this note is all uppercase, false if not

Example

[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)  
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)  
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
