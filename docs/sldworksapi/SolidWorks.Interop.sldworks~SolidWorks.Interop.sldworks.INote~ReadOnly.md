# ReadOnly Property (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ReadOnly`

Gets or sets the read-only state of a note.
Gets or sets the read-only state of a note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReadOnly As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.ReadOnly = value
 
value = instance.ReadOnly
```

```

System.bool ReadOnly {get; set;}
```

```

property System.bool ReadOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the note is read-only, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
