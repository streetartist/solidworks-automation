# Length Property (IBalloonStack)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Length`

Gets or sets the number of notes that can be stacked before another row is started.
Gets or sets the number of notes that can be stacked before another row is started.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Length As System.Integer
```

```

Dim instance As IBalloonStack
Dim value As System.Integer
 
instance.Length = value
 
value = instance.Length
```

```

System.int Length {get; set;}
```

```

property System.int Length {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Maximum number of balloons in one row of the stack; valid values are from 2 to 100

Remarks

Valid values are from 2 to 100. If you specify an invalid value for Length, SOLIDWORKS oes not change the balloon stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)
