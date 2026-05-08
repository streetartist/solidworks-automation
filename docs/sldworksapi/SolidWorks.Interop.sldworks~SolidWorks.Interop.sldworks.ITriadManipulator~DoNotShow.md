# DoNotShow Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow`

Specifies which triad manipulator's control points to not show.
Specifies which triad manipulator's control points to not show.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DoNotShow As System.Integer
```

```

Dim instance As ITriadManipulator
Dim value As System.Integer
 
instance.DoNotShow = value
 
value = instance.DoNotShow
```

```

System.int DoNotShow {get; set;}
```

```

property System.int DoNotShow {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Control points to not show as defined in [swTriadManipulatorDoNotShow\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTriadManipulatorDoNotShow_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)
