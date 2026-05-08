# Component Property (IMateInPlace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~Component`

Gets the component for this Inplace mate.
Gets the component for this Inplace mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Component As Component2
```

```

Dim instance As IMateInPlace
Dim value As Component2
 
value = instance.Component
```

```

Component2 Component {get;}
```

```

property Component2^ Component {
   Component2^ get();
}
```

#### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

The component instance tree of a subassembly is not loaded because a subassembly does not have a view of its own. Thus, this property returns NULL if the Inplace mate is in a subassembly.

Example

[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md)  
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.md)
