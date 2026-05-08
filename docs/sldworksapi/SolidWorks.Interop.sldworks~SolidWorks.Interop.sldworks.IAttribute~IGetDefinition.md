# IGetDefinition Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition`

Gets the definition of this attribute.
Gets the definition of this attribute.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDefinition() As AttributeDef
```

```

Dim instance As IAttribute
Dim value As AttributeDef
 
value = instance.IGetDefinition()
```

```

AttributeDef IGetDefinition()
```

```

AttributeDef^ IGetDefinition(); 
```

#### Return Value

[IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)

Remarks

SOLIDWORKS generates all attribute instances from an [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object. The object is the mold that gives the attribute its parameters and default values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)
