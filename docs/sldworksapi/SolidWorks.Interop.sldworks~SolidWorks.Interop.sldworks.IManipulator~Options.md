# Options Property (IManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Options`

Gets or sets whether the manipulator is deleted when a component in an assembly is modified or deleted.
Gets or sets whether the manipulator is deleted when a component in an assembly is modified or deleted.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Options As System.Integer
```

```

Dim instance As IManipulator
Dim value As System.Integer
 
instance.Options = value
 
value = instance.Options
```

```

System.int Options {get; set;}
```

```

property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Option as defined in [swManipulatorOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorOptions_e.html) (see **Remarks**)

Remarks

SOLIDWORKS recommends setting this property to swManipulatorOpts\_KeepAfterComponentModify when working in an assembly.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
