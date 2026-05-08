# MakeVirtual2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual2`

Makes this component and optionally its child components virtual by saving them in the current assembly.
Makes this component and optionally its child components virtual by saving them in the current assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeVirtual2( _
   ByVal AlsoChildVirtual As System.Boolean _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim AlsoChildVirtual As System.Boolean
Dim value As System.Boolean
 
value = instance.MakeVirtual2(AlsoChildVirtual)
```

```

System.bool MakeVirtual2( 
   System.bool AlsoChildVirtual
)
```

```

System.bool MakeVirtual2( 
   System.bool AlsoChildVirtual
) 
```

#### Parameters

*AlsoChildVirtual*
:   True to make child components of this component virtual, false to keep the child components linked to external files

#### Return Value

True if this component and optionally its child components are saved in an assembly, false if not

Remarks

This method breaks the link to the external component file and optionally the links to any of its child component files. Existing references are ignored, and the component and optionally any of its child components are renamed.

Example

[Add Component and Mate (C#)](Add_Component_and_Mate_Example_CSharp.htm)  
[Add Component and Mate (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)  
[Add Component and Mate (VBA)](Add_Component_and_Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IsVirtual Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IComponent2::SaveVirtualComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IAssemblyDoc::InsertNewVirtualPart Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.md)  
[IModelDocExtension::IsVirtualComponent3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md)
