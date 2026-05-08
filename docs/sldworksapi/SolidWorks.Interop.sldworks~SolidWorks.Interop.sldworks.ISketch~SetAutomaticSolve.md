# SetAutomaticSolve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetAutomaticSolve`

Controls whether the computation to solve the sketch geometry of the part as modifications are automatically performed.
Controls whether the computation to solve the sketch geometry of the part as modifications are automatically performed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAutomaticSolve( _
   ByVal SolveFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketch
Dim SolveFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.SetAutomaticSolve(SolveFlag)
```

```

System.bool SetAutomaticSolve( 
   System.bool SolveFlag
)
```

```

System.bool SetAutomaticSolve( 
   System.bool SolveFlag
) 
```

#### Parameters

*SolveFlag*
:   True if solving is on, false if it is off

#### Return Value

True if set, false if not

Remarks

If an application is making many changes in a sketch, then the Automatic Solve option may be turned off temporarily. After changes are completed, this option should be restored to its previous value, which can be obtained by calling [ISketch::GetAutomaticSolve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetAutomaticSolve.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[IModelDoc2::AutoSolveToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoSolveToggle.md)
