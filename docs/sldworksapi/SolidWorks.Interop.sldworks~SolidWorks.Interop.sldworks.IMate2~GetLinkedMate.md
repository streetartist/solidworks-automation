# GetLinkedMate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetLinkedMate`

Gets the linked mate of this concentric mate.
Gets the linked mate of this concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLinkedMate() As System.Object
```

```

Dim instance As IMate2
Dim value As System.Object
 
value = instance.GetLinkedMate()
```

```

System.object GetLinkedMate()
```

```

System.Object^ GetLinkedMate(); 
```

#### Return Value

[Mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

This mate and its linked mate are siblings in a Hole Set, which is defined as two concentric mates between the same two components.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
