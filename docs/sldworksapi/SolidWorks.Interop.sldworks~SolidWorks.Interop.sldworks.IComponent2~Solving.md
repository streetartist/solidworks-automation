# Solving Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving`

Gets the Solve as option (rigid or flexible) of this component.
Gets the **Solve as** option (rigid or flexible) of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Solving As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.Solving
```

```

System.int Solving {get;}
```

```

property System.int Solving {
   System.int get();
}
```

#### Property Value

**Solve as** option as defined in [swComponentSolvingOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html)

Remarks

You can also use [IAssemblyDoc::CompConfigProperties4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.md) to set the **Solve as** state of a component.

This property only applies to subassembly components, not part components. If you try to get the **Solve as** option of a part component, this property returns -1.

Example

[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)  
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)  
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.md)
