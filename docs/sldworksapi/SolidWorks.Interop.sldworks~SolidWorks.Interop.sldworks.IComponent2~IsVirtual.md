# IsVirtual Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual`

Gets whether this component is a virtual component.
Gets whether this component is a virtual component.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsVirtual As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
instance.IsVirtual = value
 
value = instance.IsVirtual
```

```

System.bool IsVirtual {get; set;}
```

```

property System.bool IsVirtual {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the component is a virtual component, false if not

Remarks

When you create components in the context of an assembly, the software can save them inside the assembly file, and you can immediately begin modeling. Later, you can save the components to external files or delete them. Also, no **In-Place** mate is created, so you can position and constrain the component however you want.

Example

[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)  
[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)  
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.md)  
[IComponent2::SaveVirtualComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.md)  
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md)
