# SmartMating Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SmartMating`

Gets or sets SmartMates.
Gets or sets SmartMates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SmartMating As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.SmartMating = value
 
value = instance.SmartMating
```

```

System.bool SmartMating {get; set;}
```

```

property System.bool SmartMating {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

RUE enables SmartMates, false disables it

Remarks

SmartMates is an assembly mating relation that SOLIDWORKS creates automatically.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
