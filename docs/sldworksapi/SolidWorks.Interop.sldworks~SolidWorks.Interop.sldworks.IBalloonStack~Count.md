# Count Property (IBalloonStack)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Count`

Gets the number of stacked notes in this balloon stack, excluding the master balloon.
Gets the number of stacked notes in this balloon stack, excluding the master balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Count As System.Integer
```

```

Dim instance As IBalloonStack
Dim value As System.Integer
 
value = instance.Count
```

```

System.int Count {get;}
```

```

property System.int Count {
   System.int get();
}
```

#### Property Value

Number of balloons in this balloon stack, excluding the master balloon

Remarks

This property does not count the master balloon in the stack, only the other stacked notes. Us [IBalloonStack::Master](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Master.md) to get the master balloon of the stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)
