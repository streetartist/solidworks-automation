# GetPropertyExtension Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPropertyExtension`

Gets the property extension on this face.
Gets the property extension on this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

```

Dim instance As IFace2
Dim ID As System.Integer
Dim value As System.Object
 
value = instance.GetPropertyExtension(ID)
```

```

System.object GetPropertyExtension( 
   System.int ID
)
```

```

System.Object^ GetPropertyExtension( 
   System.int ID
) 
```

#### Parameters

*ID*
:   0

#### Return Value

Value of the property extension

Remarks

SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ResetPropertyExtension.md)  
[IFace2::AddPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AddPropertyExtension.md)
