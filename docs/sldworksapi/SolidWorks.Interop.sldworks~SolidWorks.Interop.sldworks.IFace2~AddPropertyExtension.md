# AddPropertyExtension Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AddPropertyExtension`

Adds a property extension to this face.
Adds a property extension to this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

```

Dim instance As IFace2
Dim PropertyExtension As System.Object
Dim value As System.Integer
 
value = instance.AddPropertyExtension(PropertyExtension)
```

```

System.int AddPropertyExtension( 
   System.object PropertyExtension
)
```

```

System.int AddPropertyExtension( 
   System.Object^ PropertyExtension
) 
```

#### Parameters

*PropertyExtension*
:   Value of the property extension to add to this face (see **Remarks**)

#### Return Value

1 if the property extension is added to the face, -1 if not

Remarks

This method does not support:

- adding multiple property extensions to the same face.
- faces obtained from reference surface bodies.

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the face.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPropertyExtension.md)  
[IFace2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ResetPropertyExtension.md)
