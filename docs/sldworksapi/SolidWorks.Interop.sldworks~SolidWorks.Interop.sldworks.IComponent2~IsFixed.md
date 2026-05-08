# IsFixed Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsFixed`

Gets whether the component is fixed or floating.
Gets whether the component is fixed or floating.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsFixed() As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
value = instance.IsFixed()
```

```

System.bool IsFixed()
```

```

System.bool IsFixed(); 
```

#### Return Value

True if this component is fixed, false if it is floating

Remarks

This method only applies to the top level of components. To get the actual state of sub-assemblies, you must get the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object of the subassembly, show the desired configuration, and get the state (fixed or floating) of the lower components.

To determine if a component is fixed or floating, you must begin the traversal from the subassembly document in the appropriate configuration instead of from the root level. At the root level, all of the components in the subassembly are allowed to move.

Example

[Get Component by Name (C#)](Get_Component_by_Name_Example_CSharp.htm)  
[Get Component by Name (VB.NET)](Get_Component_by_Name_Example_VBNET.htm)  
[Get Component by Name (VBA)](Get_Component_by_Name_Example_VB.htm)  
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)  
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)  
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::FixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FixComponent.md)  
[IAssemblyDoc::TemporaryFixGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroup.md)  
[IAssemblyDoc::TemporaryFixGroupExit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroupExit.md)  
[IAssemblyDoc::UnfixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UnfixComponent.md)
