# GetID Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetID`

Gets the component ID for this component.
Gets the component ID for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

ID for this component

Remarks

A component ID:

- is unique within the context of the assembly to which it belongs.   
  **NOTE:** A component ID might not be unique across subassemblies within the assembly. For example, a component in subassembly A might have a component ID of 1, and a component in subassembly B might also have a component ID of 1.
- is persistent across SOLIDWORKS sessions and never changes, even if you [change the name of the component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.md).
- can be used to identify a specific component in an assembly. Use the component ID returned by this method with [IAssemblyDoc::GetComponentByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.md) to get a top-level assembly component.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get any component using its persistent reference ID.

Example

[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)  
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)  
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)  
[Get Component IDs (C#)](Get_Component_IDs_Example_CSharp.htm)  
[Get Component IDs (VB.NET)](Get_Component_IDs_Example_VBNET.htm)  
[Get Component IDs (VBA)](Get_Component_IDs_Example_VB.htm)  
[Get Top-level Components Using Component IDs (C#)](Get_Top-level_Component_Using_Component_IDs_Example_CSharp.htm)  
[Get Top-level Components Using Component IDs (VB.NET)](Get_Top-level_Component_Using_Component_IDs_Example_VBNET.htm)  
[Get Top-level Components Using Component IDs (VBA)](Get_Top-level_Component_Using_Component_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
