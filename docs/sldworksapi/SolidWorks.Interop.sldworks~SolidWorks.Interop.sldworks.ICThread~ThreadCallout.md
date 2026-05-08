# ThreadCallout Property (ICThread)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~ThreadCallout`

Gets the note for this cosmetic thread callout in a drawing.
Gets the note for this cosmetic thread callout in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ThreadCallout As Note
```

```

Dim instance As ICThread
Dim value As Note
 
value = instance.ThreadCallout
```

```

Note ThreadCallout {get;}
```

```

property Note^ ThreadCallout {
   Note^ get();
}
```

#### Property Value

Pointer to the [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object for this cosmetic thread callout in a drawing

Remarks

By getting the INote interface, you have access to all of its methods and properties, such as the ability to get or set the text or change the text format.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)  
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.md)
