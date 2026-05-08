# GetDefinition Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition`

Gets the definition of this attribute.
Gets the definition of this attribute.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDefinition() As System.Object
```

```

Dim instance As IAttribute
Dim value As System.Object
 
value = instance.GetDefinition()
```

```

System.object GetDefinition()
```

```

System.Object^ GetDefinition(); 
```

#### Return Value

Object for the attribute definition

Remarks

SOLIDWORKS generates all attribute instances from an [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object. The object is the mold that gives the attribute its parameters and default values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[IAttribute::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.md)
