# Direction Property (IBalloonStack)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Direction`

Gets or sets the direction of this balloon stack.
Gets or sets the direction of this balloon stack.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Direction As System.Integer
```

```

Dim instance As IBalloonStack
Dim value As System.Integer
 
instance.Direction = value
 
value = instance.Direction
```

```

System.int Direction {get; set;}
```

```

property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Balloon stacking direction as defined in [swStackedBalloonDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStackedBalloonDirection_e.html)

Remarks

f you specify an invalid valid for Direction, SOLIDWORKS does not change the balloon stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)
