# GOSTNotation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTNotation`

Gets whether the GOST Use for notation option is set.
Gets whether the GOST Use for notation option is set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GOSTNotation As System.Boolean
```

```

Dim instance As ISFSymbol
Dim value As System.Boolean
 
instance.GOSTNotation = value
 
value = instance.GOSTNotation
```

```

System.bool GOSTNotation {get; set;}
```

```

property System.bool GOSTNotation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the GOST Use for notation option is set, false if it is not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::GOSTDefaultSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTDefaultSymbol.md)
