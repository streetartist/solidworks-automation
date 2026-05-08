# ConstrainAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll`

Attempts to solve all of the apparent relations in the sketch and returns the number of constraints that were added to the sketch.
Attempts to solve all of the apparent relations in the sketch and returns the number  
of constraints that were added to the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConstrainAll() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.ConstrainAll()
```

```

System.int ConstrainAll()
```

```

System.int ConstrainAll(); 
```

#### Return Value

Number of constraints added

Remarks

f the sketch already has constraints, then no constraints are added (in the same  
way that the user-interface button **Constrain All** can only be pressed once for a sketch.)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetConstrainedStatus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetConstrainedStatus.md)
