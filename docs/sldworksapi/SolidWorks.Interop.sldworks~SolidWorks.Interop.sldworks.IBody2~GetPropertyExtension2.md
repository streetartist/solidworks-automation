# GetPropertyExtension2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2`

Gets the specified property extension on this body.
Gets the specified property extension on this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPropertyExtension2( _
   ByVal ID As System.Integer _
) As System.Object
```

```

Dim instance As IBody2
Dim ID As System.Integer
Dim value As System.Object
 
value = instance.GetPropertyExtension2(ID)
```

```

System.object GetPropertyExtension2( 
   System.int ID
)
```

```

System.Object^ GetPropertyExtension2( 
   System.int ID
) 
```

#### Parameters

*ID*
:   (Size of the array returned by [IBody2::AddPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2.md)) - (Position of the property extension in the array)

#### Return Value

Value of the property extension

Remarks

IBody2::AddPropertyExtension2 adds property extensions to a last-in-first-out, 1-based array and returns the size of that array.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These three interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ResetPropertyExtension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.md)
