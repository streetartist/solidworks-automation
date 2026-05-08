# GetSymbolAllAround Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolAllAround`

Gets whether this symbol is All Around or Local for this surface finish symbol.
Gets whether this symbol is All Around or Local for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymbolAllAround() As System.Boolean
```

```

Dim instance As ISFSymbol
Dim value As System.Boolean
 
value = instance.GetSymbolAllAround()
```

```

System.bool GetSymbolAllAround()
```

```

System.bool GetSymbolAllAround(); 
```

#### Return Value

True if All Around symbol, false if Local symbol

Remarks

[ISFSymbol::GetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbol.md) returns one of the following values from the [swSFSymType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html) enumeration: swSFBasic, swSFMachining\_Req, swSFDont\_Machine, swSFJIS\_No\_Machining, swSFJIS\_Basic, or swSFJIS\_Machining\_Req.

|  |  |
| --- | --- |
| **If the symbol is...** | **Then use...** |
| swSFJIS\_No\_Machining or swSFJIS\_Basic | [ISFSymbol::GetSymbolSurfaceTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.md) to retrieve more information about the symbol.    It returns one of these values from the swSFSymType\_e enumeration: swSFJIS\_Surface\_Texture\_1, swSFJIS\_Surface\_Texture\_2, swSFJIS\_Surface\_Texture\_3, or swSFJIS\_Surface\_Texture\_4. |
| swSFBasic, swSFMachining\_Req, or swSFDont\_Machine | ISFSymbol::GetSymbolAllAround to retrieve more information about the symbol. This method returns a Boolean indicating whether this is an All Around or Local symbol. |

To set the symbol type, use [ISFSymbol::SetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbol.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
