# CreateMassProperty2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty2`

Creates a mass properties object.
Creates a mass properties object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateMassProperty2() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.CreateMassProperty2()
```

```

System.object CreateMassProperty2()
```

```

System.Object^ CreateMassProperty2(); 
```

#### Return Value

[IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)

Remarks

| If this document is a... | Then this method returns... |
| --- | --- |
| Part | A mass properties object with information about one or more bodies. Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the bodies. You can also specify more bodies after calling this method by setting [IMassProperty2::SelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.md). |
| Assembly | A mass properties object with information about one or more components. Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the components. You can also specify more components after calling this method by setting [IMassProperty2::SelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.md).  Bodies from multibody part components cannot be selected for mass properties calculations. |
| Model that does not apply (e.g., a part with surface bodies only) | Null or Nothing. |

Example

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)  
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)  
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
