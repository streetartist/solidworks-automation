# GetScale3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetScale3`

Gets the scale for this block instance.
Gets the scale for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetScale3( _
   ByVal Ignoreparentscale As System.Boolean _
) As System.Double
```

```

Dim instance As ISketchBlockInstance
Dim Ignoreparentscale As System.Boolean
Dim value As System.Double
 
value = instance.GetScale3(Ignoreparentscale)
```

```

System.double GetScale3( 
   System.bool Ignoreparentscale
)
```

```

System.double GetScale3( 
   System.bool Ignoreparentscale
) 
```

#### Parameters

*Ignoreparentscale*
:   True to ignore the parent scale, false to not

#### Return Value

Scale: 0.0000001 to 500000

Remarks

Use [ISketchBlockInstance::Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale2.md) to set the scale.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
