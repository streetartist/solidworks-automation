# Master Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Master`

Gets the master note in this balloon stack.
Gets the master note in this balloon stack.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Master As Note
```

```

Dim instance As IBalloonStack
Dim value As Note
 
value = instance.Master
```

```

Note Master {get;}
```

```

property Note^ Master {
   Note^ get();
}
```

#### Property Value

Master [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) in this balloon stack

Remarks

Use [IBalloonStack::Stack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Stack.md) or [IBalloonStack::IGetStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~IGetStack.md) to get all of the other balloons in this balloon stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)
