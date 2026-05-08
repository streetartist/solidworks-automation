# AutoSolve Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoSolve`

Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it.
Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSolve As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
instance.AutoSolve = value
 
value = instance.AutoSolve
```

```

System.bool AutoSolve {get; set;}
```

```

property System.bool AutoSolve {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if automatic solve is on, false if off

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketch::GetAutomaticSolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetAutomaticSolve.md)
