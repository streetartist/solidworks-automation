# SetSymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbol`

Sets the type of symbol for this surface finish symbol.
Sets the type of symbol for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSymbol( _
   ByVal Symbol As System.Integer, _
   ByVal SurfaceTexture As System.Integer, _
   ByVal AllAround As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISFSymbol
Dim Symbol As System.Integer
Dim SurfaceTexture As System.Integer
Dim AllAround As System.Boolean
Dim value As System.Boolean
 
value = instance.SetSymbol(Symbol, SurfaceTexture, AllAround)
```

```

System.bool SetSymbol( 
   System.int Symbol,
   System.int SurfaceTexture,
   System.bool AllAround
)
```

```

System.bool SetSymbol( 
   System.int Symbol,
   System.int SurfaceTexture,
   System.bool AllAround
) 
```

#### Parameters

*Symbol*
:   Type of symbol as defined in [swSFSymType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)

*SurfaceTexture*
:   Symbol surface text type as defined in [swSFSymType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)

*AllAround*
:   True if symbol is All Around, false if symbol is Local

#### Return Value

True if symbol is set, false if it is not

Remarks

The Symbol argument must be one of the following values from the [swSFSymType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html) enumeration: swSFBasic, swSFMachining\_Req, swSFDont\_Machine, swSFJIS\_No\_Machining, swSFJIS\_Basic, or swSFJIS\_Machining\_Req.

[ISFSymbol::GetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbol.md) will get this value.

|  |  |
| --- | --- |
| **If the symbol is...** | **Then...** |
| swSFJIS\_No\_Machining or swSFJIS\_Basic | SurfaceTexture argument must be one of these values from the swSFSymType enumeration:  swSFJIS\_Surface\_Texture\_1, swSFJIS\_Surface\_Texture\_2, swSFJIS\_Surface\_Texture\_3,  or swSFJIS\_Surface\_Texture\_4.  For any other symbol types, this argument is ignored, and 0 should be passed in. The [ISFSymbol::GetSymbolSurfaceTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.md) method will get this value. |
| swSFBasic, swSFMachining\_Req, or swSFDont\_Machine | AllAround argument indicates whether this is an All Around or Local symbol.  Use [ISFSymbol::GetSymbolAllAround](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolAllAround.md) to get this value. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
