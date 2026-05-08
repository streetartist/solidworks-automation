# IInsertNote Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertNote`

Inserts a note in this document.
Inserts a note in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertNote( _
   ByVal Text As System.String _
) As Note
```

```

Dim instance As IModelDoc2
Dim Text As System.String
Dim value As Note
 
value = instance.IInsertNote(Text)
```

```

Note IInsertNote( 
   System.string Text
)
```

```

Note^ IInsertNote( 
   System.String^ Text
) 
```

#### Parameters

*Text*
:   Text string or symbol for the note (see **Remarks**)

#### Return Value

Newly created [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

If you use a symbol in Text, it must be formatted as:

<*LibraryName-SymbolName*>

where *LibraryName* and *SymbolName* are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym****.**

NOTE: You must include the right- and left-angle brackets and separate *LibraryName* and *SymbolName* with a hyphen; for example, <MOD-DEG>.

The leader attachment points for the new note come from the selections made before calling this method. The initial location of the note will be near the selection location. If there are no selections, the note:

- Does not have a leader
- Is free standing
- Is at the origin of the model or drawing

This method creates a default note. To adjust the display characteristics of this note, you should use the pointer that is returned by this method to access the properties and get and set methods of the Note object, such as [INote::SetBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.md) and [INote::Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Angle.md). Use [INote::GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation.md) or [INote::IGetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation.md) to retrieve the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNote.md)
