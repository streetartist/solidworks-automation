# ComponentReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ComponentReference`

Gets or sets a component reference for this component.
Gets or sets a component reference for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ComponentReference As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
instance.ComponentReference = value
 
value = instance.ComponentReference
```

```

System.string ComponentReference {get; set;}
```

```

property System.String^ ComponentReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Component reference string

Remarks

Call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) after setting a component reference.

To remove a component reference, set the component reference string to "".

Example

[Get Component Name from Selected Entity (VB.NET)](Get_Component_Name_From_Selected_Entity_Example_VBNET.htm)  
[Get Component Name from Selected Entity (VBA)](Get_Component_Name_From_Selected_Entity_Example_VB.htm)  
[Get Component Name from Selected Entity (C#)](Get_Component_Name_From_Selected_Entity_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
