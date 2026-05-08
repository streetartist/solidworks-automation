# LockPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition`

Gets and sets whether to anchor this note.
Gets and sets whether to anchor this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LockPosition As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.LockPosition = value
 
value = instance.LockPosition
```

```

System.bool LockPosition {get; set;}
```

```

property System.bool LockPosition {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to anchor the note, false to not

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
[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md)  
[IAnnotation::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.md)  
[INote::GetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.md)
