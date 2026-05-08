# GetPropertyExtension Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPropertyExtension`

Gets the specified property extension on this part document.
Gets the specified property extension on this part document.

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

Dim instance As IPartDoc
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
:   (Size of the array returned by [IPartDoc::AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~AddPropertyExtension.md)) - (Position of the property extension in the array) (see **Remarks**)

#### Return Value

Value of the property extension

Remarks

IPartDoc::AddPropertyExtension adds property extensions to a last-in-first-out, 1-based array and returns the size of that array. See the examples in **Example**.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Example

[Add and Get Property Extensions (C#)](Add_and_Get_Property_Extension_Example_CSharp.htm)  
[Add and Get Property Extensions (VB.NET)](Add_and_Get_Property_Extension_Example_VBNET.htm)  
[Add and Get Property Extensions (VBA)](Add_and_Get_Property_Extension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ResetPropertyExtension.md)
