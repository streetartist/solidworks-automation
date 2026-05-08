# IGetNext Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext`

Gets the next loop in the face.
Gets the next loop in the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNext() As Loop2
```

```

Dim instance As ILoop2
Dim value As Loop2
 
value = instance.IGetNext()
```

```

Loop2 IGetNext()
```

```

Loop2^ IGetNext(); 
```

#### Return Value

Next [loop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) on the face, or NULL if it is the last loop

Remarks

See [ILoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) accessors for a list of methods and properties that return loops.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.md)
