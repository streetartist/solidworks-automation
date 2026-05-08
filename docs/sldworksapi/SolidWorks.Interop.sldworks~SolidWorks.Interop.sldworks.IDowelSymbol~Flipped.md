# Flipped Property (IDowelSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~Flipped`

Gets or sets whether to flip this dowel symbol.
Gets or sets whether to flip this dowel symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Flipped As System.Boolean
```

```

Dim instance As IDowelSymbol
Dim value As System.Boolean
 
instance.Flipped = value
 
value = instance.Flipped
```

```

System.bool Flipped {get; set;}
```

```

property System.bool Flipped {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the dowel is flipped, false if it is not

Remarks

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after flipping the dowel pin symbol.

Example

[Flip Dowel Pin Symbol (VBA)](Flip_Dowel_Pin_Symbol_Example_VB.htm)  
[Flip Dowel Pin Symbol (C#)](Flip_Dowel_Pin_Symbol_Example_CSharp.htm)  
[Flip Dowel Pin Symbol (VB.NET)](Flip_Dowel_Pin_Symbol_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.md)  
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.md)
