# GetAutomaticSolve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetAutomaticSolve`

Checks whether the computation to solve the sketch geometry of the part as modifications are automatically performed.
Checks whether the computation to solve the sketch geometry of the part as modifications are automatically performed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutomaticSolve() As System.Boolean
```

```

Dim instance As ISketch
Dim value As System.Boolean
 
value = instance.GetAutomaticSolve()
```

```

System.bool GetAutomaticSolve()
```

```

System.bool GetAutomaticSolve(); 
```

#### Return Value

True if automatic solving is on, false if off

Remarks

This method can be controlled with [ISketch::SetAutomaticSolve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetAutomaticSolve.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketchManager::AutoSolve Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoSolve.md)
