# Component Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Component`

Gets the assembly component referenced in this drawing component.
Gets the assembly component referenced in this drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Component As Component2
```

```

Dim instance As IDrawingComponent
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

Associated [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object for the referenced assembly document

Remarks

The associated [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object should have the same properties as the referenced configuration. For example, if the component is suppressed in the reference configuration, then the returned component should also be suppressed.

Example

[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)  
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)  
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)
