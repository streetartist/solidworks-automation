# GetPropertyExtension Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyExtension`

Gets the specified property extension on this model.
Gets the specified property extension on this model.

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

Dim instance As IModelDoc2
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
:   (Size of  the array returned by [IModelDoc2::AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddPropertyExtension.md)) - (Position of the property extension in the array)

#### Return Value

Value of the property extension

Remarks

IModelDoc2::AddPropertyExtension adds property extensions to a last-in-first-out, 1-based array and returns the size of that array.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetPropertyExtension.md)
