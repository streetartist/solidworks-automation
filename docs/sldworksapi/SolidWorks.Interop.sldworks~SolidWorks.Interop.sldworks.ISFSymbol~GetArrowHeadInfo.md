# GetArrowHeadInfo Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo`

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.
Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadInfo() As System.Object
```

```

Dim instance As ISFSymbol
Dim value As System.Object
 
value = instance.GetArrowHeadInfo()
```

```

System.object GetArrowHeadInfo()
```

```

System.Object^ GetArrowHeadInfo(); 
```

#### Return Value

Array of doubles describing format (see **Remarks**)

Remarks

Format of return information is the following array of doubles:

|  |  |
| --- | --- |
| retval[0] | = Arrow length (leader into arrowhead) |
| retval[1] | = Arrowhead length |
| retval[2] | = Arrowhead width |
| retval[3] | = Arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.md)  
[ISFSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.md)  
[ISFSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex.md)  
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.md)
