# GetAttachPos Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos`

Gets the attachment point of this note.
Gets the attachment point of this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachPos() As System.Object
```

```

Dim instance As INote
Dim value As System.Object
 
value = instance.GetAttachPos()
```

```

System.object GetAttachPos()
```

```

System.Object^ GetAttachPos(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This is only meaningful if the note is attached.

Format of return information is the following array of doubles:

- return value[0] = x-coord of attachment point
- return value[1] = y-coord of attachment point
- return value[2] = z-coord of attachment point

Example

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAttachPos.md)  
[INote::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.md)  
[INote::LockPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.md)
