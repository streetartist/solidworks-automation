# Visible Property (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Visible`

Gets and sets the visibility state of a note during the creation of a block.
Gets and sets the visibility state of a note during the creation of a block.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.Visible = value
 
value = instance.Visible
```

```

System.bool Visible {get; set;}
```

```

property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True makes the note visible in the block, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
