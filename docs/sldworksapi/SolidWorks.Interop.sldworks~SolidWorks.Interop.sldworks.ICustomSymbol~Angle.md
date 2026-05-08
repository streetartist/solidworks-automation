# Angle Property (ICustomSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~Angle`

Obsolete. Superseded by ISketchBlockInstance::Angle.
Obsolete. Superseded by [ISketchBlockInstance::Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As ICustomSymbol
Dim value As System.Double
 
instance.Angle = value
 
value = instance.Angle
```

```

System.double Angle {get; set;}
```

```

property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.md)  
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.md)
