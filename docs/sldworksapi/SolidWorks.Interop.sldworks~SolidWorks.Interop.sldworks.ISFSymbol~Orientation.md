# Orientation Property (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation`

Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached.
Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Orientation As System.Integer
```

```

Dim instance As ISFSymbol
Dim value As System.Integer
 
instance.Orientation = value
 
value = instance.Orientation
```

```

System.int Orientation {get; set;}
```

```

property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Orientation as defined in [swSurfaceFinishSymbolOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceFinishSymbolOrientation_e.html)

Remarks

If setting the value to swSFOrientation\_UserDefined, then the angle at which the symbol is displayed does not change. Instead, use [ISFSymbol::SetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetAngle.md) to set the symbol to a user-specified angle, which automatically sets the orientation to swSFOrientation\_UserDefined.

Use [ISFSymbol::GetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAngle.md) to get the angle of the symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
