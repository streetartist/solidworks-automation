# Stack Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Stack`

Gets the stacked notes in this balloon stack, excluding the master balloon.
Gets the stacked notes in this balloon stack, excluding the master balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Stack As System.Object
```

```

Dim instance As IBalloonStack
Dim value As System.Object
 
value = instance.Stack
```

```

System.object Stack {get;}
```

```

property System.Object^ Stack {
   System.Object^ get();
}
```

#### Property Value

Array notes in the balloon stack

Remarks

This method does not return the master balloon in the stack, only the other stacked notes. Use [IBalloonStack::Master](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Master.md) to get the master balloon of the stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)  
[IBalloonStack::IGetStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~IGetStack.md)
